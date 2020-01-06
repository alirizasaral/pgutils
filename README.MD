# Installation


## migrate database to a new version
`psql-utils-migrate --schema-script create-schema.sql --data-migration-script migrate-data.sql --db-source mydb_1_0_0`

- create DB MYDB_1_0_0
- insert data
- create DB MYDB_2_0_1
- migrate data from MYDB_1_0_0

