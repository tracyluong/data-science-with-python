import numpy as np
import pandas as pd
import requests

df_bus = pd.read_csv('data_bus_stop\Potentail_Bust_Stops.csv')

# Set Google API key
#API_KEY = "api_key_here"

# Form a list of addresses for geocoding
# Remove 0 from Street Name (eg: 01ST ST --> 1st ST...) - row 2, 27, 32, 41, 52, 79, 89, 112, 116
df_bus['Street_Two'] = df_bus['Street_Two'].apply(lambda x : x[1:] if x.startswith("0") else x)
# Change the name of street from ANGELOS ALY to ANGELOS ALLEY in order to get correct lat, long of intersection - row 110
df_bus.Street_Two[110] = df_bus.Street_Two[110].replace("ALY","ALLEY")
# Create original input intersection
addresses = (df_bus['Street_One'] + ' AND ' + df_bus['Street_Two'] + ', San Francisco, CA').tolist()

# Write a function to get latitude, longitude for an intersection
def get_google_results(address, api_key):
    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    results = api_response.json()
    
     # If there's no results or an error, return empty results.
    if results['status'] != 'OK':
        output = {
            "status": results['status'],
            "address": address,
            "formatted_address": None,
            "latitude": None,
            "longitude": None,
            "types": None 
        }
    else:    
        output = {
            "status": results['status'],
            "address": address,
            "formatted_address": results['results'][0]['formatted_address'],
            "latitude": results['results'][0]['geometry']['location']['lat'],
            "longitude": results['results'][0]['geometry']['location']['lng'],
            "types": results['results'][0]['types']
        }
    
    return output

# Check whether API key is ok/valid or not
test_result = get_google_results("San Francisco, CA, USA", API_KEY)
if (test_result['status'] != 'OK'):
    print("API key is invalid!")
else:
    # Batch geocoding for all intersections
    # Create a list to hold results
    results = []
    # Go through each address in turn
    total = 0
    for address in addresses:
        geocode_result = get_google_results(address, API_KEY)
        results.append(geocode_result)
        if (geocode_result['status'] == 'OK'):
            total += 1
    
    # Write the full results to csv using the pandas library.
    #pd.DataFrame(results).to_csv('data_bus_stop/Gecoded_Potentail_Bust_Stops.csv', index=False)
    pd.DataFrame(results).to_csv('data_bus_stop/Geocoded_Intersections.csv', index=False)
    # Display the result of geocoding process
    print("Successfully geocoded {0} / {1} addresses".format(total,len(addresses)))
