import json
import os

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)
    

def get_bar_seat(bar):
    return bar['Cells']['SeatsCount']
    
def sort_by_cells_item(bar_list):
    return  sorted(bar_list, key = get_bar_seat, reverse=False)

def get_distance(long1, lat1, long2, lat2):
    return ((long1 - long2)**2 + (lat1 - lat2)**2)**0.5
    
def get_biggest_bar(bar_list):
    bar_list_tmp = sort_by_cells_item(bar_list)
    print(bar_list_tmp[-1])

def get_smallest_bar(bar_list):
    bar_list_tmp = sort_by_cells_item(bar_list)
    print(bar_list_tmp[0])

def get_closest_bar(bar_list, longitude, latitude):
    
    
    return min(bar_list, key=lambda bar: ((bar['Cells']['geoData']['coordinates'][1] - latitude)**2 +\
    (bar['Cells']['geoData']['coordinates'][0] - longitude)**2)**0.5)

if __name__ == '__main__':
    file_path = 'bars.json'
    data = load_data(file_path)
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))

    longitude = float(input("Enter longitude: "))
    latitude = float(input("Enter latitude: "))

    print(get_closest_bar(data, longitude, latitude))
