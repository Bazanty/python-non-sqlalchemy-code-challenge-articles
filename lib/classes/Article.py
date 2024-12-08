class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, author):
            raise ValueError("Error: Author must be of type Author.")
        if not isinstance(magazine, magazine):
            raise ValueError("Error: Magazine must be of type Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Error: Title must be a string between 5 and 50 characters.")
        
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise ValueError("Error: Title is immutable once set.")
