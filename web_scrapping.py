from bs4 import BeautifulSoup
import requests

file= open("text_data.txt","w")

#A random url from the medium article to display the use of BeautifulSoup
url='https://amtoyumtimmy.medium.com/no-mr-peterson-the-monarchy-is-not-brilliant-f181efa5494e'
page= requests.get(url)


#parsing the html page's content to a vaiable soup
soup= BeautifulSoup(page.content,'html.parser')


#To get all the text from the web page
a= soup.get_text()
#print("This is just all texts\n",


#to fetch the first paragraph from the web
#fp=soup.find('p')

#TO feteh all the paras from the web 
#ap= soup.find_all('p')


file.write(a)
file.write(b)
file.flush()
file.close