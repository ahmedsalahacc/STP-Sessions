class Genre:
    def __init__(self, genre):
        self.genre = genre

    def getGenre(self):
        return self.genre

    # Abstract Function
    def addMovie(self):
        raise NotImplementedError("Abstract Function Needs to be Implemented ")


class ActionGenre(Genre):
    def __init__(self):
        super().__init__("Action")
        self.movies = []

    def addMovie(self, movie):
        movie = movie.capitalize()
        self.movies.append(movie)
        print("Added Action Movie")


class DramaGenre(Genre):
    def __init__(self):
        super().__init__("Drama")
        self.movies = []

    def addMovie(self, movie):
        movie = movie.upper()
        self.movies.append(movie)
        print("Added Drama Movie")


if __name__ == "__main__":
    actions = ActionGenre()
    print(actions.getGenre())
    dramas = DramaGenre()
    print(dramas.getGenre())
