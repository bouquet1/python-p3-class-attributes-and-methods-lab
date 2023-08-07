class Song:

    count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
