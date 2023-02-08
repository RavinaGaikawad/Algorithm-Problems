print("Introduction to Python List!")

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
additional_fruits = ['lychee', 'watermelon']

print("Append")
fruits.append('grape')
print(fruits)
print()

print("Extend")
fruits.extend(additional_fruits)
print(fruits)
print()

print("Insert")
fruits.insert(0, 'mango')
print(fruits)
print()

print("Remove")
fruits.remove('pear')
print(fruits)
print()

print("Pop")
print(fruits.pop(1))
print(fruits)
print()

print("Count")
print(fruits.count('apple'))
print()

print("Sort")
fruits.sort()
print(fruits)
print()

print("Reverse")
fruits.reverse()
print(fruits)
print()

print("Copy")
new_list = fruits.copy()
print(new_list)
print()

new_list.clear()
print("Clear")
print(new_list)
print(fruits)
print()


### Stack
print('List as Stack')
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)
print()

### Queue
print('List as Queue')
queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)

queue.pop(0)
print(queue)

queue.pop(0)
print(queue)
