from enum import Flag, auto


class MovieGenres(Flag):
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()


class Movie:
    def __init__(self, name, ganres):
        self.name = name
        self.ganres = ganres

    def in_genre(self, garnes):
        return garnes in self.ganres

    def __str__(self):
        return f'{self.name}'


if __name__ == '__main__':

    movie = Movie('Любовь и голуби', MovieGenres.DRAMA | MovieGenres.COMEDY)

    print(movie.in_genre(MovieGenres.DRAMA))
    print(movie.in_genre(MovieGenres.ACTION))
    print(movie.in_genre(MovieGenres.DRAMA | MovieGenres.COMEDY))
    print(movie)
