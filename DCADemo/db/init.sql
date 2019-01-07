CREATE DATABASE volve;
use volve;

CREATE TABLE production (
  wellname VARCHAR(20),
  year YEAR(4),
  month INT,
  oil FLOAT,
  gas FLOAT
);

LOAD DATA LOCAL INFILE 'Volve production data clean.csv' 
INTO TABLE production 
FIELDS TERMINATED BY ';' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Wellbore_name,Year,Month,Oil,Gas);