# exception = an event that interrupts the flow of a program
#   (zeroDivisionError, TypeError, ValueError)
#   1. try, 2. except, 3. finally

try:    
    number = int(input('Enter a number: '))
    print(1 / number)
except ZeroDivisionError:
    print('You can’t divide by zero, idiot!')
except ValueError:
    print('Enter only numbers please!')
except Exception:
    print('Something went wrong')
finally:
    print('do some cleanup here')
