import base64
import sys
import urllib2
import json

from bs4 import BeautifulSoup

# need to build lexers.

sentimentURL = urllib2.Request("http://127.0.0.1:8000/data/sentiments/")
crawlerURL = urllib2.Request("http://127.0.0.1:8000/data/crawlers/")
#userAndPass = b64encode(b"crawler:swift").decode("ascii")
#headers = { 'Authorization' : 'Basic %s' %  userAndPass }

rules = [
    # ('bold', re.compile(r'\*\*')),
    # ('link', re.compile(r'\[\[(.*?)\]\]')),
]



#mothership gives crawler mission
def get_regex():
   # base64string = base64.encodestring('%s:%s' % ("sentiment", "swift")).replace('\n', '')
    #sentimentURL.add_header("Authorization", "Basic %s" % base64string)
    results = urllib2.urlopen(sentimentURL)
    data =  results.read()
    return data
    pass

#get CrawlerMission
def get_mission():
    base64string = base64.encodestring('%s:%s' % ("crawler", "swift")).replace('\n', '')
    crawlerURL.add_header("Authorization", "Basic %s" % base64string)
    results = urllib2.urlopen(crawlerURL)
    data =  results.read()
    return data
    pass

#open the URL
def open_page(url):
    # open URL
    page = urllib2.urlopen(url)
    return page

#Sends results to the MotherShip
def send_report(results):

   pass

#scan the page for the sentiments/Regex.
def do_mission(regex , soup):
    results = []

    try:
        for x in regex:
            results.append(soup.find_all(x))
        return json.dumps(results)
    except:
        return False


    pass



# The input needs a destination
def main(arg , urls):
    data = get_mission()
    #alive = True
    while urls != None:
        regex = get_regex()
        #urls = get_mission()
        for x in urls:
           file =  open_page(x)
           soupMix =  file.read()
           soup = BeautifulSoup(soupMix , 'html.parser')
           try:
               results = do_mission(regex , soup)
               if(False!= results ):
                   alive = False
                   urls = None
                   send_report(results)
                   #        return results
                   # get another mission from the mothership
                   # if nothing kill it.
               else:
                   alive = False
           except urllib2.HTTPError, err:
                if err.code == 404:
                    print "\n\nError 404: Phases not found!"
                elif err.code == 403:
                    print "\n\nError 403: Wrong command!"
                else:
                    print "\n\nHouston we have a problem! Error code ", err.code


            # send_report(id)











if __name__ == '__main__':
    main(sys.argv[0] , sys.argv[1:])