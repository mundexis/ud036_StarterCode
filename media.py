import webbrowser


class Movie():
    """Create a movie class."""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Initialize a movie object.

        Keyword arguments:
        title -- the title of the movie.
        poster_image_url -- link to the movie's poster.
        trailer_youtube_url -- link to the movie's trailer.
        """

        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Display the movie trailer using the web browser."""
        webbrowser.open(self.trailer_youtube_url)
