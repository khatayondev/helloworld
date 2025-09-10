def even(x , y):
   
    evennum = x
    while(evennum < x-2):
        evennum = evennum + 2
    print (evennum)

    oddnum = x
    while(oddnum < x-1):
        oddnum = oddnum + 2
    print (evennum)

    if x % 2 == 0:
        return evennum
    else:
        return oddnum
    

mylist = even()
print(f"this list is {mylist} ended");