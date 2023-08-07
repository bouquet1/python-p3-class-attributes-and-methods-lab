class Song:

    # Create a class attribute, count and set it to 0.
    count = 0
    # Create a genres attribute, equal to an empty list.
    genres = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        # Your __init__ method should call a class method that increments the value of count by one.
        self.add_song_to_count()
        # genres list when a new song is created
        self.add_to_genres(genre)

    # class method increments the value of count by one

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        # control for duplicates
        if genre not in cls.genres:
            cls.genres.append(genre)


# test ur code
