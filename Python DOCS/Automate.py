#Python code parsing XML files and saving in specified xlxs (excel) fields.
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
from tkinter import filedialog
from tkinter import *
import win32com.client as win32

def loadRSS(): #delete after done
 
    # url of rss feed
    url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
 
    # creating HTTP response object from given url
    resp = requests.get(url)
 
    # saving the xml file
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)

def loadwo(): #select XML file to parse
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("XML","*.xml"),("all files","*.*")))
    print (root.filename)


def parseXML(xmlfile):
 
    # create element tree object
    tree = ET.parse(xmlfile)
 
    # get root element
    root = tree.getroot()
 
    # create empty list for imported data
    dataimport = []
 
    # iterate data items
    for item in root.findall('./channel/item'):
 
        # empty data dictionary
        data = {}
 
        # iterate child elements of item
        for child in item:
 
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
 
        # append data dictionary to data items list
        dataimport.append(data)
     
    # return data items list
    return dataimport
 
 
def savetoCSV(dataimport, filename):
 
    # specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']
 
    # writing to csv file
    with open(filename, 'w') as csvfile:
 
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)
 
        # writing headers (field names)
        writer.writeheader()
 
        # writing data rows
        writer.writerows(dataimport)
 
     
def main():
    # load rss from web to update existing xml file
    loadwo()
 
    # parse xml file
    dataimport = parseXML('topnewsfeed.xml')
 
    # store data items in a csv file
    savetoCSV(dataimport, 'topnews.csv')


if __name__ == "__main__":
 
    # calling main function
    main()


excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open('root.filename') #might need to take out ''
wb.XmlImport("D:/tmp/result.xml") # put csv file here - might take out ''
wb.SaveAs("D:\\tmp\\result.xlsx") # this is the excel file name to be saved. IE. WO number -might need to remove ''
wb.Close()
