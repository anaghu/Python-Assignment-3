n=int(input("enter a number :"))
if n%3==0:
    print("Buzz")
elif n%5==0:
    print("Fizz")
elif n%3==0 and n%5==0:
    print("BuzzFizz")
else:
    print(n)
    
