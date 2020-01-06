import time
import sys
import tempfile
import os
from flask import Flask
from flask import request
from shell_utils import shell, cd, env, path, quiet

app = Flask(__name__)

DB_USER = os.environ['PGUSER']

def create_filename(prefix, extension):
    return prefix + time.strftime("%Y%m%d-%H%M%S") + "." + extension

def store_to_file(content):
    filename = '/tmp/' + create_filename('migrationjob-', 'sql')
    with open(filename, "w") as text_file:
        text_file.write(content)
    return filename

def execute(sql_content):
    filename = store_to_file(sql_content)
    app.logger.info('SQL script ready for execution: %s', filename)
    output = shell('psql -f ' + filename, capture=True)
    app.logger.info("Output from script:")
    app.logger.info(output.stdout)

def migrate(schema_file_content, data_migration_file_content, source_db):
    final_sql = schema_file_content + data_migration_file_content
    final_sql = final_sql.replace("<%SOURCE-DB%>", f"dbname={source_db} user={DB_USER}")
    execute(final_sql)

def check_db_connection():
    try:
        output = shell('psql -c "SELECT VERSION();"', capture=True)
        if output.returncode == 0:
            return True
        else:
            app.logger.error(output.stderr)
            return False
    except Exception as e:
        app.logger.error(e)
        return False

@app.route('/')
def isalive():
    return 'I am alive', 200

@app.route("/migrations", methods=["POST"])
def run_migration():
    #uploaded_files = request.files.getlist("schema-file")
    schema_file_content = request.files['schema-file'].read().decode("utf-8") 
    data_migration_file_content = request.files['data-migration-file'].read().decode("utf-8") 
    source_db = request.values['source-db']
    app.logger.info('Got request to migrate from %s', source_db)
    migrate(schema_file_content, data_migration_file_content, source_db)
    return "ok", 201

@app.route('/health')
def check_health():
    if check_db_connection():
        return "db-connection ok", 200
    else:
        app.logger.error('health-check failed')
        return "db-connection failed", 500

if __name__ == "__main__":
    #migrate(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    app.run(host= '0.0.0.0', debug=True)