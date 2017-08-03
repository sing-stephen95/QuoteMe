from bs4 import BeautifulSoup
import requests

class QuoteMe:

    
    def __init__(self):
        self.soup = ''

    def requestPage(self, term):
        page = 'https://www.brainyquote.com/search_results.html?q=' + term
        r = requests.get(page)
        setSoup(request)

    def getResults(self):
        for x in self.soup.find(id="quotesList").find_all(title="view quote"):
            print "\n" + x.text
            print x.find_next_sibling().text

test = QuoteMe()
test.requestPage("hate")
test.getResults()
