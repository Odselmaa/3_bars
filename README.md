# 3_bars

=================================
https://github.com/Odselmaa/3_bars

What is this?
-------------
This code is written for finding biggest, smallest bar
and closest bar corresponding to current latitude and longitude.

How to run?
----------
1. In order to find those bars, for example in Moscow,
you need to download JSON file from here:
* http://data.mos.ru/opendata/7710881420-bary

2. Save it in one folder where locates code file named 'bars.py'

3. Run it


#bars.py
--------------------
 - load_data(filepath)
    loads json data from given path, returns json data as an array
    
    filepath
    Type: string

- get_biggest_bar(bar_list)
    returns biggest bar in bar list
    
    bar_list
    Type: List
    
- get_smallest_bar(bar_list)
    returns smallest bar in bar list
    
- get_closest_bar(bar_list, longitude, latitude)
    searches, returns closest bar in bar list according to given longitude and latitude
    
    bar_list
    Type: List
    
    longitude, latitude:
    Type:Double
    
- get_bar_seat(bar)
    returns seat of given bar

- sort_by_cells_item(bar_list)
    returns sorted bar list by total seat

- get_name(bar)
    returns bar name

- get_address(bar)  
    returns bar address

- get_distance(long1, lat1, long2, lat2):
    calculate distance between two points that given by latitude and longitude
