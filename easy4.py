#Задача1
list1 = [1, 2, 3, 4]
list2 = [i**2 for i in list1]
print(list2)
#Задача2
fruits1 = ['apple', 'mango', 'banana', 'pear']
fruits2 = ['orange', 'apple', 'pear', 'peach']
fruits3 = [i for i in fruits1 if i in fruits2]
print(fruits3)
#Задача3
num1 = [-6, 6, 12, 234, 399, 482]
num2 = [i for i in num1 if i > 0 and i % 3 == 0 and i % 4 != 0]
print(num2)