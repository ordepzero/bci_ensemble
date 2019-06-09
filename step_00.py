import definitions as defs
import pandas as pd
import scipy.io as sio
import filters



def signals_segmentation(code_file,stimulus_file,signal_file,seg_begin,seg_end):
    # É utilizado o valor 42 porque é o intervalo entre os estímulos
    # 64 é a quantidade de canais
    
    codes = []
    stimulus = []
    signals_segments = []
    
    for i in range(len(code_file)):
        temp_codes = []
        temp_stimulus = []
        for j in range(0,len(code_file.loc[ i , : ]),42) :
            if(code_file.loc[ i , j] != 0): 
                temp_codes.append(code_file.loc[ i , j]) 
                temp_stimulus.append(stimulus_file.loc[ i , j]) 
                
                begin = i * 64
                end = begin + 64
                for k in range(begin,end):
                    signals_segments.append(signal_file.loc[ k , j+seg_begin : j+seg_end])
        codes.append(temp_codes)
        stimulus.append(temp_stimulus)
        
    return codes,stimulus,signals_segments

if __name__ == '__main__': 
    
    defs.create_directories()
    
    subjects = ['A','B']
    segments_begin = [0]#[0,24,48,72]
    segments_end = [160]
    
    filter_order = 5
    lowcut = 0.1
    highcut= 10.0
    
    for subject in subjects:
        if(subject == 'A'):
            signal_file = pd.read_table(defs.SIGNAL_FILE_A,delim_whitespace=True,header=None)
            stimulus_file = pd.read_table(defs.STIMULUS_FILE_A,delim_whitespace=True,header=None).T
            code_file = pd.read_table(defs.STIMULUS_CODE_A,delim_whitespace=True,header=None).T
        else:
            signal_file = pd.read_table(defs.SIGNAL_FILE_B,delim_whitespace=True,header=None)
            stimulus_file = pd.read_table(defs.STIMULUS_FILE_B,delim_whitespace=True,header=None).T
            code_file = pd.read_table(defs.STIMULUS_CODE_B,delim_whitespace=True,header=None).T
    
        for seg_begin in segments_begin:
            for seg_end in segments_end:
                codes,stimulus,signals_segments = signals_segmentation(code_file,stimulus_file,signal_file,seg_begin,seg_end)

        signals_segments = filters.chebyshev1_filter(signals_segments,0.1, 10.0, filter_order)
        
        
        filename = subject
        filename = filename+"_"+str(filter_order)
        filename = filename+"_"+str(highcut).replace(".","")[0:2]
        filename = filename+".mat"
        
        if(subject == 'A'):
            filename = defs.DIRECTORY_SIGNALS_CHANNELS_A+"/"+filename
        else:
            filename = defs.DIRECTORY_SIGNALS_CHANNELS_B+"/"+filename
        
        base = {'signals':signals_segments,'targets':stimulus,'codes':codes}
        sio.savemat(filename, base)
        