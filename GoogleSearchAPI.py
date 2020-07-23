from flask import Flask, render_template, request, redirect
import urllib
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse




app = Flask(__name__)
app.config["DEBUG"] = True

result = []

class Search:

	def __init__(self,string):

		self.string = string
	
		

	def getItem(self):
		
		#searching the keyword and fetching each search result to append to links array
		string = self.string

		url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(string)
	    
		
		response = requests.get(url)
		if response.status_code==200:
			soup = BeautifulSoup(response.text, 'lxml')
			a = soup.find_all('a') 
			for i in a:
				k = i.get('href')
				try:
					m = re.search("(?P<url>https?://[^\s]+)", k)
					n = m.group(0)
					j = n.split('&')[0]
					domain = urlparse(j)
					if(re.search('google.com', domain.netloc)):
						continue
					else:
						result.append(j)
				except:
					continue
		

		return result





@app.route('/', methods = ['GET','POST'])
def home():

	if request.method == 'GET':
		return render_template('home.html')

	
	if request.method == 'POST':

		keyword = request.form.get('word')

		find = Search(keyword)
		result = find.getItem()


	return render_template('home.html', result=result)




if __name__ == "__main__":

	
	app.run()

