INSERT INTO SDB.account (username, password, email, active) 
SELECT * FROM dblink('dbname=<%SOURCE-DB%> user=<%DB-USER%>', 'SELECT username, password, email, TRUE AS active FROM SDB.account') 
AS account_src(username VARCHAR (50), password VARCHAR (50), email VARCHAR (50), active BOOLEAN);
