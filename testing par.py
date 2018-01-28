import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from  tkinter import filedialog
import csv

#User selects file to parse
def loadwo():
  path = Tk()
  path.filename =  filedialog.askopenfilename(initialdir = "Path Where the dialog should open first",title = 
  "Title of the dialog",filetypes = (("xml files","*.xml"),("all files","*.*")))
  print (path.filename)
  path.withdraw()   

loadwo()
tree = ET.parse ('')#this is where the file location to be parsed goes
root = tree.getroot()  



#Open csv file
Resident_data = open('C:/Users/jtdev/Desktop/ResidentData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Resident_data)
resident_head = []

count = 0
for member in root.findall('Resident'):
	resident = []
	address_list = []
	if count == 0:
		name = member.find('Name').tag
		resident_head.append(name)
		PhoneNumber = member.find('PhoneNumber').tag
		resident_head.append(PhoneNumber)
		EmailAddress = member.find('EmailAddress').tag
		resident_head.append(EmailAddress)
		Address = member[3].tag
		resident_head.append(Address)
		csvwriter.writerow(resident_head)
		count = count + 1

	name = member.find('Name').text
	resident.append(name)
	PhoneNumber = member.find('PhoneNumber').text
	resident.append(PhoneNumber)
	EmailAddress = member.find('EmailAddress').text
	resident.append(EmailAddress)
	Address = member[3][0].text
	address_list.append(Address)
	City = member[3][1].text
	address_list.append(City)
	StateCode = member[3][2].text
	address_list.append(StateCode)
	PostalCode = member[3][3].text
	address_list.append(PostalCode)
	resident.append(address_list)
	csvwriter.writerow(resident)
Resident_data.close()
