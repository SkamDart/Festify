from bs4 import BeautifulSoup
import requests
import json
from urllib2 import Request, urlopen

# iterates through https://www.musicfestivalwizard.com/festivals/XXX-music-festival-2020/
# where XXX is the music festival and grabs the inside

# need to iterate through the pages (1-7)- maybe expand to 10?

masterArr = []

for i in range (1,10):

	url = 'https://www.musicfestivalwizard.com/all-festivals/page/' + str(i) + '/?festival_guide=us-festivals&month&festivalgenre=electronic&festivaltype&festival_length&festival_size&camping&artist&company&sdate=Feb%208%2C%202020&edate=Dec%2031%2C%202020#038;month&festivalgenre=electronic&festivaltype&festival_length&festival_size&camping&artist&company&sdate=Feb+8%2C+2020&edate=Dec+31%2C+2020'
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	content = BeautifulSoup(webpage, "html.parser")

	#find festival names
	festival_header = content.findAll('h2')

	#grab the festival websites within musicfestivalwizard
	festival_ref = []
	for a in content.select('h2 a[href]'):
		festival_ref.append(a['href'])
	

	#create a list for the festival names
	festival_length = len(festival_header)
	festival_list = []
	for i in range(festival_length):

		festival_string = festival_header[i].string
		festival_list.append(festival_string)

	#print (festival_list)

	#create an Array with the festival name and its corresponding website
	#festivalArr = []

	for i in range(festival_length):

		if festival_list[i] == None:

			print("empty")

		else :
			festivalObject = {

			"festival" : festival_list[i],
			"ref" : festival_ref[i]

			}

			masterArr.append(festivalObject)
		#festivalArr.append(festivalObject)

	#print(festivalArr)

	#masterArr.append(festivalArr)



with open('festref.json', 'w') as outfile:
	json.dump(masterArr, outfile, indent = 4)

