import sys
import re
import urllib2
from bs4 import BeautifulSoup
import httplib


# need to build lexers.

sentiments = []

rules = [
    # ('bold', re.compile(r'\*\*')),
    # ('link', re.compile(r'\[\[(.*?)\]\]')),
]



def send_to_mothership():
    pass


#mothership gives crawler mission
def get_regex():
    # Regex
    return "a"
    pass

def get_mission():
    # URLS
    return "a"
    pass

def open_page(url):
    # open URL
    page = urllib2.urlopen(url)
    return page

def send_report(results):
    pass

def do_mission(regex , soup):
    results = []

    try:
        for x in regex:
            results.append(soup.find_all(x))


        return results
    except:
        return False
    pass



# The input needs a destination
def main(arg , urls):

    alive = True
    while alive or urls != None:
        regex = get_regex()
        # urls = get_mission()
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