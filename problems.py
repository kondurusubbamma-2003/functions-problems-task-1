#1.Write a function to sum all elements in a list
def u_sum(n):
    sum=0
    for x in n:
        sum+=x
    print(sum)
u_sum([10,20,30,40])

#2.Write a function to count uppercase and lowercase letters in a given string
def u_count(n):
    u_count=0
    l_count=0
    for x in n:
        if x.isupper():
            u_count+=1
        elif x.islower():
            l_count+=1
    print(u_count)
    print(l_count)
u_count("pythonAETVC")
#3.Write a function to print the Fibonacci series up to n terms
def u_febonic(n):
    a,b=0,1
    for x in range(n):
        print(a,end=" ")
        a,b=b,a+b
u_febonic(5)
#4.Write a function to count the digits in a given number
def u_digits(n):
    count=0
    for x in str(n):
        count+=1
    print(count)
u_digits(123456)
#5.Write a function to find the largest element in a list
def u_largest(n):
    max=n[0]
    for x in n:
        if x>max:
            max=x
        elif x!=max:
            max=x
    print(max)
u_largest([10,20,30,40])
#6.Write a function to count the even numbers in a list
def u_even(n):
    count=0
    for x in(n):
        if x%2==0:
            count+=1
    print(count)
u_even([2,8,5,3,5,4,9,8,6])
#7.Write a function to remove duplicates from a list
def u_remove(n):
    tem=[]
    for x in n:
        if x not in tem:
            tem.append(x)
    print(tem)
u_remove([19,29,202,20,30,30])
#8.Write a function to find the factorial of a given number
def u_factorial(n):
    fact=1
    for x in range(1,n):
        fact*=x
    print(fact)
u_factorial(8)
#9.Write a function to check if a number is prime
def u_prime(n):
    count=0
    for x in range(1,n):
        if n%x==0:
            count+=1
    if count==1:
        print("prime")
    else:
        print("not prime")
u_prime(8)
#10.Write a function to reverse a given number
def u_reverse(n):
    rev=""
    for x in str(n):
        rev=x+rev;
    print(rev)
u_reverse(1234)
#11.Write a function to check if a number is a palindrome
def u_palindrome(n):
    rev=""
    for x in n:
        rev=x+rev
    if rev==n:
        print("palindrome")
    else:
        print("not palindrome")
u_palindrome("madam")
#12.Write a function to find the sum of digits of a given number
def u_sum(n):
    sum=0
    for x in str(n):
        sum+=int(x)
    print(sum)
u_sum(12345)
     