import requests
from bs4 import BeautifulSoup


try:
    url = "https://www.tryhackme.com" #Any url You want to Craw
    r=requests.get(url)
    r.raise_for_status() #Throw an Error message incase of invalid url 
    htmlContent=r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    title=soup.title #Get the title of HTML page
    print("​🆃🅸🆃🅻🅴 🅾🅵 🆃🅷🅴 🅿🅰🅶🅴​")
    print("\t")
    print(title) #Get the Title 
    print("\t")
    print("🅰🅻🅻 🆃🅷🅴 🅿🅰🆁🅰🅶🆁🅰🅿🅷🆂")
    print("\t")
    paras=soup.find_all('p')  #Get all the Paragraphs
    print(paras)
    print("\t")
    print("🅵🅸🆁🆂🆃 🅴🅻🅴🅼🅴🅽🆃 🅸🅽 🅷🆃🅼🅻 🅿🅰🅶🅴")
    print("\t")
    print(soup.find('p')) #Get the first Element in the html page
    print("\t")
    print("🅰🅻🅻 🆃🅷🅴 🆃🅴🆇🆃🆂 🅵🆁🅾🅼 🆃🅷🅴 🅿🅰🆁🅰🅶🆁🅰🅿🅷 🆃🅰🅶🆂 🅸🅽 🆃🅷🅴 🅷🆃🅼🅻 🆄🆁🅻")
    print("\t")
    print(soup.get_text()) #Get All the Texts from The paragraph tags
    print("\t")
    print("🅰🅻🅻 🆃🅷🅴 🅰🅽🅲🅷🅾🆁🆂 🆃🅰🅶🆂")
    print("\t")
    anchors=soup.find_all('a') #Get all the Anchor tags
    print(anchors)
    print("\t")
    print("🅰🅻🅻 🆃🅷🅴 🅻🅸🅽🅺🆂 🅾🅵 🅰🅽🅲🅷🅾🆁 🆃🅰🅶🆂")
    print("\t")
    all_links= set()
    for link in anchors:   #Get all the links from Anchor tags 
       if(link.get('href') != '#'): #Print only the clean links
          linkText=url +link.get('href') 
          all_links.add(link)
          print(linkText)           
    print("\t")
    print("🅲🅾🅼🅿🅻🅴🆃🅴 🅷🆃🅼🅻 🅲🅾🅽🆃🅴🅽🆃 🅵🆁🅾🅼 🆃🅷🅴 🆄🆁🅻 🅴🅽🆃🅴🆁🅴🅳")
    #print(htmlContent)
    print("\t")
    print("🅿🆁🅴🆃🆃🅸🅵🆈 🅵🅾🆁🅼 🅾🅵 🆃🅷🅴 🅷🆃🅼🅻 🅲🅾🅽🆃🅴🅽🆃")
    #print(soup.prettify)
except Exception as e:
  print(e)
