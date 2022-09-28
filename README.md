# Code to solve problem set for job application:

Take a list of hotels with latitude and longitude,
figure out N closest hotels (on hotel list) for each hotel.

Hotel list takes form col_1 = 'hotel_id', col_2 = 'longitude', col_3 = 'latitude'

**'distance_calculation_vecotrization.py' is latest and most efficient code for calculating distances. To use in own script: **
* import - 'from distance_calculation_vectorization import calc_dist_coord'
* need numpy, pandas, scipy and haversine modules installed 
* in script 'calc_dist_coord(<csv>, <N>)' - csv is the csv containing hotel list, N is the number of closest hotels you wish to calculate 


Can be tested using the csv files present in repo, which contain varying numbers of hotels in list (to test speed).

Adjust .csv file read and N hotels listed at bottom of script

## To-do:
* ~~may adapt to make a module which can be run as script from command line~~
