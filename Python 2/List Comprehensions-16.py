## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for item, ship in enumerate(ships):
    print(ship)
    print(cars[item])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for item, elem in enumerate(things):
    elem.append(trees[item])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [(item * 2) for item in apple_prices]
apple_prices_lowered = [(item - 100) for item in apple_prices]

## 5. Counting Female Names ##

name_counts = {}
for item in legislators:
    if item[3] == 'F' and item[7] > 1940:
        name = item[1]
        if name in name_counts:
            name_counts[name] = name_counts[name] + 1
        else:
            name_counts[name] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
checks = [item is not None and item>30 for item in values]
    

## 8. Highest Female Name Count ##

max_value = None
for items in name_counts:
    count = name_counts[items]
    if max_value is None or count > max_value:
        max_value = count


## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for a,b in plant_types.items():
    print(a)
    print(b)

## 10. Finding the Most Common Female Names ##

top_female_names = []
top_female_names = [x for x in name_counts if name_counts[x] ==2]

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts = {}
for item in legislators:
    if item[3] == 'M' and item[7] > 1940:
        name = item[1]
        if name in male_name_counts:
            male_name_counts[name] = male_name_counts[name] +1
        else:
            male_name_counts[name] = 1
highest_value = None
for name,count in male_name_counts.items():
    if highest_value is None or count > highest_value:
        highest_value = count

for name,count in male_name_counts.items():
    if count == highest_value:
        top_male_names.append(name)
