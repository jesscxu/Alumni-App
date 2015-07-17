import rauth, json, requests

def get_search_parameters(category, location, num_results):
    params = {}
    params['category_filter'] = category
    params['location'] = location
    params['limit'] = num_results
    return params

def get_results(params):
    #Obtain these from Yelp's manage access page
    consumer_key = 'quwpaOnMXbqhZ6uFNp-KFQ' # "YOUR_KEY"
    consumer_secret = 'HrEugLT9be6Aj_Xodc0akAAg0Mk' # "YOUR_SECRET"
    token = '3MF7TVz0-K8RlDvyjHGIUhGPBQYBAVrw' # "YOUR_TOKEN"
    token_secret = '0EyNq7eHSwSzPtO5FjzUI9Ynmg0' # "YOUR_TOKEN_SECRET"

    session = rauth.OAuth1Session(
    consumer_key = consumer_key
    ,consumer_secret = consumer_secret
    ,access_token = token
    ,access_token_secret = token_secret)
     
    request = session.get("http://api.yelp.com/v2/search",params=params)

    #Transforms the JSON API response into a Python dictionary
    data = request.json()
    session.close()

    return data

def get_multiple_results(params):
    parameters = get_search_parameters('pizza', 'San Francisco, CA', 20)
    data = get_results(parameters)
    # print(data)

    data_set = []
    info = data['businesses']
    # for i in range(len(info)):
    #     data_set.append({'name': info[i]['name'], 'location': info[i]['location']})

    for i in range(len(info)):
        data_set.append({'name': info[i]['name'], 
                        'address': info[i]['location']['address'][0],
                        'latitude': info[i]['location']['coordinate']['latitude'], 
                        'longitude': info[i]['location']['coordinate']['longitude']})

    # print(data_set)

    with open ('yelp_api.json', 'w') as outfile:
        json.dump(data_set, outfile, indent=4)
    
    return data_set


def main():
    parameters_1 = get_search_parameters('pizza', 'CA', 20)
    data_1 = get_results(parameters_1)

    parameters_2 = get_search_parameters('icecream', 'OH', 20)
    data_2 = get_results(parameters_2)
    

    data_set = []
    info_1 = data_1['businesses']
    info_2 = data_2['businesses']
    # for i in range(len(info)):
    #     data_set.append({'name': info[i]['name'], 'location': info[i]['location']})

    for i in range(len(info_1)):
        if info_1[i]['location']['address'] != [] and info_2[i]['location']['address'] != []:
            data_set.append({'name': info_1[i]['name'], 
                            'address': info_1[i]['location']['address'][0],
                            'latitude': info_1[i]['location']['coordinate']['latitude'], 
                            'longitude': info_1[i]['location']['coordinate']['longitude']})
            data_set.append({'name': info_2[i]['name'], 
                            'address': info_2[i]['location']['address'][0],
                            'latitude': info_2[i]['location']['coordinate']['latitude'], 
                            'longitude': info_2[i]['location']['coordinate']['longitude']})

    # print(data_set)

    with open ('yelp_api.json', 'w') as outfile:
        json.dump(data_set, outfile, indent=4)

    # Create the fixture for Django to load data automatically.

    # fixture_data = []
    # counter = 1
    # for i in range(len(data_set)):
    #     fixture_data.append({'model': 'alumni.name', 'pk': counter, 'fields': {
    #         'name_text': data_set[i]['name']}})
    #     fixture_data.append({'model': 'alumni.address', 'pk': counter + 1, 'fields': {
    #         'address_text': data_set[i]['address'],
    #         'name': counter,
    #         'lat': data_set[i]['latitude'],
    #         'lon': data_set[i]['longitude']
    #         }})
    #     counter += 2

    # with open ('fixture_data.json', 'w') as outfile:
    #     json.dump(fixture_data, outfile, indent=4)

    fixture_data = []
    for i in range(len(data_set)):
        fixture_data.append({'model': 'alumni.name', 'pk': i + 1, 'fields': {
            'name_text': data_set[i]['name'],
            'address_text': data_set[i]['address'],
            'lat': data_set[i]['latitude'],
            'lon': data_set[i]['longitude']
            }})

    with open ('fixture_data.json', 'w') as outfile:
        json.dump(fixture_data, outfile, indent=4)



    latlon_points = []
    for i in range(len(data_set)):
        latlon_points.append( [data_set[i]['longitude'], data_set[i]['latitude']] )

    with open ('latlon.json', 'w') as outfile:
        json.dump(latlon_points, outfile, indent=4)






###########################################################
    google_data = []
    all_data = []

    for i in range(len(latlon_points)):
        google_address = requests.get('http://maps.googleapis.com/maps/api/geocode/json?latlng=' + 
                        str(latlon_points[i][1]) + ',' + str(latlon_points[i][0])).json()['results'][0]['formatted_address']
        city = google_address.split(',')[-3].strip()
        state = google_address.split(',')[-2].split(' ')[1]

        all_data.append({
            'name': data_set[i]['name'],
            'address': city + ', ' + state,
            'coordinates': latlon_points[i]
            })





    with open ('data.json', 'w') as outfile:
        json.dump(all_data, outfile, indent=4)

    return 



if __name__ == '__main__':
    main()