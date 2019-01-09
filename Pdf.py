from tabula import read_pdf
df = read_pdf("Pelna_tabela_notowan_z_dnia_2017.05.25.pdf", encoding='latin2', engine='python', pages="all")
#lub np pages='1-3, 6'

convert_into("Pelna_tabela_notowan_z_dnia_2017.05.25.pdf", "test.csv", output_format="csv", pages="all")
!cat test.csv
