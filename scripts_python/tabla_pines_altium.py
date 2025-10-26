# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 14:26:42 2025

@author: Juli-Leo
"""

import pandas as pd

path = "stm32f401re_pin_table.csv"
desired_columns = ['LQFP64', 'Pin name', 'Pin type', 'Alternate functions']
new_header = ['Designator', 'Display Name', 'Electrical Type', 'Description']

# Abro el archivo .csv con la tabla de pines
pin_table = pd.read_csv(path)

# Elijo las columnas de interes
pin_table = pin_table[desired_columns]

# Me quedo solo con las filas que correspondan al LQFP deseado (sin -)
pin_table = pin_table[pin_table['LQFP64'] != "-"]

#Adapto la tabla segun los requerimientos de altium
pin_table['Pin type'] = pin_table['Pin type'].replace('S', 'Power')
pin_table['Pin type'] = pin_table['Pin type'].replace('I', 'Input')

#Cambio el header actual por el requerido por altium
pin_table.columns = new_header

pin_table.to_csv("stm32f401re_altium_table.csv", index = False)