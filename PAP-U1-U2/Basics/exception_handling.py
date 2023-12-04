# EXCEPTION HANDLING

# Exception handling is a way to handle errors or exceptional situations in a program. It involves using try, except, and optionally, finally blocks.

try:
    num=int(input("Enter a number:"))
    res=10/num
    print(f"The result is {res}")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Executed")

