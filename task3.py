# A Harshad number is a positive integer that is divisible by the sum of its own digits.

number = input("Enter the number: ")

def harshad_number(num):
   sum_of_digits = sum(int(i) for i in num)
   return "The number is Harshad" if int(num) % sum_of_digits == 0 else "The number is not Harshad"
     

print(harshad_number(number))
