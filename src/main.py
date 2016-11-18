import base64
import sys
import urllib2 , urllib
import json
import requests
from bs4 import BeautifulSoup


class pages(object):
    def __init__(self):
        self.list = []
        pass
    def add(self, page):
        self.list.append(page)


# class sentiment(object):
#     def __init__(self):
#         pass
#     def store(self, data):
#         self.data = data


# need to build lexers.
sentimentURL = "http://127.0.0.1:8000/data/sentiments/"

# sentimentURL = urllib2.Request("http://127.0.0.1:8000/data/sentiments/1")
crawlerURL = "http://127.0.0.1:8000/data/crawlers/"
# crawlerURL = urllib2.Request("http://127.0.0.1:8000/data/crawlers/")
# userAndPass = base64.encode(b"crawler:swift").decode("ascii")
# #headers = { 'Authorization' : 'Basic %s' %  userAndPass }

rules = [
    # ('bold', re.compile(r'\*\*')),
    # ('link', re.compile(r'\[\[(.*?)\]\]')),
]



#mothership gives crawler mission
# aka crawler gets some sentiment to look for.
def get_sentiment_regex():
    results = requests.get(sentimentURL)
    return results


#get CrawlerMission
def get_crawler_mission():
    results = requests.get(crawlerURL)
    return results


#open the URL
def open_page(url):
    # open URL
    page = urllib2.urlopen(url)
    return page

# #Sends results to the MotherShip
# def send_report(results):
#    #  for now print to file
#     data = urllib.urlencode(results)
#     req = urllib2.Request(sentimentURL, data)
#     response = urllib2.urlopen(req)
#     the_page = response.read()
#     print the_page

#
# # make format for sentiments
#          "id": 1,
#         "text": "This is good!",
#         "num_positive": 2,
#         "num_negative": 1,
#         "num_neutral": 0


#scan the page for the sentiments/Regex.
def do_mission(regexList , soup):
    results = []
    # what we are looking for
    keys = []
    for regex in regexList:
        keys.append(regex['text'])
        pass
    print(keys)


    try:
        for x in keys:
            results.append(soup.find_all(x))
        return json.dumps(results)
    except:
        return False


    pass

def makeSoup(url):
    try:
        print(url)
        file =  open_page(url)
        soupMix =  file.read()
        soup = BeautifulSoup(soupMix , 'html.parser')
        return soup
    except:
        print("...couldn't open page...")



def findNext(soup):
    a = soup.find_all("a")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    for x in a:
        print(x.get('href'))
    # print(pages)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# Input
#  arg 1 should be a command
#  arg 2 should be a destination to look at.

# The input needs a destination

# Test scrape Code
      # if arg == 'get':
    #     for y in urls:
    #         soup = makeSoup(y)
    #     print(soup)
    #     findNext(soup)
    #     return 1
	#
def response2list(response):
    data =  response.json()
    jsonObj = json.dumps(data)
    ret = json.loads(jsonObj)
    return ret


def main():
    # Stat crawling from here
    crawlers = get_crawler_mission()
    dict = response2list(crawlers)

    # create a pages object
    viewedPages = pages()

    # while there are urls
    while len(dict) != len(viewedPages.list):
        # get regex from sentiments to figure out what to look for
        regex = get_sentiment_regex()
        regexlist = response2list(regex)

        for current in dict:
            currentPage = current['Target']
            #  Check to see if site is in viewedPages
            if currentPage in viewedPages.list:
                continue
            else:
                # add our page to viewed pages
                viewedPages.add(currentPage)

            try:
               soup = makeSoup(currentPage)
               results = do_mission(regexlist , soup)
               print results

               if(False!= results ):
                   # Need to immplement sending back info aka POST

                   urls = None
                   # send_report(results)
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
                    print "\n\nHouston we have a problem! Error code ", err.cod

if __name__ == '__main__':
   ret = main()