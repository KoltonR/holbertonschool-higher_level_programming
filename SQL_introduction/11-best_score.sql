-- script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in the MySQL server.
-- results are displayed both the score and the name (in this order) ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;