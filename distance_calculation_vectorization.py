#!/usr/bin/python

## to run this module: top of script add:
# 'from distance_calculation_vectorization import calc_dist_coord'
# Need numpy, pandas, scipy and haversine modules installed

import numpy as np 
import pandas as pd
from scipy.spatial.distance import squareform, pdist
from haversine import haversine


## function that takes a csv (containing hotels, latitude and longitude) and number (N), to calculate N 
# closest hotels to each hotel on list  

def calc_dist_coord(csv: str, num_near: int, printout: bool= False, savename: str= None):

    # open CSV in to dataframe
    df = pd.read_csv(csv, sep= ',')

    # take long/ lat and create coordinate array, create array with hotel IDs
    data = df[['latitude','longitude']].to_numpy()
    hotels = df['hotel_id'].to_numpy()

    # use squareform, pdist to calculate distance matrix of each set of coordinates from each other
    # use haversine algorith, then fill diagonals (distance of hotel from itself) with high number
    # so not considered when calulating closest 10 hotels
    dm = squareform(pdist(data, metric=haversine))
    np.fill_diagonal(dm, 100000)

    # find index of 10 shortest distances for each column - to be used to index distance matrix and 
    # extract 10 closest hotels for each hotel
    # argpartition will sort N smallest numbers to first N rows of each column, but N rows will not
    # be in sorted order 
    indices = np.argpartition(dm, num_near)[:, :num_near].T

    # # initialize empty lists to store ten hotels and there distances for each column 
    hotel_orders = []
    distances_orders = []

    # loop through distance matrix on a column x column basis and extract 10 hotels, 
    # extract ID of those 10 hotels from hotel list
    # sort ten extracted distances and hotels as zipped list so hotel id and distances
    # stay together, append each distance and hotel to corresponding lists

    for n in range(indices.shape[1]):
        Y = dm[indices[:, n], n]
        X = hotels[indices[:, n]]
        sorted_list = sorted(zip(X, Y), key = lambda x: x[1])
        distances_orders.append([x for _,x in sorted_list])
        hotel_orders.append([x for x,_ in sorted_list])

    # create new df and add lists of hotels and their distances, set index to name of each hotel
    df2 = pd.DataFrame()
    df2['Hotels'] = hotels
    df2['closest_hotels'] = hotel_orders
    df2['distances'] = distances_orders
    df2.set_index('Hotels', inplace=True)

    # return dataframe with N closest hotels to each hotel, and their distances    
    if printout == True:
        print(df2)

    if savename != None:
        df.to_csv(savename)

    return df2  

if __name__ == "__main__":
    import sys
    arg1, arg2, arg3 = sys.argv[1:4]


