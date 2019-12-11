import urllib.request
from bs4 import BeautifulSoup
import re

page=1

'''
link1= 'http://www.yellowpages.com.au/search/listings?clue=security&locationClue=Western+Australia&pageNumber='
link2='&referredBy=www.yellowpages.com.au'
'''
link1='https://www.yellowpages.com.au/search/listings?clue=security&locationClue=Western+Australia&pageNumber='
link2='&referredBy=UNKNOWN&eventType=pagination'


def filter_list(link):

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

        print(company,'--',tel.strip(),'--',email,'--',address)



#filter_list('https://www.yellowpages.com.au/search/listings?clue=security&locationClue=Western+Australia&pageNumber=2&referredBy=UNKNOWN&eventType=pagination')



while page<23:
    url =link1+ str(page)+link2
    header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
    req = urllib.request.Request(url,headers=header)
    f = urllib.request.urlopen(req)
    content = f.read().decode('utf-8')
    #print(content)

    soup = BeautifulSoup(content,features = "lxml")
    #print('size:',len(soup))
    #print(soup)
    divs = soup.select('div.cell.in-area-cell.find-show-more-trial.middle-cell')


    filter_list(url)
    page+=1
    print('this is number',page)


print('----------------------')
#print(len(divs))
print(soup.find('span',class_='emphasise').getText())



'''
# items example:
<html>
 <body>
  <div class="cell in-area-cell find-show-more-trial middle-cell">
   <div class="listing listing-search listing-data" data-about-id="e9dac15a-86f2-4455-8304-60af2c935a8f" data-advertiser-id="480398834" data-business-name="Vidguard_Security_Systems" data-content-group-id="e2092df6-5eec-4149-b2bc-2f768e7f1d05" data-content-score="10" data-context="businessTypeSearch" data-full-name="Vidguard Security Systems" data-heading-code="12610" data-heading-name="Security Systems" data-intent="businessTypeSearch" data-is-free="true" data-is-top-of-list="false" data-listing-id="13846088" data-listing-name="vidguard-security-systems" data-omniture-average-rating="0.0" data-product-code="YPD00" data-product-id="999015139722" data-product-version="17" data-referred-by="UNKNOWN" data-result-type="O" data-score="1072.0" data-state="suppressed" data-suburb="suppressed" data-total-reviews="0" data-url="/sup/vidguard-security-systems-13846088-listing.html?context=businessTypeSearch">
    <div class="search-contact-card call-to-actions-4 feedback-feature-on">
     <div class="search-contact-card-table-div cag-groups-2 cag-items-4">
      <table>
       <tr class="search-contact-card-row">
        <td class="search-contact-card-top">
         <div class="listing-details clickable-listing">
          <div class="flow-layout outside-gap-large inside-gap inside-gap-medium vertical">
           <div class="cell first-cell last-cell">
            <div class="flow-layout inside-gap inside-gap-medium vertical">
             <div class="cell first-cell">
              <div class="media-object clearfix inside-gap-medium image-on-right listing-summary">
               <div class="body left right">
                <a class="listing-name" href="/sup/vidguard-security-systems-13846088-listing.html?context=businessTypeSearch" title="View more about this business">
                 Vidguard Security Systems
                </a>
                <p class="listing-heading">
                 <a data-index-link="true" href="/find/security-systems/geraldton-wa-6530">
                  Security Systems - Geraldton, WA 6530
                 </a>
                </p>
               </div>
              </div>
             </div>
             <div class="cell middle-cell">
              <div class="opening-hours-empty bold">
               No Opening Hours Provided
              </div>
             </div>
             <div class="cell middle-cell">
              <div class="listing-review-summary">
               <div class="no-rating-spacer">
               </div>
              </div>
             </div>
             <div class="cell last-cell">
              <div class="contact-legal-id contact-legal-id-search">
               Legal ID: Commercial alarm systems
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </td>
        <td class="sizing" rowspan="2">
         <div class="fixed">
         </div>
         <div class="variable">
         </div>
        </td>
       </tr>
       <tr class="search-contact-card-row">
        <td class="search-contact-card-bottom">
         <div class="viewable">
         </div>
        </td>
       </tr>
      </table>
      <div class="real-actions cag-groups-2 cag-items-4">
       <div class="call-to-action-group">
        <div class="call-to-action first">
         <a class="click-to-call contact contact-preferred contact-phone" data-overtok-enabled="false" href="tel:0899641810" rel="nofollow" title="Phone">
          <span class="glyph icon-phone border border-dark-blue with-text">
          </span>
          <span class="contact-text">
           (08) 9964 1810
          </span>
         </a>
        </div>
        <div class="call-to-action first">
         <a class="contact contact-main contact-email" data-email="sales@vidguard.com.au" data-overtok-enabled="false" href="mailto:sales%40vidguard.com.au?subject=Enquiry%2C%20sent%20from%20yellowpages.com.au&amp;body=%0A%0A%0A%0A%0A------------------------------------------%0AEnquiry%20via%20yellowpages.com.au%0Ahttps%3A%2F%2Fwww.yellowpages.com.au%2Fsup%2Fvidguard-security-systems-13846088-listing.html%3Fcontext%3DbusinessTypeSearch" rel="nofollow" title="Send Email sales@vidguard.com.au">
          <span class="glyph icon-email border border-dark-blue with-text">
          </span>
          <span class="contact-text">
           Send Email
          </span>
         </a>
        </div>
       </div>
       <div class="call-to-action-group">
        <div class="call-to-action">
         <a class="contact contact-main contact-url" data-overtok-enabled="false" href="http://www.mbcom.com.au" rel="nofollow" target="_blank" title="http://www.vidguard.com.au (opens in a new window)">
          <span class="glyph icon-website border border-dark-blue with-text">
          </span>
          <span class="contact-text">
           Website
          </span>
         </a>
        </div>
        <div class="call-to-action">
         <a class="contact send-to-mobile" href="/renderSendToMobile?listingId=13846088&amp;productId=999015139722&amp;productVersion=17&amp;context=businessTypeSearch&amp;referredBy=UNKNOWN" rel="nofollow">
          <span class="glyph icon-mobile border border-dark-blue with-text">
          </span>
          <span class="short-send-to-text">
           Send to
          </span>
          <span class="long-send-to-text">
           Send to mobile
          </span>
         </a>
        </div>
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
 </body>
</html>
'''
