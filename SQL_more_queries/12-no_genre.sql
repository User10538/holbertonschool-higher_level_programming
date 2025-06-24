-- This script import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT show_id FROM tv_show_genres
) ORDER BY tv_shows.title ASC, genre_id ASC;
