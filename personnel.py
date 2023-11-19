from bs4 import BeautifulSoup
import requests
import faculty

def get_personnel_page():

	personnel_page = []

	# loop through all program/institute sites	
	for url in faculty.get_sites():
		site = requests.get(url)
		html = site.text
		soup = BeautifulSoup(html, "html.parser")

		# find list elements
		text = soup.find_all('ul')
		
		# cast to string
		str = text.__str__()

		strs = ""

		# Akademik kadro page is written 3 different ways throughout the website so match all of them
		# After matching it split the html string into 2 parts
		# We only care about the first part where akademik kadro page url lies
		if(str.find("Akademik Kadro") != -1):
			strs = str.split("Akademik Kadro")[0].rstrip()
		elif(str.find("Akademik kadro") != -1):
			strs = str.split("Akademik kadro")[0].rstrip()
		else:
			strs = str.split("AKADEMİK KADRO")[0].rstrip()


		# After splitting, first part will ends with ">
		# We need to discard these characters
		strs = strs[:-2]

		# After discarding the unnecessary characters we need to find the start of the url
		# Start looking from end of the string and find the index of last quote in string
		# This last quote will be the start of the url we need
		# After finding this index, we can get the string after it
		index = strs.rfind('"')
		link = strs[index+1:]

		personnel_page.append(link)

	return personnel_page
	