-- genre id all shows
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows, tv_show_genres
    WHERE
        CASE
            WHEN tv_show_genres.genre_id NOT NULL
                THEN tv_shows.id = tv_show_genres.genre_id
                ELSE tv_show_genres.genre_id = 'NULL'
        END

    ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;