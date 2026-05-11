# Arithmetic Operator 
a = 11
b = 7

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a % b = ", a % b)
print("a // b = ", a // b)
print("a ** b = ", a ** b)

# Conditional Operators 
print(a>12)
print(a<17)
print(a<=100)
print(a>=1)
print(a==0) 
print(a==11) 
print(a!=17)

# Assignment Operators
k = 15
print(k)
k += 3
print(k)
k -= 3
print(k)
k *= 3
print(k)
k /= 3
print(k)
k **= 3
print(k)

#Comparison Operators

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical Operator

m = 10
n = 20
print(m==n and n==20)
print(m>5 and n<30)
print(m>10 and n<30)
print(m>10 or n<30)
print(not m>100)
print(not m>7)

# Identity Operators (Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal

print(x is not y)

# Membership Operators (Membership operators are used to test if a sequence is presented in an object)
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)
