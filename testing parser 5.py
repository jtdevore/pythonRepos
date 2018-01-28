import xml.etree.ElementTree as ET
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from  tkinter import filedialog
from tkinter import simpledialog
import csv



        

#Open csv file
#need to find a way to create this file and make name match wo number as input by user
#need to create a folder on desktop where all these files go but not overwrite existing folder/files

class gui:
        def selectEvent():  #User selects file to parse
                path = Tk()
                path.filename =  filedialog.askopenfilename(initialdir = "Path Where the dialog should open first",title = "Select Event File",filetypes = (("xml files","*.xml"),("all files","*.*")))
                print (path.filename)
                path.withdraw()
                global root
                tree = ET.parse(path.filename)#this is where the file location to be parsed goes
                root = tree.getroot()
        
        def callWO(): #This opens an input text gui for user to input wo number and converts it to the variable woNumber for later use.
                root = Tk()
                root.withdraw()
                woNumber = tkinter.simpledialog.askstring("Enter WO #", "Enter WO Number")
                print (woNumber)

        #this is a gui for user to select which template to use and variable selected will be used to open an existing excel template that will be included in program folder.
        def woTemplate():
                
                master = Tk()

                variable = StringVar(master)
                variable.set("Select the main fault for billable event") # default value

                w = OptionMenu(master, variable, "Out of fuel", "Dead battery from misuse", "E-stop", "Frozen", "Damage", "E-brake unplugged", "OI unplugged")
                w.pack()

                def ok():
                    print ('Billable event due to ' +  variable.get()) #gui.
                    master.withdraw()

                button = Button(master, text="OK", command=ok)
                button.pack()
                master.mainloop()
                

        
                
gui.selectEvent()                
gui.callWO()
gui.woTemplate()


#make a gui for selecting the excel template to use and make this the variable for it
cbForm = open('C:/Users/jtdev/Desktop/ResidentData.csv', 'w') #need to make file location more universally available and easy to find

# create the csv writer object

csvwriter = csv.writer(cbForm)
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
cbForm.close()





