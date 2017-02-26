## 2. Parsing the File ##

f = open("la_weather.csv", "r")
data = f.read()
rows = data.split('\n')
weather_data = []
for elem in rows:
    split_row = elem.split(',')
    weather_data.append(split_row)


## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for item in weather_data:
    val = item[1]
    weather.append(val)

## 4. Counting the Items in a List ##

count = 0
for items in weather:
    count += 1
print(count)    

## 5. Removing the Header ##

new_weather = weather[1:]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for elem in weather_types:
    result = elem in new_weather
    weather_type_found.append(result)
print(weather_type_found)    