-- SQL query to find the top 5 most ordered dishes in the last 30 days.

SELECT d.name AS dish_name, COUNT(*) AS order_count
FROM orders o
JOIN dishes d ON o.dish_id = d.id
WHERE o.order_date >= NOW() - INTERVAL '30 days'
GROUP BY d.name
ORDER BY order_count DESC
LIMIT 5;


-- SQL query to get a list of restaurants that have at least 5 different dishes on their menu.
SELECT r.name AS restaurant_name
FROM Restaurants r
JOIN Dishes d ON r.id = d.restaurant_id
GROUP BY r.id
HAVING COUNT(DISTINCT d.id) >= 5;