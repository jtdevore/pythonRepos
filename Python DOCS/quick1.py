#! python3
#this program is a practice projec
#program needs to take 
import re

beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.findall('Hello world!')
print (mo)