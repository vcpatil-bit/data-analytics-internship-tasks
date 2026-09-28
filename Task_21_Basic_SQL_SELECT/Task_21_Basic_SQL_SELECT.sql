SHOW DATABASES;
USE world;
SHOW TABLES;
SELECT *
FROM city
LIMIT 10;
SELECT Name, CountryCode, Population
FROM city
LIMIT 10;
SELECT Name, CountryCode, Population
FROM city
WHERE CountryCode = 'IND';
SELECT Name, CountryCode, Population
FROM city
WHERE Population > 1000000;

SELECT Name, CountryCode, Population
FROM city
ORDER BY Population DESC
LIMIT 10;

SELECT Name, CountryCode, Population
FROM city
ORDER BY Population ASC
LIMIT 10;

-- Query 7
SELECT Name, CountryCode, Population
FROM city
WHERE CountryCode = 'IND'
ORDER BY Population DESC;

-- Query 8
SELECT Name, CountryCode, Population
FROM city
WHERE Population > 500000
ORDER BY Population DESC;

-- Query 9
SELECT Name, Continent, Population
FROM country
WHERE Continent = 'Asia'
ORDER BY Population DESC
LIMIT 10;

-- Query 10
SELECT Name, Continent, Population
FROM country
WHERE Population > 50000000
ORDER BY Population DESC;

