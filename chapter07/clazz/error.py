class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise


while True:
    try:
        x = int(input("Enter the first number: "))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x/y is', value)
    except Exception as e:
        print('Invalid input:', e)
        print('Invalid input.Please try again.')
    else:
        break
