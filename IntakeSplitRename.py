# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:31:36 2023

SCRIPT FOR EASIER SPLITTING AND NAMING OF MARHSALL PDFs

@author: Ethan Davis
"""



### imports
import os
from pypdf import PdfWriter, PdfReader

j = 20
box = "56"
num = "001"
split = [1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

fpath = f"C:/Users/Davis/Desktop/MarshallPDFProject/Box{box}/Box0{box}/"
fname = f"MarshallPentagonSelected_B0{box}_F{num}.pdf"
reader = PdfReader(fpath+fname)

outpath = f"C:/Users/Davis/Desktop/MarshallPDFProject/Box{box}_Output/Box0{box}/"
outpathExist = os.path.exists(outpath)
if not outpathExist:
    os.makedirs(outpath)

for i in range(0, (len(split)-1)):
    merger = PdfWriter()
    span = split[i+1] - split[i] ### length of each sub document
    
    ### stuff for naming outputs nicely
    hold = str(j).rjust(3, "0")
    outname = f"MarshallPentagonSelected_B0{box}_F{hold}.pdf"
    outfile = outpath+outname
    print(outname)
    
    ### split the file, append the pages, write to output
    merger.append(reader, (split[i]-1, split[i]-1 + span))
    output = open(outfile, 'wb')
    merger.write(output)
    merger.close()
    output.close()
    
    ### iterate j
    j = j + 1
    
print(f"Success. New J = {j}")