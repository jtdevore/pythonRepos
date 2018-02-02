import xml.etree.ElementTree as ET
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from  tkinter import filedialog
from tkinter import simpledialog
import openpyxl
import win32com.client as win32
import time

#TODO need to find a way to create this file and make name match wo number as input by user
#TODO make customerCell and locationCell and nameCell, signatureCell not have to be entered every time.  Some way for it to hold the data unless changed by user.


#User selects file to parse
master = Tk()
master.filename =  filedialog.askopenfilename(initialdir = "Path Where the dialog should open first",title = "Select Event File",filetypes = (("xml files","*.xml"),("all files","*.*")))
print (master.filename)


global root
tree = ET.parse(master.filename)#this is where the file location to be parsed goes
root = tree.getroot()
        
#This opens an input text gui for user to input wo number and converts it to the variable woCell for later use.
      

woCell = tkinter.simpledialog.askstring("Enter WO #", "Enter WO Number")
print (woCell)

#this is a gui for user to select which template to use and variable selected will be used to open an existing excel template that will be included in program folder.
                  
variable = StringVar(master)
variable.set("Select the main fault for billable event") # default value
w = OptionMenu(master, variable, "Out of fuel", "Dead battery from misuse", "E-stop", "Frozen", "Damage", "E-brake unplugged", "OI unplugged", "Other")
w.pack()

def ok():
    print ('Billable event due to ' +  variable.get()) #gui button.
    master.destroy()

button = Button(master, text="OK", command=ok)
button.pack()
master.wait_window(button)

#Stores user input variable truckCell for later use
master = Tk()
truckCell = tkinter.simpledialog.askstring("Enter Truck  Number", "Enter Truck number")
print (truckCell)

#Stores user input variable repairSdate for later use
        

repairSdate = tkinter.simpledialog.askstring("Enter Repair Start Time", "Enter Repair Start Time\nFormat hh:mm")
print (repairSdate)

repairCdate = tkinter.simpledialog.askstring("Enter Repair completed Time", "Enter Repair completed Time\nFormat hh:mm")
print (repairCdate)

laborCell = tkinter.simpledialog.askstring("Enter labor hours", "Enter labor hours")
print (laborCell)

dateCell = time.strftime("%d/%m/%Y")
occuredCell = None #TODO autofill from xml data, must check against alarm template to specificy what time to select from the xmlfile.  
#IE.  OOF occured at 1500 , program checks for the string 'out of fuel' in xml data and enters that time as variable
partCost = None#TODO make this total all parts cost
fillableform_for_parts = None#TODO figure out how to make a fillable form for all parts entered

alarmOptions = ['Unit out of fuel','EWN FC Lockout','Estop','FC stack frozen','UI can-bus failure']

for data in root:
    dataDict =root.attrib
    fchoursCell = (dataDict['FuelCellHours'])
    systemCell = (dataDict['SerialNumber'])
    break

for child in root:
    alarmDict = child.attrib      #This lists the alarm codes as dicts
    alarm_list = alarmOptions 
    for alarm in alarm_list:
        if alarm in alarmDict.values():
            print ('contains this alarm', alarm)
        else:
            print ('No valid operator error alarm found in event file')
            break

# this script updates excel cells.
excel = win32.gencache.EnsureDispatch('Excel.Application')
#Change this location to match the file template name as long as same folder. IE. E-stop.xlxs
wb = excel.Workbooks.Open('C:\\Users\\jtdev\\Desktop\\testcb.xlsx')
# wb = excel.Workbooks.Open(r'C:\myfiles\excel\workbook2.xlsx')
ws = wb.Worksheets('Copy1')

excel.Visible = False


 
#This is the cell formating  ws.Cells(row , column)

ws.Cells(6, 9).Value = woCell  
ws.Cells(9, 3).Value = systemCell 
ws.Cells(10, 3).Value = truckCell 
ws.Cells(11, 3).Value = fchoursCell 
ws.Cells(12, 3).Value = dateCell 
ws.Cells(8, 7).Value = occuredCell
ws.Cells(8, 10).Value = repairSdate 
ws.Cells(8, 13).Value = repairCdate 
ws.Cells(31, 15).Value = laborCell 
ws.Cells(31, 17).Value = partCostCell  
ws.Cells(32, 15).Value = laborCell + partsCostCell
#todo add all the cells for the parts consumed form


#TODO make saveas a variable location in gui.savefile funtion
wb.SaveAs('C:\\Users\\jtdev\\Desktop\\UpdatedTestcb.xlsx')

excel.Application.Quit()

master.mainloop()
