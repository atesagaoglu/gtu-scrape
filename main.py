from bs4 import BeautifulSoup
import requests
import personnel


def get_mails():

	# Look through all akademik kadro pages
	for url in personnel.get_personnel_page():
		
		site = requests.get(url)
		html = site.text
		soup = BeautifulSoup(html, "html.parser")

		# Find the div where lecturers personal info sits
		details = soup.find_all('div', {'class': 'details'})

		text = []

		# Email part we need is under the second div after details part
		# So find that div and get the text inside
		# This text is the lecturers email adress before the @gtu.edu.tr part
		for detail in details:
			text.append(detail.findNext("div").findNextSibling("div").get_text().__str__())


		for i in text:
			# 15th index corresponds to the start of the email address
			# end is the character before gtu.edu.tr part
			start = 15
			end = i.find("gtu.edu.tr")
			str = i[start:end]

			# finally print the email adress and append it to the file
			print(str)
			f = open("mails.txt","a")
			f.write(str+'\n')
			f.close()

# call the function
get_mails()