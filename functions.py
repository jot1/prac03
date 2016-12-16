__author__ = 'jc437345'

"""
def square_number(num):
    return(num * num)
print(square_number(5))

def is_prime(value):
    i = 2
    while i < value:
        remainder = value % i
        if remainder == 0:
            return False
        i += 1
    return True

is_prime(is_prime(5))

#inch to parameter

def inch_to_meter(inch):
    return inch * 0.0254
inch = float(input("enter inches:"))
meter = inch_to_meter(inch)
print("meter:{}".format(meter))
"""""
"======"

tax = 0
def tax_return(income):

    if income > 16000:
     return (income - 16000) * 0.3
income =int(input("enter the income:"))
if tax==0:
    print("no tax")
else:
 print("amount of tax ${}:".format(tax_return(income)))
