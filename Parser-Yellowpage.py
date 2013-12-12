import urllib.request
from bs4 import BeautifulSoup
import re
   
page=1 

'''
link1= 'http://www.yellowpages.com.au/search/listings?clue=security&locationClue=Western+Australia&pageNumber='    
link2='&referredBy=www.yellowpages.com.au'
'''
link1='http://www.yellowpages.com.au/search/listings?clue=ALARM&eventType=pagination&locationClue=Western+Australia&pageNumber='
link2='&referredBy=www.yellowpages.com.au'


   
def filter_list(link):
  
    f = urllib.request.urlopen(link)
    content = f.read().decode('utf-8')
    soup = BeautifulSoup(content)

    divs = soup.findAll('div',{"class":"cell in-area-cell middle-cell"})

    div = soup.find('div',{"class":"cell in-area-cell middle-cell"})

    for div in divs:
        items = BeautifulSoup(str(div))  

        try:    
            company = items.find('a',{"class":"listing-name"}).getText().replace(',','')
        except:
            company='None Name'
        try:
            address = items.find('p',{"class":"listing-address mappable-address"}).getText()
            address=address.replace(',','')
        except:
            address='None Add'
        
        try:
            tel = items.findAll('a',{"title":"Phone"})
            tel =re.findall(r'\d+',str(tel))
            tel=tel[-3]+tel[-2]+tel[-1]
        
        except Exception as e:

            tel = 'None Tel'
        try:
            email=items.find('a',{"class":"contact contact-main contact-email "})['data-email']
        
        except Exception as e:
            email="None Email"
            
        data=company+','+str(tel)+','+email+','+address
    
        with open('/Documents and Settings/DSP Front Desk/Desktop/securitylist.txt','a') as f:
            f.write(data+'\n')
            print(data)
     
        
while page<17:
    url =link1+ str(page)+link2
    filter_list(url)
    page+=1
    print('this is number',page)

      
   
