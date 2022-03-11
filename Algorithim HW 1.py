# Compute sume of digits in all numbers from 1 to n
#n = int(input('Enter your number:'))
result = 0
i = 0
#while i <= n:
  #  result = result + i
   # i+=1

#print(result)


# Find max number

#n1 = int(input('Enter number 1: '))
#n2 = int(input('Enter number 2: '))
#n3 = int(input('Enter number 3: '))
#n_max = max(n1,n2,n3)
#print(f'Max number is: {n_max}')

# Count odd and even numbers
number = int(input('Enter your number:'))
#34560
d_1 = number % 10
d_ten = (number // 10) % 10
d_hun = (number // 100) % 100 % 10
d_thou =  (number // 1000) % 10
d_ten_thou = (number // 10000)
odd_number = 0
even_number = 0

if d_1 % 2:
    odd_number += 1
else: even_number +=1

if d_ten % 2:
    odd_number += 1
else: even_number +=1

if d_hun % 2:
    odd_number += 1
else: even_number += 1

if d_thou % 2:
    odd_number += 1
else: even_number += 1

if d_ten_thou % 2:
    odd_number += 1
else: even_number += 1

print(f'Even numbers: {even_number}, Odd numbers: {odd_number}')


