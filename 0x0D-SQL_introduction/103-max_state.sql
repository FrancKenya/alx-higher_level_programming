-- Imports in hbtn_0c_0 database a table dump
-- Writes a script that displays the max temperature of each state (ordered by State name).

SELECT state, MAX(temperature) AS max_temperature FROM Temperatures GROUP BY state ORDER BY state;
