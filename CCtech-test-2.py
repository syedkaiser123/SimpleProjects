
from googlesearch import search

class Search:

	def __init__(self,keyword):

		self.keyword = keyword

	

	def getItem(self):


		links = []

		#searching the keyword and fetching each search result to append to links array
		for x in search(query=keyword, tld = "co.in", num = 20, stop = 20, pause = 2):

			links.append(x)

		#displaying the results from links array
		for i in links:
			print(i)



if __name__ == "__main__":

	#asking the user for a keyword
	keyword = input("Enter the keyword : ")

	find = Search(keyword)
	find.getItem()