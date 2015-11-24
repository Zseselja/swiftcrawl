import sys
import re
import urllib2

# need to build lexers.

sentiments = []

rules = [
    # ('bold', re.compile(r'\*\*')),
    # ('link', re.compile(r'\[\[(.*?)\]\]')),
]



def send_to_mothership():


 #mothership gives crawler mission
def get_mission():
    pass

def do_mission():
    pass

def send_report(id):
    pass

def main(arg , argv):
    alive = 1
    id = argv[1]


    while alive:
        get_mission()

        try:
            do_mission()




        except urllib2.HTTPError, err:
		if err.code == 404:
			print "\n\nError 404: Phases not found!"
		elif err.code == 403:
			print "\n\nError 403: Wrong command!"
		else:
			print "\n\nHouston we have a problem! Error code ", err.code


        send_report(id)











if __name__ == '__main__':
    main(sys.argv[1:])