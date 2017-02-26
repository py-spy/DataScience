## 2. Opening Files ##

a = open("test.txt", "r")
print(a)
f = open("crime_rates.csv","r")

## 3. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()

## 4. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows)

## 6. Practice - Loops ##

ten_rows = rows[0:10]
for x in ten_rows:
    print(x)

## 8. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data = []
for x in rows:
    split = x.split(',')
    final_data.append(split)
print(final_data[0:5])    
    

## 9. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)
cities_list = []
cities_list.append(five_elements[0][0])
cities_list.append(five_elements[1][0])
cities_list.append(five_elements[2][0])
cities_list.append(five_elements[3][0])
cities_list.append(five_elements[4][0])
print (cities_list) 

## 10. Looping Through a List of Lists ##

crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
cities_list = []
for cursor in final_data:
    city_name = cursor[0]
    cities_list.append(city_name)

## 11. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
int_crime_rates = []
for x in rows:
    split_data = x.split(',')
    converted = int(split_data[1])
    int_crime_rates.append(converted)