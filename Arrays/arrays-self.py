strings= ['a', 'b', 'c', 'd']

print(strings[2])

strings.append('e')

strings.pop() # O(1)
strings.pop() # O(1)

# add first element

strings.insert(0,'x') # O(n)

# splice

strings.insert(2,'alien') # O(n)

print(strings)
