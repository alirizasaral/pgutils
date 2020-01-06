curl \
  -F "source-db=sampledb1" \
  -F "target-db=sampledb3" \
  -F "schema-file=@../create-schema.sql" \
  -F "data-migration-file=@../migrate-data.sql" \
  http://localhost:5000/migrations