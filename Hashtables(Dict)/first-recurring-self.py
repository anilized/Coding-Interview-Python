# Given an array = [2,5,1,2,3,5,1,2,4]
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# It should return 1

# Given an array = [2,3,4,5]
# It should return undefined

# Which repeated first!!

def func(mylist):
    for i in range(0,len(mylist)):
        for j in range(i+1, len(mylist)):
            if mylist[i] == mylist[j]:
                return mylist[i]
    return 0

#   O(n^2)

x = [2,1,1,2,3,5,1,2,4]
print(func(x))

def hashtable(mylist):
    mydict = {}
    for i in range(len(mylist)):
        if mylist[i] in mydict:
            return mylist[i]
        else:
            mydict[mylist[i]]=i
    return 0
x = [2,1,1,2,3,5,1,2,4]
print(hashtable(x))

#   O(n)