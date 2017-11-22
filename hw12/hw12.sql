CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name AS name, b.size AS size FROM dogs as a ,sizes as b 
  WHERE a.height>min AND a.height <= max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT b.child FROM dogs as a, parents as b WHERE b.parent = a.name ORDER by a.height DESC;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  with 
    property (child,parent,size) as (
      select b.child,b.parent,c.size FROM dogs as a,parents as b, size_of_dogs as c 
      WHERE b.parent = a.name AND b.child = c.name
      )
  SELECT a.child || " and " || b.child || " are " || a.size || " siblings" FROM property as a, property as b 
  WHERE a.parent = b.parent AND a.size = b.size AND a.child<b.child ORDER by a.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks AS
  with
    counter(count,name,height,lasthight) as (
        select 1,d.name,d.height,d.height FROM dogs as d union
        select counter.count+1,counter.name || ", " || d.name,counter.height + d.height,d.height 
        FROM dogs as d, counter WHERE count<5 and d.height>lasthight -- we need to keep track the last added dog's height so the order could be increasing
        -- we don't need to consider more about d.height'order, if we recursion use this subtable and enumerate everything, when we print the table the order will be something we want
      )
  SELECT c.name ||"|"|| c.height FROM counter as c WHERE c.count = 4 AND c.height>170 ORDER BY c.height;
