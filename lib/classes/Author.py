from article import Article # type: ignore

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Error: Name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise ValueError("Error: Author name is immutable once set.")

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def topic_areas(self):
        if not self.magazines():
            return None
        return list({magazine.category for magazine in self.magazines()})
