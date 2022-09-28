# export maths for distance calculations and pandas to work with dataframe
# other modules available for calculating geographic distances but I stayed with
# standard modules
from math import sin, cos, sqrt, atan2, radians
import pandas as pd
import time

def calc_dist_coord(df, num_near):

    t2 = time.time()

    range_len = range(len(df.hotel_id))

    # initialise dataframe to store distances at each loop
    column_1 = list(df.hotel_id)
    df_dist = pd.DataFrame(column_1, index=column_1)

    # initialise empty list that will store information for each hotel
    full_list = []

    # begin outer loop to iterate through each hotel on list 
    for n in range_len:

        # initialise list to hold distances for current working hotel (n)
        dist_list = []
        
        # create column name variable from id of current working hotel (n)
        column_name = str(column_1[n])

        # create variable from hotel(n) longitude and latitude - so dataframe doesn't have to be
        # dynaimcally indexed at each iteration of the inner loop
        n_long = df.longitude[n]
        n_lat = df.latitude[n]


        # begin inner loop to iterate through each hotel and measure distance from hotel(n) 
        for i in range_len:

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
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            c = c * 6373.0 # can multiply c by 6373.0 to get distance in km
            
            # append distance measured between hotel(n) and hotel(i) to distance list
            dist_list.append(c)
           
        # add distance list for (n) to dataframe - transferring to dataframe allows for identification 
        # of closest hotels (id & distance) using few lines of code with: pd.nsmallest function
        df_dist["dist"] = dist_list
        # distances of 0.0 (when hotel (n) is measured against itself) converted 
        # to 10000 to avoid identifying (n) as closest hotel to (n)
        df_dist = df_dist.replace(0.0, 10000)
        # identify N closest, user-specified
        closest_hotels = df_dist.nsmallest(num_near, 'dist')

        # make list out of identities and distances of the N closest hotels, append to 
        # 'full_list' with hotel (n)
        close_hotel = list(closest_hotels.iloc[:,0])
        hotel_distance = list(closest_hotels.iloc[:,1])
        full_list.append([column_name, close_hotel, hotel_distance])

    # convert 'full_list' to dataframe for easier indexing/ saving elsewhere etc
    df_full = pd.DataFrame(full_list, columns=["hotel", "closest_hotels", "distances"])
        
    print(time.time() - t2)
    return df_full     

# # lines used to test function
df = pd.read_csv("tester_csv.csv", sep= ',')
num_near = 10
print(calc_dist_coord(df, num_near))


