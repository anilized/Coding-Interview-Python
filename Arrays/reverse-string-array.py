# Create a function that reverses a string:
# 'Hi My name is Anıl' should be:
# 'lınA si eman yM iH'

# def reverse(text):
#    text = text[::-1]
#    print(text)

# reverse("Hi My name is Anıl")

def reverse_string(text):
    mylist = []
    for i in range(len(text)-1,-1,-1): # 8. indexten 1 azaltarak geri doğru
        mylist.append(text[i])
    return ''.join(mylist)

x=reverse_string("I am anıl")
print(len("I am anıl"))
print(x)

test = ['a', 'b', 'c', 'd']
for i in range(len(test)-1,-1,-1):
    print(test[i])
