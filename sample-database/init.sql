CREATE DATABASE sampledb1;
GRANT ALL PRIVILEGES ON DATABASE sampledb1 TO docker;

\connect sampledb1;
CREATE SCHEMA SDB;

CREATE TABLE SDB.account(
   user_id serial PRIMARY KEY,
   username VARCHAR (50) UNIQUE NOT NULL,
   password VARCHAR (50) NOT NULL,
   email VARCHAR (355) NOT NULL
);

INSERT INTO SDB.account (username, password, email) values ('max1', 'max1234', 'max1@max.at');
INSERT INTO SDB.account (username, password, email) values ('max2', 'max1234', 'max2@max.at');
INSERT INTO SDB.account (username, password, email) values ('max3', 'max1234', 'max3@max.at');

CREATE DATABASE sampledb2;
GRANT ALL PRIVILEGES ON DATABASE sampledb2 TO docker;

\connect sampledb2;
CREATE SCHEMA SDB;
create extension dblink;

CREATE TABLE SDB.account(
   user_id serial PRIMARY KEY,
   username VARCHAR (50) UNIQUE NOT NULL,
   password VARCHAR (50) NOT NULL,
   active BOOLEAN NOT NULL,
   email VARCHAR (355) NOT NULL
);


