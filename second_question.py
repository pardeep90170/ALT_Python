# 1. List_Mainuplation
List=[1,2,3,4,5,6,7,8,9,10]
print(f"Create a list of number {List}")
List.insert(0,100)
print(f"Insert the number in begining {List}")
List.extend([11,12,13,14,15])
print(f"Add the number with extend method {List}")
List.remove(3)
List.remove(8)
print(f"Remove the number of list {List}")
print(f"Modified list {List}")

# 2.List_Sorting_and_Reversing
List=["apple","banana","kiwi","orange","grape"]
print(f"Create a word list {List}")
List.sort()
print(f"Alphabetically sorting list {List}")
List.reverse()
print(f"Reverse the sort list {List}")
print(f"Modifies the list {List}")

# 3.List_Count_and_Removal
List=[1,2,3,2,4,2,5,6,2]
print(f"Create a list with duplicates {List}")
Count=List.count(2)
print(f"Count the number 2 in lsit: {Count}")
List.remove(2)
List.remove(2)
List.remove(2)
List.remove(2)
print(f"Remove the value of 2 in list {List}")


# 4.List_of_List
List=[[1,2],[3,4],[5,6],[7,8]]
print(f"Create of list {List}")
list=List[0]
list.extend(List[1])
list.extend(List[2])
list.extend(List[3])
print(f"Flat list in:{list}")

# 5.Unique_elements
List=[1,2,2,3,4,4,5,6,6,6]
print(List.count(1)) #List in the count are one and this item not repeat list
print(List.count(2)) #List in the count are two or more then value and this item are repeat list


# All the list in unique  item in list
New_list=[]
New_list.append(1)
New_list.append(2)
New_list.append(3)
New_list.append(4)
New_list.append(5)
New_list.append(6)
print(New_list)

# 6. Created_a_list_of_tuple
List_of_Tuple=[("alice",85),("bob",92),("eva",78),("david",98)]
print(List_of_Tuple)
List_of_Tuple.sort(key=lambda a:a[1])
print(List_of_Tuple)



# 7. Create two list number
List1=[1,2,3]
List2=[4,5,6]
print(List1,List2)
List1.extend(List2)
print(List1)
print(f"Concatenate the two list {List1}")
Index=List1.index(5)
print(f"Find the index no. {Index}")
List1.insert(2,10)
print(f"Insert the number 10 in list {List1}")
List1.remove(3)
print(f"Remove the number 3 in list {List1}")
Final_list=List1
print(f"Modified list {Final_list}")
