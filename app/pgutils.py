import time
import sys
import tempfile
import os
from shell_utils import shell, cd, env, path, quiet
import click

def create_filename(prefix, extension):
    return prefix + time.strftime("%Y%m%d-%H%M%S") + "." + extension

def store_to_file(content, directory):
    filename = directory + '/' + create_filename('migrationjob-', 'sql')
    with open(filename, "w") as text_file:
        text_file.write(content)
    return filename

@click.group()
def cli():
    pass

@cli.command()
def test():
    """Test db-connection. 
    Do not forget to set environment variables for PSQL to access the database (e.g. PGPASSWORD)"""
    click.echo("Checking database connection.")
    try:
        output = shell('psql -c "SELECT VERSION();"', capture=True)
        if output.returncode == 0:
            click.echo('Database connection was successful')
            return True
        else:
            click.echo(output.stderr)
            click.echo('Database connection failed')
            return False
    except Exception as e:
        click.echo(e)
        click.echo('Database connection failed')
        return False

@cli.command()
@click.option('--schema-file', required=True, type=click.File('r'), help='SQL file to create the target database and the target schema.')
@click.option('--data-file', required=True, type=click.File('r'), help='SQL file to copy data from a source database to the target database')
@click.option('--work-directory', type=click.Path(exists=True, writable=True), default='/tmp', help='Workfolder to store temporary files. The default value is /tmp')
@click.option('--source-db', required=True, help='The name of the database from which the data will be migrated to the target database.')
@click.option('--target-db', required=True, help='The name of the database to which the data will be migrated.')
def migrate(schema_file, data_file, work_directory, source_db, target_db):
    """Migrate existing database and data to a fresh database. 
    Do not forget to set environment variables for PSQL to access the database (e.g. PGPASSWORD)"""
    click.echo(f"Migrating from {source_db} to {target_db}. Using {click.format_filename(work_directory)} as working-directory.")
    
    final_sql = schema_file.read() + '\n' + data_file.read()
    final_sql = final_sql.replace("<%SOURCE-DB%>", source_db)
    final_sql = final_sql.replace("<%TARGET-DB%>", target_db)
    final_sql = final_sql.replace("<%DB-USER%>", os.environ['PGUSER'])
    final_sql_file = store_to_file(final_sql, click.format_filename(work_directory))

    click.echo(f'SQL script ready for execution: {final_sql_file}')
    output = shell('psql -f ' + final_sql_file, capture=True)
    click.echo(output.stdout)
    if output.returncode == 0:
        click.echo('Migration completed successfully.')
    else:
        click.echo('Migration failed.')

if __name__ == '__main__':
    cli()