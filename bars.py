import json


def load_data(filepath):
    with open(filepath) as data_file:    
        data = json.load(data_file)

    return data
    

def get_biggest_bar(data):
    data1 = sorted(data, key=lambda k: k['Cells']['SeatsCount'], reverse=False)
    print(data1[-1])

def get_smallest_bar(data):
    data1 = sorted(data, key=lambda k: k['Cells']['SeatsCount'], reverse=False)
    print(data1[0])


def get_closest_bar(data, longitude, latitude):
    distance = 10000;
    
    for bar in data:
        tmp_lat = bar['Cells']['geoData']['coordinates'][0]
        tmp_long = bar['Cells']['geoData']['coordinates'][1]
        tmp_dist = ((tmp_lat - latitude)**2 + (tmp_long - longitude)**2)**0.5
        if distance > tmp_dist:
            distance = tmp_dist
            number = bar['Number']
    
    return [bar for bar in data if bar['Number'] == number]


if __name__ == '__main__':
    pass

data = load_data('bars.json')
print(get_biggest_bar(data))
print(get_smallest_bar(data))

longitude = float(input("Enter longitude: "))
latitude = float(input("Enter latitude: "))

print(get_closest_bar(data, longitude, latitude))

