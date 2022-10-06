# Code to solve problem set for job application:

Take a list of hotels with latitude and longitude,
figure out N closest hotels (on hotel list) for each hotel.
Can be tested using the csv files present in repo, which contain varying numbers of hotels in list (to test speed).

### Hotel list takes form col_1 = 'hotel_id', col_2 = 'longitude', col_3 = 'latitude'

## How to use script
**'distance_calculation_vecotrization.py' is latest and most efficient code for calculating distances. To use in own script: **
* import - 'from distance_calculation_vectorization import calc_dist_coord'
* need numpy, pandas, scipy and haversine modules installed 
* in script 'calc_dist_coord(< csv >, < N >, < printout = False >, < savename = None >)' - 
* csv specifies the .csv file to be read containint the hotel list (details above), argument must be str type, required argument.
* N is the number of closest hotels you wish to calculate, argument must be int type, required argument
* printout: specify whether you wise to print function output, argument must be bool type, argument default = False, make True to print output
* savename = specify a filename (format= "*.csv") to save argument output to, argument must be str type, default = None (no file will be saved)
* Function returns a two column pandas dataframe: 
    + index = hotel ID 
    + column['closest_hotels'] = list containing hotel IDs of N closest (ordered in descending order, closest at position [0])
    + column['distances'] = list containing distances in kilometers of N closest hotels (distances correspond to hotel IDs in column[0])