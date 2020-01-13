import csv

rows = [[0,1,2], ['a','b','c']]
with open('./row.csv', 'a', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(rows)