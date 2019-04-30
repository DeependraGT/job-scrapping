
import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup
for i in range(1, 10):
	page = requests.get("https://www.indeed.co.in/jobs?q=software+developer&l=Delhi")
	soup = BeautifulSoup(page.content, 'html.parser')
	data = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
	with open("output1.txt", "w") as file:
		file.write(str(data))
	item = data[0] 
	alldata = []   
	jobtitle = []      																	
	org =[]
	exp = []
	loc = []
	skill = []
	salary = []
	date = []
	store = []

	for item in data:
		try:
			jobtitle = item.find(class_="jobtitle").get_text()
			str(jobtitle + ",")
			org = item.find(class_="company").get_text()	
			str(org + ",")
			loc = item.find(class_="location").get_text()
			str(loc + ",")
		except:
			pass
		
			
		
        for alldata in  range (1):
        	with open('job-data.csv', 'a') as csv_file:
	    		writer = csv.writer(csv_file)
	    		writer.writerow([jobtitle, org,exp,loc,skill,salary,date, datetime.now()])

		# outputFile = open('naukariD.csv', 'w')          
		# outputWriter = csv.writer(outputFile)
		# outputWriter.writerow([desig, org,exp,loc,skill,salary,date, datetime.now()])

		

 
