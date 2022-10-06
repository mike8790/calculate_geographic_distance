# export maths for distance calculations and pandas to work with dataframe
# other modules available for calculating geographic distances but I stayed with
# standard modules
from math import sin, cos, sqrt, atan2, radians
import pandas as pd
import time
import csv

def calc_dist_coord(df, num_near):

    range_len = range(len(df.hotel_id))

    # initialise dataframe to store distances at each loop
    column_1 = list(df.hotel_id)
    big_list = []

    # begin outer loop to iterate through each hotel on list 
    for n in range_len:

        # initialise list to hold distances for current working hotel (n)
        top_ten = [100000000] * num_near
        top_ten_names = [1000] * num_near

        # create variable from hotel(n) longitude and latitude - so dataframe doesn't have to be
        # dynaimcally indexed at each iteration of the inner loop
        n_long = df.longitude[n]
        n_lat = df.latitude[n]


        # begin inner loop to iterate through each hotel and measure distance from hotel(n) 
        for i in range(10):

            # create variable from hotel(i) longitude and latitude - so dataframe doesn't have to be
            # dynaimcally indexed multiple times for distance calculations
            i_long = df.longitude[i]
            i_lat = df.latitude[i]

            # diff. between longitudes and latitudes of two locations needed to 
            # calculate distances between them
            dlong = radians(i_long - n_long)
            dlat = radians(i_lat - n_lat)


            # equation to calculate distance between two points on sphere (Haversine Equation)
            a = (sin(dlat / 2) * sin(dlat / 2) +
                cos(radians(n_lat)) * cos(radians(i_lat)) *
                sin(dlong / 2) * sin(dlong / 2)) 
            c = 2 * atan2(sqrt(a), sqrt(1 - a)) # can multiply c by 6373.0 to get distance in km

            if c != 0.0:
                top_ten[i] = c
                top_ten_names[i] = str(column_1[i])

        for jj in range(10, len(df.hotel_id)):

            # create variable from hotel(i) longitude and latitude - so dataframe doesn't have to be
            # dynaimcally indexed multiple times for distance calculations
            i_long = df.longitude[jj]
            i_lat = df.latitude[jj]

            # diff. between longitudes and latitudes of two locations needed to 
            # calculate distances between them
            dlong = radians(i_long - n_long)
            dlat = radians(i_lat - n_lat)


            # equation to calculate distance between two points on sphere (Haversine Equation)
            a = (sin(dlat / 2) * sin(dlat / 2) +
                cos(radians(n_lat)) * cos(radians(i_lat)) *
                sin(dlong / 2) * sin(dlong / 2))
            c = 2 * atan2(sqrt(a), sqrt(1 - a)) # can multiply c by 6373.0 to get distance in km
                
            for ii in range(0, 10):
                if c < top_ten[ii] and c > 0.0:
                    top_ten[ii] = c
                    top_ten_names[ii] = str(column_1[jj])
                    break

        top_ten_full = list(zip(top_ten_names, top_ten))
        big_list.append(top_ten_full)

    big_list = list(zip(column_1, big_list))

    return big_list

# # lines used to test function

t2 = time.time()

df = pd.read_csv("tester_csv2.csv", sep= ',')
num_near = 10

bubba_dubba = calc_dist_coord(df, num_near)

print(time.time() - t2)



