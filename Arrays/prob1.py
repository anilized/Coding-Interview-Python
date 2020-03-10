# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                print([seen[remaining], i])
            seen[v] = i
        return []
a = [2,7,11,15]
twoSum(a, 9)

def moveZeros(arr):
    pos = 0
    for i in range(len(arr)):
        el = arr[i]
        if el != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1
    return arr

arr = [0,2,0,3,4]
print(moveZeros(arr))


def findDuplicate(arr2):
    dic = {}
    for n in arr2:
        if n in dic:
            print(dic) 
            return True
        else: 
            print(dic)
            dic[n] = 1
    return False

b = [1,2,3,1]
print(findDuplicate(b))