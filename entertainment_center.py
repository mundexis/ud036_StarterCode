import fresh_tomatoes
import media

# Fargo movie: movie title, link to movie poster image, and link to movie trailer.
fargo = media.Movie(
    'Fargo',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTgxNzY3MzUxOV5BMl5BanBnXkFtZTcwMDA0NjMyNA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg',
    'https://youtu.be/h2tY82z3xXU'
)

# Trainspotting movie: movie title, link to movie poster image, and link to movie trailer.
trainspotting = media.Movie(
    'Trainspotting', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMzA5Zjc3ZTMtMmU5YS00YTMwLWI4MWUtYTU0YTVmNjVmODZhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_SX675_AL_.jpg', 'https://youtu.be/8LuxOYIpu-I'
)

# Trainspotting 2 movie: movie title, link to movie poster image, and link to movie trailer.
trainspotting2 = media.Movie(
    'T2 Trainspotting',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NTA0NDM0MF5BMl5BanBnXkFtZTgwMDMzMTQzMTI@._V1_SY1000_CR0,0,666,1000_AL_.jpg',
    'https://youtu.be/EsozpEE543w'
)

# American Psycho movie: movie title, link to movie poster image, and link to movie trailer.
american_psycho = media.Movie(
    'American Psycho',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyMTYwMTI0N15BMl5BanBnXkFtZTgwNTU2NTYxMTE@._V1_.jpg',
    'https://youtu.be/18-ZIKUZwTQ'
)

# Zootopia movie: movie title, link to movie poster image, and link to movie trailer.
zootopia = media.Movie(
    'Zootopia',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BOTMyMjEyNzIzMV5BMl5BanBnXkFtZTgwNzIyNjU0NzE@._V1_SY1000_SX675_AL_.jpg',
    'https://youtu.be/jWM0ct-OLsM'
)

# Jungle Book movie: movie title, link to movie poster image, and link to movie trailer.
jungle_book = media.Movie(
    'The Jungle Book',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTc3NTUzNTI4MV5BMl5BanBnXkFtZTgwNjU0NjU5NzE@._V1_SY1000_SX675_AL_.jpg',
    'https://www.youtube.com/watch?v=C4qgAaxB_pc'
)

# Lion King movie: movie title, link to movie poster image, and link to movie trailer.
lion_king = media.Movie(
    'The Lion King',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_SY1000_CR0,0,673,1000_AL_.jpg',
    'https://youtu.be/vgEAkOtl1FE'
)

# No Country for Old Men movie: movie title, link to movie poster image, and link to movie trailer.
no_country_for_old_med = media.Movie(
    'No Country For Old Men',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5Njk3MjM4OV5BMl5BanBnXkFtZTcwMTc5MTE1MQ@@._V1_.jpg',
    'https://youtu.be/81aDGWCAetw'
)

# Pulp Fiction movie: movie title, link to movie poster image, and link to movie trailer.
pulp_fiction = media.Movie(
    'Pulp Fuction',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg',
    'https://youtu.be/s7EdQ4FqbhY'
)

# Create a list of movies to be displayed on the website.
movies = [
    fargo,
    trainspotting,
    trainspotting2,
    pulp_fiction,
    american_psycho,
    no_country_for_old_med,
    zootopia,
    jungle_book,
    lion_king]

# Display the list of movies in a web page.
fresh_tomatoes.open_movies_page(movies)
