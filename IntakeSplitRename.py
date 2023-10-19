# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:31:36 2023

SCRIPT FOR EASIER SPLITTING AND NAMING OF MARHSALL PDFs

@author: Ethan Davis
"""



### imports
import os
import sys
from pypdf import PdfWriter, PdfReader

#### new j for box 056 = 20
j = 1
box = "59"
num = "002"
split = [1]


fpath = f"C:/Users/Davis/Desktop/MarshallPDFProject/Box{box}/Box0{box}/"
fname = f"MarshallPentagonSelected_B0{box}_F{num}.pdf"
reader = PdfReader(fpath+fname)



outpath = f"C:/Users/Davis/Desktop/MarshallPDFProject/Box{box}_Output/Box0{box}/"
outpathExist = os.path.exists(outpath)
if not outpathExist:
    os.makedirs(outpath)
    
    
### Handles the case that the folder contains one document    
if len(split) == 1:
    merger = PdfWriter()
    
    ### Name output file nicely 
    hold = str(j).rjust(3, "0")
    outname = f"MarshallPentagonSelected_B0{box}_F{num}_{hold}.pdf"
    outfile = outpath+outname
    print(outname)
    
    ### append pages to output
    merger.append(reader)
    output = open(outfile, 'wb')
    merger.write(output)
    merger.close()
    output.close()
    
    ### iterate j
    j = j + 1
    
    print(f"Success. New J = {j}")
    
    ### quit program here so we don't double up on outputs
    sys.exit()
    
### Handles the case that there are multiple documents in folder
for i in range(0, (len(split))):
    merger = PdfWriter()      
    
    ### Handles last entry in split
    if i == (len(split)-1):
        if len(split) == len(reader.pages):
            span = split[i] - split[i-1] ### last entry = 1 page out
        else:
            span = len(reader.pages) - (split[i]-1) ### last entry = many page out
    else: 
        span = split[i+1] - split[i] ### length of each sub document

    
    ### stuff for naming outputs nicely
    hold = str(j).rjust(3, "0")
    outname = f"MarshallPentagonSelected_B0{box}_F{num}_{hold}.pdf"
    outfile = outpath+outname
    print(outname)
    
    ### split the file, append the pages, write to output
    merger.append(reader, (split[i]-1, split[i]-1 + span))
    print((split[i]-1, split[i]-1 + span))
    output = open(outfile, 'wb')
    merger.write(output)
    merger.close()
    output.close()
    
    ### iterate j
    j = j + 1
    
print(f"Success. New J = {j}")