import random
from lxml import html
import requests

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]
random_response = random.choice(responses)

# store the html content of the common acronymns used at CERN
cern_page = requests.get("http://library.cern/archives/accronymes?fbclid=IwAR3p33pijvUw0iaHiLdgul789O_jqlc8dStINZRyCu4rkrFBjvR7_NDo6P4")
lhc_page = requests.get("http://maalpu.org/lhc/LHC.abbrs.htm")
tree = html.fromstring(cern_page.content + lhc_page.content)

# get all the abbreviations & store them in dictionary
elements = tree.xpath('//td/text()')
acronymns = {}
for e in range(0, len(elements), 2):
    acronymns[elements[e]] = elements[e+1]

keys = list(acronymns.keys())

while True:
	userInput = input(">>> ")
	if userInput.upper() in keys:
		print(acronymns[userInput.upper()])
