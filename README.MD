# Description
This commandline utility contains various utilities for PostgreSQL. My starting point was a private project of mine, however
the requirements are generic and I kept the functionality general-purpose - free of any conventions or assumptions related to my private project.

# Before you begin
This project requires Python>3. If you are using conda, setup an environment and activate it:
`conda activate py3`

# Local Installation
In the app folder

`pip install --editable .`

Once installed, you can use it like

`pgutils --help`

# Commands
## Migrate database
Database schemas evolve over time. You need DDM to alter the structure and DDL to update the data to the latest schema version.
If DDM manipulates the current schema version to the next one, it cannot be used to create a fresh schema during development and test.

This utility expects a DDM to create the schema from scratch into a fresh database. Once created, it executes the DDL to read the data from the database with the previous schema (using dblink), manipulate and write them to the new database. Here is a sample call:

`pgutils migrate --schema-file ../test-scripts/create-schema.sql --data-file ../test-scripts/migrate-data.sql --source-db sampledb_1_0_0 --target-db sampledb_2_0_0`

The scripts uses psql and assumes that:
- psql is installed
- all the relevant environment variables are set for the database connection (see https://www.postgresql.org/docs/9.1/libpq-envars.html)

The database credentials are ideally kept in the `~/.pgpass` file.




