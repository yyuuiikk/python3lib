import csv

with open('./row.csv') as f:
    print(f.read())

    # csvの内容をリストに格納
    reader = csv.reader(f)
    for row in reader:
        print(row)