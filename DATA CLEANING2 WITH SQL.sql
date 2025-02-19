-- DATA CLEANING
#Data Cleaning: Here, we get the data in a more usable format, by fixing a lot of issues in the raw data.


SELECT *
FROM world_layoffs.layoffs;

-- STEP 1. Remove duplicates
-- STEP 2. Standardize the Data
-- STEP 3. Null Values or blank values
-- STEP 4. Remove Any Columns

#Note that removing a column from a data bank can pose a big issue later. Therefore, we would create a staging or raw dataset in proxy of the original data set.

SELECT *
FROM world_layoffs.layoffs;

-- CREATE A PROXY
CREATE TABLE world_layoffs.layoff_sample
LIKE world_layoffs.layoffs;

#Check out the Proxy Table
SELECT *
FROM world_layoffs.layoff_sample;

-- INSERT THE DATA IN 'LAYOFFS' INTO 'LAYOFF_SAMPLE'
INSERT world_layoffs.layoff_sample
SELECT *
FROM world_layoffs.layoffs;

-- STEP 1. Remove duplicates
# But we check the duplicates first by using row number
SELECT *,
ROW_NUMBER () OVER (PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions) row_num
FROM world_layoffs.layoff_sample;

# LET'S CREATE A CTE
WITH duplicates_cte AS
(
SELECT *,
ROW_NUMBER () OVER (PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions) AS row_num
FROM world_layoffs.layoff_sample
)
SELECT *
FROM duplicates_cte
WHERE row_num > 1;

# It is wise to create another prototype table like that of "world_layoffs.layoff_sample".

CREATE TABLE world_layoffs.`layoff_sample4` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




INSERT INTO world_layoffs.layoff_sample4
SELECT *,
ROW_NUMBER () OVER (PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, `date`, stage,
country, funds_raised_millions) row_num
FROM world_layoffs.layoff_sample;


SELECT*
FROM world_layoffs.layoff_sample4
WHERE row_num > 1;

DELETE
FROM world_layoffs.layoff_sample4
WHERE row_num > 1;

SELECT*
FROM world_layoffs.layoff_sample4;

WITH duplicates_cte AS
(
SELECT *,
ROW_NUMBER () OVER (PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions) AS row_num1
FROM world_layoffs.layoff_sample4
)
SELECT *
FROM duplicates_cte
WHERE row_num1 > 1;

SELECT*
FROM world_layoffs.layoff_sample4;


-- STEP 2: STANDARDIZING DATA
#This is about finding issues in my data and fixing it.

SELECT company, TRIM(company)
FROM world_layoffs.layoff_sample4;

# Note that, TRIM takes off the white space off the end. We then update our data set in the respect, below:

UPDATE world_layoffs.layoff_sample4
SET company = TRIM(company);

# We then take a look at the INDUSTRY

SELECT DISTINCT(industry)
FROM world_layoffs.layoff_sample4
ORDER BY 1;
SELECT *
FROM world_layoffs.layoff_sample4
WHERE industry LIKE 'Crypto%';

UPDATE world_layoffs.layoff_sample4
SET industry = 'Crypto'
WHERE industry LIKE 'Crypto%';

#Let's look at LOCATION
SELECT DISTINCT(location)
FROM world_layoffs.layoff_sample4
ORDER BY 1;

#Let's look at COUNTRY
SELECT DISTINCT country
FROM world_layoffs.layoff_sample4
ORDER BY 1;

SELECT *
FROM world_layoffs.layoff_sample4
WHERE country LIKE 'United States%';

# We can use 'TRAILING' to cut characters from a data point.
SELECT DISTINCT country, TRIM(TRAILING '.' FROM country)
FROM world_layoffs.layoff_sample4;

UPDATE world_layoffs.layoff_sample4
SET country = TRIM(TRAILING '.' FROM country)
WHERE country LIKE 'United State%';

SELECT *
FROM world_layoffs.layoff_sample4;

# NOW WE NEED TO CONVERT THE DATE COLUMN FROM 'TEXT' TO 'DATE' COLUMN.
SELECT `date`,
STR_TO_DATE(`date`, '%m/%d/%Y')
FROM world_layoffs.layoff_sample4;

UPDATE world_layoffs.layoff_sample4
SET `date` = STR_TO_DATE(`date`, '%m/%d/%Y');

SELECT `date`
FROM world_layoffs.layoff_sample4;


#We can modify the date column now from 'text to 'date' column.

ALTER TABLE world_layoffs.layoff_sample4
MODIFY COLUMN `date` DATE;

SELECT *
FROM world_layoffs.layoff_sample4;

-- STEP 3. NULL VALUES OR BLANK VALUES
SELECT *
FROM world_layoffs.layoff_sample4
WHERE total_laid_off IS NULL
AND percentage_laid_off IS NULL;

UPDATE world_layoffs.layoff_sample4
SET industry = NULL
WHERE industry = '';

SELECT *
FROM world_layoffs.layoff_sample4
WHERE industry IS NULL
OR industry = '';

# Here, 'Airbnb', 'Ballys_Interactive', 'Cavana', 'Juul' are npot classified into sectors. 
#Let's treat 'AIRBNB', to start with.

SELECT *
FROM world_layoffs.layoff_sample4
WHERE company = 'Airbnb';

#We can populate the missing cell in the industry column for Airbnb
SELECT t1.industry, t2.industry
FROM world_layoffs.layoff_sample4 t1
JOIN world_layoffs.layoff_sample4 t2
	ON t1.company = t2.company
    AND t1.location = t2.location
WHERE t1.industry IS NULL
AND t2.industry IS NOT NULL;

UPDATE world_layoffs.layoff_sample4 t1
JOIN world_layoffs.layoff_sample4 t2
	ON t1.company = t2.company
SET t1.industry = t2.industry
WHERE t1.industry IS NULL
AND t2.industry IS NOT NULL;



-- STEP 4. Remove Any Columns
# Here we will delete rows with no entry.

SELECT *
FROM world_layoffs.layoff_sample4
WHERE total_laid_off IS NULL
AND percentage_laid_off IS NULL;

#Because there is no how we can calculate for the missing values of the result of the above query, we have to then have to delete those rows with this peculiarity

DELETE
FROM world_layoffs.layoff_sample4
WHERE total_laid_off IS NULL
AND percentage_laid_off IS NULL; 

# LET'S CHECK OUR DATA TO SEE IF THE ABOVE QUERY HAS BEEN EFFECTED
SELECT *
FROM world_layoffs.layoff_sample4
WHERE total_laid_off IS NULL
AND percentage_laid_off IS NULL;

SELECT *
FROM world_layoffs.layoff_sample4;

#We will remove the 'row number' column with the query below;

ALTER TABLE world_layoffs.layoff_sample4
DROP row_num;

#We thencheck our data to see if the 'row number column has been dropped.
SELECT *
FROM world_layoffs.layoff_sample4;

-- THE END -----------------------------------------------------------