-- 1. Let’s examine the three tables.

SELECT * FROM trips;
SELECT * FROM riders; 
SELECT * FROM cars;

-- Question 2 - theoretical question. 

-- Question 3: try out a simple cross join between riders and cars. Is the result useful?

SELECT riders.first,
   riders.last,
   cars.model
FROM riders, cars;


-- Question 4: suppose we want to create a Trip Log with the trips and its users. Find the columns to join between trips and riders and combine the two tables using a LEFT JOIN. Let trips be the left table.

SELECT *
FROM riders
LEFT JOIN trips
ON riders.id = trips.id;


-- 5. Suppose we want to create a link between the trips and the cars used during those trips. Find the columns to join on and combine the trips and cars table using an INNER JOIN.

SELECT *
FROM trips
JOIN cars ON trips.car_id = cars.id;


-- 6. The new riders data are in! There are three new users this month. Stack the riders table on top of the new table named riders2.

SELECT *
FROM riders
UNION SELECT * FROM riders2;


-- 7. What is the average cost for a trip?
SELECT AVG(cost) FROM trips;


-- 8. Lyft is looking to do an email campaign for all the irregular users. Find all the riders who have used Lyft less than 500 times!

SELECT * FROM riders 
WHERE total_trips < 500
ORDER BY id;

-- 9. Calculate the number of cars that are active.
SELECT * FROM cars
WHERE status = 'active';

-- 10. Write a query that finds the two cars that have the highest trips_completed.

SELECT MAX(trips_completed)
FROM cars; 

-- OR:

SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;
