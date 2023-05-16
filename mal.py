import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import xlsxwriter

url = 'https://api.worldnewsapi.com/search-news?api-key=1f5553b6cf1c4e13a9a78fde8a2b3b0d&https://api.worldnewsapi.com/search-news?api-key=1f5553b6cf1c4e13a9a78fde8a2b3b0d&earliest-publish-date=01-01-2023'
res = requests.get(url).json()

for new in res['news']:
    print(new['author'])
    print(new['title'])
    print(new['image'])
    print(new['text'])
    print('\n')

article = res['news']
for a,b in enumerate(article):
    print(f'{a}:     {b["title"]}')

for k,v in article[0].items():
    print(f'\n{k.ljust(15)}  {v}')

print(pd.DataFrame(article))
#write to csv
pd.DataFrame(article).to_csv('res.csv')
#write to excel
authors = []
titles = []
contents = []
for new in res['news']:
    authors.append(new['author'])
    titles.append(new['title'])
    contents.append(new['text'])


workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet('first')

worksheet.write(0,0,'0')
worksheet.write(0,1,'author')
worksheet.write(0,2,'title')
worksheet.write(0,3,'content')

for j in range(len(authors)):
    worksheet.write(j+1,0,str(j))
    worksheet.write(j+1,1,authors[j])
    worksheet.write(j+1,2,titles[j])
    worksheet.write(j+1,3,contents[j])

workbook.close()
