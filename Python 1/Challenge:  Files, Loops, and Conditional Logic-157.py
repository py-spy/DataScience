## 3. Read the File Into a String ##

f = open("dq_unisex_names.csv", "r")
names = f.read()         

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
#nested list code
nested_list = []
for elem in names_list:
    comma_list = elem.split(',')
    nested_list.append(comma_list)
print(nested_list[0:5])

## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list = []
for elem in nested_list:
    x = elem[0]
    y = float(elem[1])
    new_list = [x,y]
    numerical_list.append(new_list)

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for elem in numerical_list:   
    if (elem[1] >=1000):
        thousand_or_greater.append(elem[0])
print(thousand_or_greater[0:10])        