import xlrd



arquivo=xlrd.open_workbook('dados.xlsx')
planilha=arquivo.sheet_by_name("Folha1")
matricula=planilha.col_values(0) #primeira coluna
nome=planilha.col_values(1) #segunda coluna
situacao=planilha.col_values(2)

#identificar quantidade de folhas/abas
print("Amount de folhas/worksheet {0}".format(arquivo.nsheets))
print("List name Worksheet : {0}".format(arquivo.sheet_names()))

sh = arquivo.sheet_by_index(0)
print("name worksheet: {0} \nregistration amount:{1} \ncoluns amount: {2}".format(sh.name, sh.nrows, sh.ncols))

print("Get Cell B4 is {0}".format(sh.cell_value(rowx=3, colx=1)))

#IMPRIMI TABELA COMPLETA
for rx in range(sh.nrows):
    print(sh.row(rx))


# print(matricula)
# cont = 0
# for m in matricula:
#     #print(m) #imprimi matriculas
#     cont = cont + 1
#
# print(cont)

# print(y)