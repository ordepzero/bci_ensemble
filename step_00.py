import definitions as defs
import pandas as pd

print(defs.SIGNAL_FILE_A)

signal_file = pd.read_table(defs.SIGNAL_FILE_A,delim_whitespace=True,header=None)
stimulus_file = pd.read_table(defs.STIMULUS_FILE_A,delim_whitespace=True,header=None).T
code_file = pd.read_table(defs.STIMULUS_CODE_A,delim_whitespace=True,header=None).T


codes = []
signals_segments = []

for i in range(len(code_file)):
    temp_codes = []
    for j in range(0,len(code_file.loc[ i , : ]),42) :
        if(code_file.loc[ i , j] != 0): 
            temp_codes.append(code_file.loc[ i , j]) 
            
            begin = i * 64
            end = begin + 64
            for k in range(begin,end):
                signals_segments.append(signal_file.loc[ k , j: j+160 ])
    codes.append(temp_codes)