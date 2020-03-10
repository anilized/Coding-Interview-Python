"""
   #
  ##
 ###
####

for right allign 1st -> print n-1 " "
for right allign 2nd -> print n-2 " "
for right allign 3st -> print n-3 " "
for right allign 4th -> print n-4 " "

"""

counter = 0
sq_counter = 0
def stairCase(n):
    e = ' '
    square = '#'
    global counter
    global sq_counter
    if counter < n and sq_counter <= n:
        counter += 1
        sq_counter += 1
        print(e * (n-counter) + sq_counter * square)
        return stairCase(n)

stairCase