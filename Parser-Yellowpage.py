import urllib.request
from bs4 import BeautifulSoup
import re,csv


'''
link1= 'http://www.yellowpages.com.au/search/listings?clue=security&locationClue=Western+Australia&pageNumber='
link2='&referredBy=www.yellowpages.com.au'
'''
link1='https://www.yellowpages.com.au/search/listings?clue=security&locationClue=Western+Australia&pageNumber='
link2='&referredBy=UNKNOWN&eventType=pagination'
page=1
index=1
output=[]
def filter_list():
    global index
    global output      # store all info

    for div in divs:
        items = BeautifulSoup(str(div),features = "lxml")
        try:
            company = items.find('a',class_="listing-name").getText().replace(',','')

        except:
            company='None Name'


        try:
            address = items.find('p',class_="listing-address mappable-address mappable-address-with-poi").getText()
            address=address.replace(',','')
        except:
            address='None Add'

        try:

            tel = items.find('a',class_='click-to-call contact contact-preferred contact-phone').getText()
            #print(tel)

        except Exception as e:

            tel = 'None Tel'

        try:
            email=items.find('a',class_='contact contact-main contact-email')['data-email']


        except Exception as e:
            email="None Email"

        print('#',index,'--',company,'--',tel.strip(),'--',email,'--',address)
        output.append([index,company,tel.strip(),email,address])
        index=index+1






while page:
    url =link1+ str(page)+link2
    header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
    req = urllib.request.Request(url,headers=header)
    f = urllib.request.urlopen(req)
    content = f.read().decode('utf-8')
    #print(content)

    soup = BeautifulSoup(str(content),features = "lxml")
    #print('size:',len(soup))
    #print(soup)
    divs = soup.select('div.cell.in-area-cell.find-show-more-trial.middle-cell')
    pages = str(soup.select('div.button-pagination-container.responsive')[0])
    soup1=BeautifulSoup(pages,features="lxml")


    if('Next' in soup1.getText()):
        print('this is number',page)

        filter_list()
        page+=1
    else:
        print('this is number',page)

        filter_list()
        page=0



print('----------------------')
#print(len(divs))
print(soup.find('span',class_='emphasise').getText())



#timestr = time.strftime("%Y%m%d-%H%M%S")

with open('output.csv', 'w',newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    for i in output:
        writer.writerow(i)
    print('write finished')
