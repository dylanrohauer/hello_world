# function test
def math_ops(num1, num2):
    sum = num1 + num2
    print(f"This is the sum of {num1} and {num2}: {sum}.")
    difference = num1 - num2
    print(f"This is the difference between {num1} and {num2}: {difference}.")
    product = num1 * num2
    print(f"This is the product of {num1} and {num2}: {product}.")
    quotient = num1 / num2
    print(f"This is the quotient of {num1} over {num2}: {quotient}.")
    return(sum, difference, product, quotient)

n1 = float(input("What's your favorite number? "))
n2 = float(input("What's your second favorite number? "))

add, subtract, multiply, divide = math_ops(n1, n2)

print(f"Now if we take the sum({add}) and the product({multiply})...")
print("We can find the same operations for those!")

input("Press Enter <<< ")

math_ops(add, multiply)
