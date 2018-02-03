import xml.etree.ElementTree as ET
import tkinter
from tkinter import *
from  tkinter import filedialog
from tkinter import simpledialog
import win32com.client as win32
import time

#TODO make name match wo number as input by user
#TODO make customerCell and locationCell and nameCell, signatureCell not have to be entered every time.  Some way for it to hold the data unless changed by user.

#User selects file to parse
master = Tk()
master.filename =  filedialog.askopenfilename(initialdir = "Path Where the dialog should open first",title = "Select Event File",filetypes = (("xml files","*.xml"),("all files","*.*")))
print (master.filename)

tree = ET.parse(master.filename)#this is where the file location to be parsed goes
root = tree.getroot()
         
woCell = tkinter.simpledialog.askstring("Enter WO #", "Enter WO Number")
print (woCell)

#this is a gui for user to select which template to use and variable selected will be used to open an existing excel template that will be included in program folder.
                  
variable = StringVar(master)
variable.set("Select the main fault for billable event") # default value
w = OptionMenu(master, variable, 'Out of fuel', 'Dead battery from misuse', 'E-stop', 'Frozen', 'Damage', 'E-brake unplugged', 'OI unplugged', 'Other')
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
     
repairSdate = tkinter.simpledialog.askstring("Enter Repair Start Time", "Enter Repair Start Time\nFormat yyyy-mm-dd hh:mm")
print (repairSdate)

repairCdate = tkinter.simpledialog.askstring("Enter Repair completed Time", "Enter Repair completed Time\nFormat yyyy-mm-dd hh:mm")
print (repairCdate)

laborCell = tkinter.simpledialog.askstring("Enter labor hours", "Enter labor hours")
print (laborCell)
master.withdraw()

dateCell = time.strftime("%d/%m/%Y")

alarmOptions = ['Unit out of fuel','EWN FC Lockout','Estop','FC stack frozen','UI can-bus failure']

for data in root:
    dataDict =root.attrib
    fchoursCell = (dataDict['FuelCellHours'])
    systemCell = (dataDict['SerialNumber'])
    break

for child in root:
    alarmDict = child.attrib      #This lists the alarm codes as dicts
    for alarm in alarmOptions:
        if alarm in alarmDict.values():
            print ('contains this alarm',alarm)
            alarmTime = (alarmDict['CreatedDate'])  #This pulls timestamp of alarm from xml file
            print (alarmTime)

try:
    alarmTime      
except NameError:
    print ('No operator error alarm code found')
    alarmTime = tkinter.simpledialog.askstring("Enter Event Occured  Time", "Enter Occured Time\nFormat yyyy-mm-dd hh:mm")
    print (alarmTime)
    

occuredCell = alarmTime #TODO make alarmTime = optionmenu selection occured time
partsCostCell = None #TODO make this total all parts cost
fillableform_for_parts = None #TODO figure out how to make a fillable form for all parts entered

# this script updates excel cells.
excel = win32.gencache.EnsureDispatch('Excel.Application')
#Change this location to match the file template name as long as same folder. IE. E-stop.xlxs
selection = variable.get()
if selection == 'Out of fuel':
    wb = excel.Workbooks.Open('C:\\Users\\jtdev\\Desktop\\testcb.xlsx')
if selection == 'Dead battery from misuse':
    wb = excel.Workbooks.Open('C:\\Users\\jtdev\\Desktop\\testcb1.xlsx')
if selection == 'E-stop':
    wb = excel.Workbooks.Open('C:\\Users\\jtdev\\Desktop\\testcb2.xlsx')
if selection == 'Frozen':
    wb = excel.Workbooks.Open('C:\\Users\\jtdev\\Desktop\\testcb3.xlsx')
if selection == 'Damage':
    wb = excel.Workbooks.Open('C:\\Users\\jtdev\\Desktop\\testcb4.xlsx')
if selection == 'E-brake unplugged':
    wb = excel.Workbooks.Open('C:\\Users\\jtdev\\Desktop\\testcb5.xlsx')
if selection == 'OI unplugged':
    wb = excel.Workbooks.Open('C:\\Users\\jtdev\\Desktop\\testcb6.xlsx')
if selection == 'Other':
    wb = excel.Workbooks.Open('C:\\Users\\jtdev\\Desktop\\testcb7.xlsx')  
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
ws.Cells(31, 17).Value = partsCostCell  
ws.Cells(32, 15).Value = None # laborCell + partsCostCell
#todo add all the cells for the parts consumed form

#TODO make saveas a variable location in gui.savefile funtion
wb.SaveAs('C:\\Users\\jtdev\\Desktop\\UpdatedTestcb.xlsx')

excel.Application.Quit()

master.mainloop()
exit()
