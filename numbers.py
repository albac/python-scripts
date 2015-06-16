# Test code to input a N number and return a sequence from 1 to N, and print Fizz if multiple of 3, Buzz multiple of 5 and FizzBuzz if both
# Enter your code here. Read input from STDIN. Print output to STDOUT
def multiple_three(i):
    number = int(i)
    if number%3 == 0:
        return True
    return False 
    
def multiple_five(i):
    number = int(i)
    if number%5 == 0:
        return True
    return False
  
def numbers(n):
    for i in range(1,n):
        if multiple_three(i) and multiple_five(i):
            print "FizzBuzz"
        elif multiple_three(i):
            print "Fizz"
        elif multiple_five(i):
            print "Buzz"
        else:
            print i
        
n = int(raw_input('Enter number: '))
numbers(n+1)
