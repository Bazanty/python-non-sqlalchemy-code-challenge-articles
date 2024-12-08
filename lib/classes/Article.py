class Article:
    all = []  # Class variable to hold all articles

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        # Append the instance to the class variable 'all'
        Article.all.append(self)


    def title(self):
        return self._title

    @classmethod
    def all(cls):
        return cls._all

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine