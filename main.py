from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
place = input("Enter a location: ")
location = geolocator.geocode(place)
print(location)