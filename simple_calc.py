# dot503 assessment 2 -- for git

class calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def percentage(self, a, b):
        return (a / b) * 100

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("cannot divide by zero")
        return a / b

if __name__ == "__main__":
    calc = calculator()

    print("enter an expression like '1+1', '5-3', '2*3', or '8/2'.\nType 'exit' to quit.")

    while True:
        expression = input("\nenter calculation (or 'exit' to quit): ").strip()

        if expression.lower() == "exit":
            print("exiting...")
            break

        try:
            # multiplication and division -- for intentional error purposes
            if "*" in expression:
                a, b = map(float, expression.split("*"))
                result = calc.multiply(a, b)
            elif "/" in expression:
                a, b = map(float, expression.split("/"))
                result = calc.divide(a, b)
            else:
                result = eval(expression)

            print(f"RESULT: {result}")

        except ValueError as e:
            print(f"ERROR: {e}")
        except Exception as e:
            print(f"INVALID SYNTAX: {e}")

## test passed ##