SELECT COUNT(*) AS total_titles
FROM netflix_titles;

SELECT 
    type,
    COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY type
ORDER BY total_titles DESC;

SELECT 
    release_year,
    COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY release_year
ORDER BY release_year;

SELECT 
    listed_in AS genre,
    COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY listed_in
ORDER BY total_titles DESC
LIMIT 10;

SELECT 
    country,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE country IS NOT NULL
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;

vSELECT 
    rating,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE rating IS NOT NULL
GROUP BY rating
ORDER BY total_titles DESC;

SELECT 
    YEAR(date_added) AS added_year,
    COUNT(*) AS titles_added
FROM netflix_titles
WHERE date_added IS NOT NULL
GROUP BY YEAR(date_added)
ORDER BY added_year;

SELECT 
    release_year,
    type,
    COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY release_year, type
ORDER BY release_year, type;

SELECT 
    title,
    type,
    release_year,
    rating
FROM netflix_titles
WHERE release_year >= 2020
ORDER BY release_year DESC;

SELECT 
    type,
    ROUND(AVG(release_year), 2) AS average_release_year
FROM netflix_titles
GROUP BY type;

