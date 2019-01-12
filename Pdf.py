from tabula import read_pdf
df = read_pdf("Pelna_tabela_notowan_z_dnia_2017.05.25.pdf", encoding='latin2', engine='python', pages="all")
#lub np pages='1-3, 6'

convert_into("Pelna_tabela_notowan_z_dnia_2017.05.25.pdf", "test.csv", output_format="csv", pages="all")


import camelot
tables = camelot.read_pdf('brzozow.pdf', pages='all')
tables

tables.export('brzozow.csv', f='csv', compress=True) 
tables[15]
tables[15].parsing_report
for i in range(len(tables)):
    print(tables[i].df)
tables[4].to_excel('brzozow.xlsx') 
tables[7].df
