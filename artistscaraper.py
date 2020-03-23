from bs4 import BeautifulSoup
import requests
import json
from urllib2 import Request, urlopen

# iterate through the websites that are within festref.json (list of dictionaries)
# create a list of dictionaries for the festival and list of artists

artistArr = []

with open('festref.json', 'r') as festfile:

	festdata = json.load(festfile)

	for fest in range(len(festdata)):


		url = festdata[fest]['ref']
		fest_name = festdata[fest]['festival']
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req).read()
		content = BeautifulSoup(webpage, "html.parser")

		#date and location
		dateloc = content.find('div', {'class': 'headerblock'}).findAll('p')
		dateloc_length = len(dateloc)
		dateloc_list = []
		for i in range(dateloc_length):
			dateloc_list.append(dateloc[i].string)

		artists = content.findAll('li')
		artist_length = len(artists)
		artist_list = []
		artistObject ={}
		for i in range(artist_length):

			if artists[i].string in (None, "Login", "Sign up", "Latest News", "All Festivals", "US Festivals", "Europe Festivals", "UK Festivals", "Artists on Tour", "Festival Posters", "Best Festivals", "Festival Gear", "Festival Travel", "Reviews", "Photos","100 Nights of Summer","Top 100 USA", "Top 100 Europe", "Home","Festival News","Festival Travel"):

				continue
        		
			else :

				artist_list.append(artists[i].string)


		artistObject = {

			"festival" : fest_name,
			"location" : dateloc_list[0],
			"dates" : dateloc_list[1],
			"artists" : artist_list

			}


		artistArr.append(artistObject)



with open('festartists.json', 'w') as outfile:
	json.dump(artistArr, outfile, indent = 4)


