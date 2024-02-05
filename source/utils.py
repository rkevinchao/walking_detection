'''
Descriptions:
- Including several utilities functions
- Some functions are modified from "01_data_understanding.ipynb"

Latest Updated: 2024-02-04
By Kevin Chao (kevinchao@gmail.com)
'''

import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np
import numpy.ma as ma

def get_all_files():
    data_path = "../data/raw_accelerometry_data/" # Directory of raw accelerometer data 
    all_files = glob.glob(data_path+'*.csv')      # Get names for all CSV files
    return all_files

def load_single_data(all_files, file_id):
    file_id = all_files[file_id]   # Define which file to read
    df = pd.read_csv(file_id)      # Load CSV into a DataFrame
    return file_id, df

def plot_zoomin(file_id, df, activity, device_location, t0=None, t1=None):
    '''
    Function to plot a zoom-in acc records
    t0_index: the first index of data point in an dataframe
    t1_index: the last index of data point in an dataframe
    '''

    def appl_mask(x, y):
        '''
        This sub-function will deal with missing data points for showing correct plot of time series data         
        '''
        threshold = 0.01*5                    # Default sampling rate rate is 100-HZ (0.01 sec); Here set to allow 5 of missing data points  
        mask = x.diff()>threshold             # Find missing periods if the gap is greater than the default sampling rate
        masked_x = ma.masked_where(mask, x)   # Fill gap with '-'
        masked_y = ma.masked_where(mask, y)   # Fill gap with '-'
        return masked_x, masked_y

    df2 = df[df.activity==activity]  # Select data for a certain Activity
    
    # Define device location
    loc_x = device_location+'_x'
    loc_y = device_location+'_y'
    loc_z = device_location+'_z'
    
    # Check activity type
    if activity==1:
        activity_type = "Walking"
    elif activity==2:
        activity_type = "Descending Stairs"
    elif activity==3:
        activity_type = "Ascending Stairs"
    elif activity==4:
        activity_type = "Driving"
    elif activity==77:
        activity_type = "Clapping"
    elif activity==99:
        activity_type = "Non-study Activity"
        
    # Check device location
    if device_location=='lw':
        loc = "Left Wrist"    
    elif device_location=='rw':
        loc = "Right Wrist" 
    elif device_location=='lh':
        loc = "Left Hip"
    elif device_location=='rh':
        loc = "Right Hip"        
    elif device_location=='la':
        loc = "Left Ankle"
    elif device_location=='ra':
        loc = "Right Ankle"
        
    # Plot zoom-in Acc data
    x = df2.time_s
    y = df2[loc_x]
    masked_x, masked_y = appl_mask(x, y)
    plt.plot(masked_x, masked_y, label=loc_x)

    x = df2.time_s
    y = df2[loc_y]
    masked_x, masked_y = appl_mask(x, y)    
    plt.plot(masked_x, masked_y, label=loc_y)

    x = df2.time_s
    y = df2[loc_z]
    masked_x, masked_y = appl_mask(x, y)  
    plt.plot(masked_x, masked_y, label=loc_z)
    
    plt.xlabel('Seconds')
    plt.ylabel('m/s^2')
    plt.legend()
    if (t0 is not None) and (t1 is not None):
        plt.xlim(t0, t1)
    file_id = file_id.split('/')[-1]
    plt.title('File='+file_id+' / Activity='+activity_type+' / Device Location='+loc)


