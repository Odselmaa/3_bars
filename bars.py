import json
import os


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)


def get_biggest_bar(bar_list):
    return bar_list[-1]


def get_smallest_bar(bar_list):
    return bar_list[0]


def get_closest_bar(bar_list, longitude, latitude):
    return min(
                bar_list,
                key=lambda bar:
                get_distance(
                            bar['Cells']['geoData']['coordinates'][1],
                            latitude,
                            bar['Cells']['geoData']['coordinates'][0],
                            longitude))


def get_bar_seat(bar):
    return bar['Cells']['SeatsCount']


def sort_by_cells_item(bar_list):
    return sorted(bar_list, key = get_bar_seat, reverse=False)


def get_name(bar):
    return bar["Cells"]["Name"]


def get_address(bar):
    return bar["Cells"]["Address"]


def get_distance(long1, lat1, long2, lat2):
    return ((long1 - long2)**2 + (lat1 - lat2)**2)**0.5


if __name__ == '__main__':

    file_path = input("Enter file path: ")
    data = load_data(file_path)
    data = sort_by_cells_item(data)
    smallest_bar = get_smallest_bar(data)
    biggest_bar = get_biggest_bar(data)
    print("\nBiggest bar in Moscow is: '%s', %s" % (
                get_name(biggest_bar),
                get_address(biggest_bar)))
    print("Smallest bar in Moscow is: '%s', %s" % (
                get_name(smallest_bar),
                get_address(smallest_bar)))
    print("\nDo you want to find where is closest bar?")
    longitude = float(input("Enter longitude: "))
    latitude = float(input("Enter latitude: "))
    closest_bar = get_closest_bar(data, longitude, latitude)
    print("Closest bar is : '%s', %s" % (get_name(closest_bar),
                                        get_address(closest_bar)))

