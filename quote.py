afrom termcolor import colored   #add colored output here
import time #to use sleep function for delay
import urllib2 #for handling content from website
#for using system functions
#import sys #later removed

#ifdef unfinished = True , then program is not fully finished and he might not be runnable or not propertly
#ifdef runnable = False , program cannot even run , because of missing part of code, some files etc..
unfinished = True
runnable = True

#Exit function :)
def bye():
    print ("\nExiting . . .")
    time.sleep(3)

    print colored("\n\nUse this wisely young Padawan", "yellow", attrs=['bold', 'dark'])

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

check()

url = "https://www.brainyquote.com/topics/daily"
req = urllib2.Request(url)
response = urllib2.urlopen(req)
html = response.read()
print (html[0:300])

#end of main part of code
##########################################
