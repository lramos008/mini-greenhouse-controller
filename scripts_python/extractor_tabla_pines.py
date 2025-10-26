import tabula
import pandas as pd

pdf_path = "stm32f401re.pdf"
extract_pages = range(38, 45)
columns = ['UQFN48', 'WLCSP49', 'LQFP64', 'LQFP100', 'UFBGA100', 'Pin name', 
           'Pin type', 'I/O structure', 'Notes', 'Alternate functions', 
           'Additional functions']

desired_columns = ['LQFP64', 'Pin name', 'Pin type', 'Alternate functions']

#Extraccion de tablas
tables = tabula.read_pdf(pdf_path, pages= extract_pages[0],                        #Extraigo tablas de la primer página
                         multiple_tables=True, lattice=True)
tables.pop(0)                                                                      #Elimino la primer tabla que no me sirve

tables[0] = tables[0].dropna(how = 'all')
tables[0] = tables[0].dropna(axis = 1, how = 'all')

#Extraigo el resto de la tabla
for i in extract_pages[1:]:
    df = tabula.read_pdf(pdf_path, pages= i, multiple_tables=False, 
                         lattice=True)[0]
    df = df.dropna(how = 'all')                                                 #Elimino columnas y filas nan para cuidar alineacion
    df = df.dropna(axis = 1, how = 'all')
    
    tables.append(df)

# A cada tabla les asigno los mismos nombres de columna
for i in range(0, len(tables)):
    tables[i].columns = columns

# Concateno todas las tablas para obtener la tabla de pines completa
pin_table = pd.concat(tables, ignore_index= True)
pin_table.to_csv("stm32f401re_pin_table.csv", index = False)


