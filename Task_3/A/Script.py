# Anuneet Anand
# 2018022
# Table Extraction

import os
import tabula
import camelot
import pandas as pd


File = input('File Name : ')

x = tabula.read_pdf(File,pages="all",multiple_tables=True,guess=True)

for i in range(len(x)):
	x[i].to_csv(File+"_Table "+str(i+1)+".csv")

# END OF CODE
