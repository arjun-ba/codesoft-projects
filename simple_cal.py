
print("\n ----*SIMPLE CALCULATOR*----\n")
num1=float(input("Enter The First Number:"))
operator=str(input("Enter The Opeartor(+,-,*,/,%):"))
num2=float(input("Enter The Second Number:"))

if operator == '+':
    print(f"\nThe Result\n{num1} + {num2} =",num1+num2)
elif operator == '-':
    print(f"\nThe Result\n{num1} - {num2}=",num1-num2)
elif operator == '*':
    print(f"\nThe Result\n{num1} * {num2} =",num1*num2)   
elif operator == '/':
    print(f"\nThe Result\n{num1} / {num2} =",num1/num2)
elif operator == '%':
    print(f"\nThe Result\n{num1} % {num2} =",num1%num2)
else:
    print("the operator is invalid...try again")



