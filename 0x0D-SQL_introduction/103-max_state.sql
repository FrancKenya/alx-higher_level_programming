-- Imports in hbtn_0c_0 database a table dump
-- Writes a script that displays the max temperature of each state (ordered by State name).
SELECT `state`, MAX(`value`) AS `max_temp` FROM `temperatures` GROUP BY `state` ORDER BY `state`;
