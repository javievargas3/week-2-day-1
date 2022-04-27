Write a function that takes in two lists and returns the two lists merged together and sorted
Hint: You can use the .sort() method
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]


test_list1 = [1, 2, 3, 4, 5, 6]
test_list2 = [3, 4, 5, 6, 7, 8, 10]
  

print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))
  
res = sorted(test_list1 + test_list2)
  
print ("The combined sorted list is : " + str(res))

Given a list as a parameter,write a function that returns a list of numbers that are less than ten


For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

a = [1, 11, 14, 5, 8, 9]

for i in a:

    if i < 10:

        print(i)