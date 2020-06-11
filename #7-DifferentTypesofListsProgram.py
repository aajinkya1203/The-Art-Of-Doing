num_strings = [ "15", "100", "55", "42" ]
num_int = [ 15, 100, 55, 42 ]
num_float = [ 2.2, 8.09, 23.4, 9.69 ]
num_lists = [[1,2,3], [4,5,6], [7,8,9]]

allLists = [num_strings, num_int, num_float, num_lists]

for count,item in enumerate(allLists, start=1):
    print("\n\nYour variable",count,"is a",type(item))
    print("It contains the elements:",item)
    print(f"The element {item[0]} is a",type(item[0]))