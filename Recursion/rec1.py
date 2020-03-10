counter = 0
def inception():
    global counter
    print(counter)
    if (counter >= 3):
        return 'done'
    counter += 1
    return inception()

print(inception())

def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)

print(factorial(5))