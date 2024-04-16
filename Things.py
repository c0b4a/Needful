#!/usr/bin/env python
#Needful

#good formatting
#!/usr/bin/env python
def main() -> None:
if __name__ == '__main__':
    main()

#splits based on delimiter into an array of strings
splitByWord = [str(x) for x in pc.paste().split('\t')]

#joins array of strings into a single string
copyable = ''.join(formattedData)

#gets date
timeNow = dt.datetime.now()
date = timeNow.strftime('%m/%d/%y')

#create pyperclip copyable string from list
copyable = ''.join(list)
pc.copy(copyable)

#process xl sheets
from openpyxl import load_workbook
def openSheet(path):
    workbook = load_workbook(filename = path)
    sheet = workbook.active
    return sheet
sheet['B'] #gets row, get cell index's with [B4], collumn [4]
sheet['C7'].value

#removes tailing chars from strings
string = string.replace('A', '')
string = string.replace('Z', '')

#pandas and pdf parsing
import pandas as pd
from pypdf import PdfReader
data = {'Id': [None]*100, 'stored': [None]*100, 'part': [None]*100}
dataFrame = pd.DataFrame(data=data)
dataFrame.loc[index, 'Id'] = idList[0]
print(sys.getsizeof(df))
dataFrame.to_csv('Report.csv')
#set reader up and allows specify file
reader = PdfReader(sys.argv[1])
#calculates page quantity
PdfLen = len(reader.pages)
for x in range(PdfLen):
    #skip first page
    if x == 0:continue
    page = reader.pages[x]
    pageText = page.extract_text(0)

#find 1-2 digits followed by 'mm'
findMM = re.compile('\d{1,2}mm')
find8D = re.compile('\d{8}')

#more regex
reFilteredList = re.findall(regex, textSource)

#open output stream
f = open('Report.txt', 'w+')
