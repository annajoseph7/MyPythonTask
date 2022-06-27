def Solution(S, V):   #function accepting 2 arguments(S as R and V as V)
    a_min = b_min = balance = 0 #initializing the variables
    for receiver, amount in zip(S, V): #iterate over 2 lists at same time
        if receiver == 'A': #if the receiver is A
            balance += amount   #add the amount of balance
            b_min = min(-balance, b_min) #if the balance is -tive ,the minimun amount is the amount
        else: #if the receiver is B
            balance -= amount #subtract the amount from the balance
            a_min = min(balance, a_min) #if the balance is +tive, then the minimum amount is the amount
    return [-a_min, -b_min] #return the minimum amount to each

#Test 1
a = Solution('BAABA', [2, 4, 1, 1, 2]) #calling funct with 2 arg(S,V)
print(a)
#Test 2
b = Solution('B', [100])
print(b)
#Test 3
c = Solution('ABAB', [10, 5, 10, 15])
print(c)

