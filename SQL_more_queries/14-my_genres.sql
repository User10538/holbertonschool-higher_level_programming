-- This script import the database dump from hbtn_0d_tvshows to your MySQL

SELECT tv_genres.name 
FROM tv_shows 
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id 
WHERE title = 'Dexter' 
ORDER BY tv_genres.name ASC
