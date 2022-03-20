from .run import *
from .calltoreducer import calltoreducer
def cek_simlilarity2(recorded_sound,url_bacaan): 
    # print (".WAV Search Engine Version 1 (For Python Ver. 3+) ")
    
    good_file = 0
    
    # while (good_file == 0):
    #     query     = input("Submit .wav file to search against repository (Example: button.wav): ")
    #     if (os.path.isfile(query)):
    #         good_file = 1    
    #     query_wavsound = wavsound(query)    
    
    query_wavsound = wavsound(recorded_sound) 
                
    # print("\n**Higher number of partitions increases false positive rates, \nwhile lower number of partitions increases false negative rates\n")
    # samplelength = input("Set word size (sample length) (5 ~ 100) : ");
    samplelength = 5
    # samples   = input("Set number of samples (n) of partitions from 1 to " + str(int(len(query_wavsound.get_data())/float(samplelength))) + ": ")
    samples   = 3
    
    # repository look up directory
    # print(url_bacaan)
    # dbdir    = input("Enter repository directory to search (example: 'db') : ")
    dbdir    = url_bacaan
    # max_split = int(input("Set maximum allowable number of split repositories : "))
    max_split = 2
    
    # repository query time
    start_time = time.time()        
            
    result_lst = run(recorded_sound, int(samplelength), samples, dbdir, max_split)
            
    # output
    output = "Search Result: \n" 
            
    keluaran = ""
    # Tabulate % match (wav files with 0% match are excluded from the result)
    for pair in result_lst:
        output += pair[0] + " : " + (40-len(pair[0]))*" " + pair[1] + "% match" + "\n"
        keluaran =    (40-len(pair[0]))*" " + pair[1] + "% "  
        
    # print(keluaran)          
    # Show search time
    timelapse_parallel = time.time() - start_time   
    output = output + str(timelapse_parallel) + "seconds"
    # print(output)
    # remove all the spaces
    keluaran = keluaran.replace(" ","")
    return keluaran