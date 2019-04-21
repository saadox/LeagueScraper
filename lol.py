import re
import  urllib.request
from bs4 import BeautifulSoup
import os
import time
import sys

####### LOLSKILL BASED ########
##   MADE BY 0x544D          ##
##     fb : saadox.amrani    ##
###############################

clear   = lambda : os.system('cls')

#autoret bytes
def getBytes(strng):
    return bytes(strng+'\n','utf-8')


#To Make sure the files exists
of = open("links.txt",'w+')
of.close()
#Closed and checked !

#Opening the File for appending it
af = open("links.txt",'ab')

staticLink = 'http://www.lolskill.net/top/skillscore/page-'
test  = 1
for page in range(1,1017):
    fullLink = staticLink+str(page)
    req = urllib.request.Request(fullLink, headers={'User-Agent': 'Mozilla/5.0'})
    html =  urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html)
    clear()
    print('PAGE ['+str(page)+']\n')
    for a in soup.find_all("a"):
        if('summoner/' in a['href']):
            #print(a['href'])
            un      = str(a['href']).replace('summoner/','')
            ind     = un.index('/')
            server  = un[0:ind]
            un      = un[ind+1:len(un)]
            res     = urllib.parse.unquote(un) + ':'+server
            print(str(test)+"  ->  "+res)
            af.write(getBytes(res))
            test    += 1
    #input("")

af.close()
clear()
print("-> ["+str(test)+"] Total Summoner Generated !")
#catFile()
