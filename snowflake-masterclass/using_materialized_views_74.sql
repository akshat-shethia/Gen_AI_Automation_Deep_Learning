-- Remove caching just to have a fair test -- Part 1

ALTER SESSION SET USE_CACHED_RESULT=FALSE; -- disable global caching
ALTER warehouse compute_wh suspend;
ALTER warehouse compute_wh resume;



-- Prepare table
CREATE OR REPLACE TRANSIENT DATABASE ORDERS;

CREATE OR REPLACE SCHEMA TPCH_SF100;

CREATE OR REPLACE TABLE TPCH_SF100.ORDERS AS
SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF100.ORDERS;

SELECT * FROM ORDERS LIMIT 100;



-- Example statement view -- 
SELECT
YEAR(O_ORDERDATE) AS YEAR,
MAX(O_COMMENT) AS MAX_COMMENT,
MIN(O_COMMENT) AS MIN_COMMENT,
MAX(O_CLERK) AS MAX_CLERK,
MIN(O_CLERK) AS MIN_CLERK
FROM ORDERS.TPCH_SF100.ORDERS
GROUP BY YEAR(O_ORDERDATE)
ORDER BY YEAR(O_ORDERDATE);




-- Create materialized view
CREATE OR REPLACE MATERIALIZED VIEW ORDERS_MV
AS 
SELECT
YEAR(O_ORDERDATE) AS YEAR,
MAX(O_COMMENT) AS MAX_COMMENT,
MIN(O_COMMENT) AS MIN_COMMENT,
MAX(O_CLERK) AS MAX_CLERK,
MIN(O_CLERK) AS MIN_CLERK
FROM ORDERS.TPCH_SF100.ORDERS
GROUP BY YEAR(O_ORDERDATE);


SHOW MATERIALIZED VIEWS;

-- Query view
SELECT * FROM ORDERS_MV
ORDER BY YEAR;



-- UPDATE or DELETE values
UPDATE ORDERS
SET O_CLERK='Clerk#99900000' 
WHERE O_ORDERDATE='1992-01-01';





   -- Test updated data --
-- Example statement view -- 
SELECT
YEAR(O_ORDERDATE) AS YEAR,
MAX(O_COMMENT) AS MAX_COMMENT,
MIN(O_COMMENT) AS MIN_COMMENT,
MAX(O_CLERK) AS MAX_CLERK,
MIN(O_CLERK) AS MIN_CLERK
FROM ORDERS.TPCH_SF100.ORDERS
GROUP BY YEAR(O_ORDERDATE)
ORDER BY YEAR(O_ORDERDATE);



-- Query view
SELECT * FROM ORDERS_MV
ORDER BY YEAR;


SHOW MATERIALIZED VIEWS;