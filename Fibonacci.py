
print ("please type in a number:") 
input = int (input ())
f1 = 0
f2 = 1

n = 0

if input <= 0:
    print ("Please enter 1 or higher")
elif input == 1:
    print (f1)
else: 
    while n < input:
        print (f1)
        fib = f1 + f2
        f1 = f2
        f2 = fib
        n +=1

        
  
  
  
  
