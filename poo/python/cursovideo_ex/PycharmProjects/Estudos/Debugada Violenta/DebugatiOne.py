import csv
with open('covid.csv', 'r', encoding='utf-8') as arcovid:
    leitor = csv.reader(arcovid)
    next(leitor)
    for linha in leitor:
        if int(linha[2]) > 5:
            print(linha)