try :
	count = int(input("Give me a number: "))
except ValueError:
	print("That's not a number!")
	
else:
	print("Hi " * count)
	
	
def add(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        return (num1 + num2)
    except ValueError:
        return None
	