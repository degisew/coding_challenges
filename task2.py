# n is Deficient, if the sum of its proper divisors is less than n.
# n is Abundant, >>   >>         >>   >>            greater than n.
# n is Perfect,  >>   >>         >>   >>            equal to n.

number = int(input("Enter the number: "))

def classify_number(number):
    sum_of_divisors = sum(num for num in range(1, number) if number % num == 0)
    classifn = {
        sum_of_divisors > number: "Abundant",
        sum_of_divisors < number: "Deficient",
        sum_of_divisors == number: "Perfect"
    }
    return classifn[True]
    
print(classify_number(number))
