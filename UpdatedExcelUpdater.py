#! python3
# this script updates excel cells.

import openpyxl
import win32com.client as win32




excel = win32.gencache.EnsureDispatch('Excel.Application')
#Change this location to match the file template name as long as same folder. IE. E-stop.xlxs
wb = excel.Workbooks.Open('C:\\Users\\PlugService\\Desktop\\testy.xlsx')
# wb = excel.Workbooks.Open(r'C:\myfiles\excel\workbook2.xlsx')
ws = wb.Worksheets('Copy1')


excel.Visible = False

#Placeholder variables - TODO: change values to equal user input

customerCell = 'Kroger'  #TODO make customerCell and locationCell and nameCell, signatureCell not have to be entered every time.  Some way for it to hold the data unless changed by user.
woCell = '10' #TODO make this the variable for wo input gui
systemCell = '999' #TODO  autofil from xml data
nameCell =
truckCell = #TODO user input gui
fchoursCell #TODO autofill from xml
dateCell = #TODO autofill from computer date/time
occuredCell = #TODO autofill from xml data, must check against alarm template to specificy what time to select from the xmlfile.  IE.  OOF occured at 1500 , program checks for the string 'out of fuel' in xml data and enters that time as variable
repairSdate = #TODO create GUI for entering repair start time
repairCdate = #Todo create gui for entering repair complete time
laborCell = #TODO creat GUI for labor hour input
partCost = #TODO make this total all parts cost
fillableform_for_parts = #TODO figure out how to make a fillable form for all parts entered
signatureCell = 


#This is the cell formating  ws.Cells(row , column)
ws.Cells(6, 3).Value = customerCell
ws.Cells(7, 3).Value = locationCell
ws.Cells(6, 9).Value = woCell  
ws.Cells(6, 12).Values = nameCell 
ws.Cells(9, 3).Value = systemCell 
ws.Cells(10, 3).Value = truckCell 
ws.Cells(11, 3).Value = fchoursCell 
ws.Cells(12, 3).Value = dateCell 
ws.Cells(8, 7).Values = occuredCell
ws.Cells(8, 10).Values = repairSdate 
ws.Cells(8, 13).Values = repairCdate 
ws.Cells(31, 15).Values = laborCell 
ws.Cells(31, 17).Values = partCostCell  
ws.Cells(32, 15).Values = laborCell + partsCostCell
#todo add all the cells for the parts consumed form
ws.Cells(34, 1).Values = 'Technician signature:' + signatureCell 



#TODO make saveas a variable location in gui.savefile funtion
wb.SaveAs('C:\\Users\\PlugService\\Desktop\\testyUpdate.xlsx')

excel.Application.Quit()
