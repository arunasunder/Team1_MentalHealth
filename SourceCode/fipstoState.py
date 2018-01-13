#Below python script cretaes a dictionary with fips code and state abbreviations in USA
#import dependencies
import csv
import pandas as pd
import os
print("Starting input processing")
#read the input file
inputfilepath=os.path.join("..","raw_data","input","state_fips_master.csv")
fips_df=pd.read_csv(inputfilepath)

#create new df with required columns
fips_new=fips_df[["state_abbr","fips"]]

#create a list with fips code of islands
fips_list=[66,72,78]
fips_state=["GU","PR","VI"]
#create dataframe and concat the two dataframes
new_df=pd.DataFrame({"state_abbr":fips_state,
                    "fips":fips_list})
frames=[fips_new,new_df]

result = pd.concat(frames).reset_index(drop=True)

#create dictionary
fips_dict=result.set_index('fips')['state_abbr'].to_dict()
#set output path and save to csv
#outputfilepath=os.path.join("..","raw_data","output","fipstostate.csv")
#result.to_csv(outputfilepath,index=False)
print("Successfully Completed")


import numpy as np

np.save('fips_state', fips_dict) 

# Load
read_dictionary = np.load('fips_state.npy').item()
print(read_dictionary[1]) 