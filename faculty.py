from bs4 import BeautifulSoup
import requests

# scrape all institute/program site adresses
def scrape(col):
	# find all list elements
	col_li = col.find_all('li')

	col_li_str = []

	# cast to string
	for i in col_li:
		col_li_str.append(i.__str__())

	str = []

	# discard bold texts. theese are faculty sites
	for i in col_li_str:
		if(i.find('<strong>') == -1):
			str.append(i)

	links = []

	# find the adresses of starting and ending quotes
	for i in str:
		start = i.find('"')+1
		end = i.rfind('"')
		
		# discard the quotes
		links.append(i[start:end])

	final_links = []

	for i in links:
		# i think i can delete this line but i am not sure so i won't touch this
		if(i.startswith("http://ute")):
			continue

		# if adresses start with http, they are correct adresses
		elif(i.startswith("http")):
			final_links.append(i)
		# if they don't start with htpp, turn them to correct address from
		else:
			final_links.append(r'https://www.gtu.edu.tr/' + i)

	return final_links

def get_sites():

	# adress to programs page of gtu site
	site = requests.get("https://www.gtu.edu.tr/kategori/4/3/display.aspx")
	html = site.text
	soup = BeautifulSoup(html, "html.parser")

	# find the columns where list of programs are
	columns = soup.find_all('div', {'class': 'two-column'})

	result = []

	# call the scrape function
	for column in columns:
		for i in scrape(column):
			result.append(i)

	# Theese adresses are problematic so I discarded them
	result.remove("https://www.gtu.edu.tr/kategori/2201/3/display.aspx?languageId=1")
	result.remove("https://www.gtu.edu.tr/kategori/46/3/display.aspx?languageId=1")
	result.remove("https://ute.gtu.edu.tr/")
	# bte.gtu.edu.tr redirects to this adress so I replaced them
	result.remove("http://bte.gtu.edu.tr")
	result.append("https://www.gtu.edu.tr/kategori/2208/3/display.aspx")

	return result