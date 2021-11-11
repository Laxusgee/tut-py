# Lists
shopping = ['bread', 'yam', 'egg']
print(shopping)

for i in range(len(shopping)):
    print(shopping[i])

print(shopping[-1])
print(shopping[0:2])

shopping.append('plantain')
shopping.insert(1, 'beans')

shopping.remove('beans')
shopping.pop(3)

print(shopping)

m = [[1,2,3], [4, 5,6]]

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j])

name = ['john', 'lisa', 'sujan']
age = [10, 15, 18]
department = ['sales', 'marketing', 'HR']

employees = [name, age, department]
print(employees)
print(employees[0][1])

x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[10,11,12],[13,14,15],[16,17,18]]
result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j] + y[i][j]

print(result)

# Tuples
weekdays = ("monday", "tuesday", "wednessday", "thursday", "friday", "saturday", "sunday")
print(len(weekdays), weekdays)


# Dictionary Keys and Values
movie = {
    "title": "gundam",
    "genre": "anime",
    "year": 1977,
    "rating": 9.8
}

movie['actors'] = ['rock', 'van damm', 'chris patt']

print (len(movie))
print(list(movie.keys()))
print(list(movie.values()))
print(list(movie.items()))

for i in range(len(movie)):
    k = list(movie.keys())[i]
    print(k, ':', movie[k])