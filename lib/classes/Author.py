from lib.Article import Article # type: ignore

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []
    
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        magazines = []
        for article in self._articles:
            magazine = article.magazine()
            if magazine not in magazines:#if condition is true
                magazines.append(magazine)
        return magazines

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)

    def topic_areas(self):
        categories = []
        for article in self._articles:
            magazine = article.magazine()
            category = magazine.category()
            if category not in categories:
                categories.append(category)
        return categories