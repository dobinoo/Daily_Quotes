from termcolor import colored   #add colored output here
import time #to use sleep function for delay
import urllib2 #for handling content from website
#import re #imported re but later decided to use built in funcions
#for using system functions
#import sys #later removed

#ifdef unfinished = True , then program is not fully finished and he might not be runnable or not propertly
#ifdef runnable = False , program cannot even run , because of missing part of code, some files etc..
unfinished = False
runnable = True

#Exit function :)
def bye():
    print ("\n\nExiting . . .")
    time.sleep(3)

    print colored("Use this wisely young Padawan", "yellow", attrs=['bold', 'dark'])

    exit(0)
    return None

#checking function
def check():
    if(unfinished):
        print colored("\nWarning!\nThis program is not fully finished, It might not WORK propertly!\n","yellow")

        if(not runnable):
            print colored("Error!\nThis program is not in runnable state\n","red")
            bye()       # calling exiting function

##########################################
#main part of code

#calling checking function
check()

##############
#manipulating with website
url = "https://www.brainyquote.com/topics/daily"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(url, headers=hdr)
try:
    response = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()
html = response.read()
start = html.find('&quot;') + 6
next = html.find('&quot;',start)
end = html.find('">',next + 6)
quote = html[start:next]
author = html[next + 6:end]
#manipulating with website
#######################

########
#printing part
print "\nTHE QUOTE OF THE DAY:\n"
time.sleep(2)
print colored(quote,"blue", attrs=['bold'])
time.sleep(2)
print colored(author,"red", attrs=['bold'])
#print html
#printing part
###########
time.sleep(1)
bye()

#end of main part of code
##########################################
