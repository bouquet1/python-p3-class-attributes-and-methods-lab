class Song:

    # Create a class attribute, count and set it to 0.
    count = 0
    # Create a genres attribute, equal to an empty list.
    genres = []
    # artists, that is equal to an empty list.
    artists = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        # Your __init__ method should call a class method that increments the value of count by one.
        self.add_song_to_count()
        # genres list when a new song is created
        self.add_to_genres(genre)
        # artists list
        self.add_to_artists(artist)

    # class method increments the value of count by one
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        # control for duplicates
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # control for duplicates
        if artist not in cls.artists:
            cls.artists.append(artist)


# test ur code python lib/song.py
# song1 = Song("Song 1", "Artist 1", "Pop")
# song2 = Song("Song 2", "Artist 2", "Pop")
# song3 = Song("Song 3", "Artist 3", "Rock")

# print(Song.genres)
# print(Song.artists)
