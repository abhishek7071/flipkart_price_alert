from bs4 import BeautifulSoup
import requests, time, smtplib
#from notify_run import Notify
from datetime import datetime
import re
import requests as r
from bs4 import BeautifulSoup as bs
searchquery = input("Enter the search query")
search_query = searchquery.replace(' ', '+') 
link="https://www.1mg.com/search/all?filter=true&name="+str(search_query)
#link ="https://www.1mg.com/search/all?filter=true&name=Combiflam"
html_page = r.get(link)
soup = BeautifulSoup(html_page.content,"lxml")

for i in soup.find_all('div',{'class':['style__horizontal-card___1Zwmt','style__product-box___3oEU6']}):
	link = i.find('a',href=True)
	if link is None:
	     continue
	link1 = link['href']
	#print(link['href'])
	print(link1)
	break
	
url1= "https://www.1mg.com"  +str(link1)
print(url1)
page1 = r.get(url1)
soup = bs(page1.content, "html.parser")
price=soup.find("span" , {"class": "l3Regular"}).text
price = price[1:]
print(price)

for j in soup.find_all('div',{'class':'FactBox__rowContent__2YA1r FactBox__flexCenter__j9P_K col-3'}):
	Manu= j.find('a',href=True)
	if Manu is None:
	     continue
	Manu1 = Manu.text
	#print(link['href'])
	print(Manu1)
	break
 #   if Manu is str
     #   continue
   #  Manu2 = 
#Manu=soup.find("div",{"class":"j9P_K col-3"}).text
#print(Man
#practo
link="https://www.practo.com/medicine-info/search?drug=Diclowin"                                          #link ="https://www.1mg.com/search/all?filter=true&name=Combiflam"                                        
html_page = r.get(link)                              
soup = BeautifulSoup(html_page.content,'html.parser')
#print(soup.prettify())
for i in soup.find_all("div" , {"class":"shdzcg-1 cjDIVa"}):
	link = i.find('a',href=True)
	if link is None:
		continue
	link1 = link['href']
	print(link['href'])
	print(link1)
	break
