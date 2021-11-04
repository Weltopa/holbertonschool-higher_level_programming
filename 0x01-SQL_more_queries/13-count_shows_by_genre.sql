-- Grouped by genre
SELECT tv_genres.name genre, tv_show_genres.genre_id FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name, tv_show_genres.genre_id
ORDER BY number_ofshows DESC;
