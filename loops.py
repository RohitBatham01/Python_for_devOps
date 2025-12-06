# list --> Data Structure which can hold multiples values of same type or different type
# list is ordered --> we can access the values using index

# array --> Data Structure which can hold multiples values of same type only

list_of_cloud=["AWS","Azure","GCP","Oracle","IBM"]
print(list_of_cloud)  # print the complete list


#add a new cloud provider to the list

list_of_cloud.append("Digital Ocean")  # add a new value to the list
print(list_of_cloud)  # print the updated list

#inserting a value at specific index

list_of_cloud.insert(0,"Heroku")  # insert a new value at index 0
print(list_of_cloud)  # print the updated list

# length of the list
print(len(list_of_cloud))  # print the length of the list

# iterate through the list and print each value
for cloud in list_of_cloud:
    print(cloud)

for i in range(0,5):
    print(i)