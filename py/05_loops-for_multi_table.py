# for loop
num = int(input("Enter the no. you want to multiply: ")) # multiplication num that user wants
print(f"this is the multiplication of {num}")
for x in (range(1,13)):
    product = num * x
    print(f"{num} x {x} = {product}")
