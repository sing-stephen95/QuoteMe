from bs4 import BeautifulSoup
import requests

class QuoteMe:

    
    def __init__(self):
        self.soup = ''

    def requestPage(self, term):
    	"""Requests a search page from brainyquote.com with the defined term"""
        page = 'https://www.brainyquote.com/search_results.html?q=' + term
        r = requests.get(page)
        setSoup(request)

    def getResults(self):
    	"""Stores results from the search page in an array with author and quote"""
        for x in self.soup.find(id="quotesList").find_all(title="view quote"):
            print "\n" + x.text
            print x.find_next_sibling().text
		
    def getRepeatResult(self):
        """Iterates to the same element in the array retrieving the same result"""
        print "hello"
		
    def getNextResult(self):
    	"""Iterates to the next element in the array retrieving the next result"""
    	print "hello"

    def getPreviousResult(self):
    	"""Iterates to the previous element in the array retrieving the previous result"""
    	print "hello"
	
    def getRandomResult(self):
        """Returns random quote"""
        print "hello"
	
	def getAuthor(self):
		"""Returns the author"""
		print "hello"

test = QuoteMe()
test.requestPage("hate")
test.getResults()
