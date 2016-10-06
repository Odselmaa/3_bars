# 3_bars
https://github.com/Odselmaa/3_bars
## What is this?
This code is written for finding biggest, smallest bar
and closest bar corresponding to current latitude and longitude.

## How to run?
- In order to execute code, for example in Moscow, you need to download JSON file from here:
http://data.mos.ru/opendata/7710881420-bary
- Save it in one folder where locates code file named 'bars.py'
- Run it

## bars.py
 - load_data(filepath)
    loads json data from given path, returns json data as an array</br>
    filepath</br>
    **Type**: string

- get_biggest_bar(bar_list)
    returns biggest bar in bar list</br>
    bar_list</br>
    **Type**: List
    
- get_smallest_bar(bar_list)</br>
    returns smallest bar in bar list
    
- get_closest_bar(bar_list, longitude, latitude)</br>
    searches, returns closest bar in bar list according to given longitude and latitude</br>
    
    bar_list</br>
    **Type**: List</br>
    
    longitude, latitude</br>
    **Type***:Double
    
- get_bar_seat(bar)</br>
    returns seat of given bar

- sort_by_cells_item(bar_list)</br>
    returns sorted bar list by total seat

- get_name(bar)</br>
    returns bar name

- get_address(bar)  </br>
    returns bar address

- get_distance(long1, lat1, long2, lat2)</br>
    calculate distance between two points that given by latitude and longitude
