# A variable will be printed, as long as the number of variables in the list.
# The i stands for the number of variables in the list.
# By using the for loop, each variable will be printed, as long as the list is NOT finished. 
# When the last variable of the list is printed, the printing will stop because of the use of the for loop.


namen = [ 'Fadi', 'Ahmed' ,'Victor', 'Marieke']
for i in namen:
    print (i)


for i in range(10):
    print(i)

# By using the value x=5, the outcome can be changed through a formula
# 1 becomes 5, 2 becomes 10 etc.
# the first value is the 0, so the first result will be a zero. 
# the last value will be 45 (9*5)

x=5
for i in range(10): 
    print(i*5)
