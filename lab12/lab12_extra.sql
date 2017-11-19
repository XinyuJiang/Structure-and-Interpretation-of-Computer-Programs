.read lab12.sql

CREATE TABLE sp17favnum AS
  SELECT number, COUNT(*) AS count FROM sp17students GROUP BY number
  ORDER BY count DESC LIMIT 1;


CREATE TABLE sp17favpets AS
  SELECT pet,COUNT(*) AS count FROM sp17students GROUP BY number
  ORDER BY count DESC LIMIT 10;


CREATE TABLE fa17favpets AS
  SELECT pet,COUNT(*) AS count FROM students GROUP BY number
  ORDER BY count DESC LIMIT 10;

CREATE TABLE fa17dog AS
  SELECT pet,COUNT(*) AS count FROM students WHERE pet = 'dog' GROUP BY number 
  ORDER BY count DESC LIMIT 1;


CREATE TABLE fa17alldogs AS
  SELECT pet,COUNT(*) AS count FROM students WHERE pet LIKE '%dog%' GROUP BY number 
  ORDER BY count DESC LIMIT 1;


CREATE TABLE obedienceimages AS
  SELECT seven,denero,hilfinger,COUNT(*) AS count FROM students 
  WHERE seven = '7' GROUP BY denero,hilfinger ORDER BY denero;


CREATE TABLE smallest_int_count AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
