-- Importing the database dump from hbtn_0d_tvshows to my MySQL server

SELECT tv_genres.genre AS 'genre', COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
