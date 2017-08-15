"""
Module to display movie object, attributes and instances
"""

import webbrowser
"""
Class object stores movie related information
"""


class Movie():
    def __init__(
        self,
        title,
        storyline,
        poster_image_url,
        trailer_youtube_url
    ):

    """
    Initialize instance of class Movie

    :param title:
    :param storyline:
    :param poster_image_url:
    :param trailer_youtube_url
    """
    self.title = title
    self.storyline = storyline
    self.poster_image_url = poster_image_url
    self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
    	"""
    	Initializing instane for opening the youtube video
    	:return: webbrowser to play trailer
    	"""
        webbrowser.open(self.trailer_youtube_url)
