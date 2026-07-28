a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1
i = 1

while i <= a and i <= b:
    if a / i == int(a / i) and b / i == int(b / i):
        gcd = i
    i = i + 1


lcm = a
while True:
    if lcm / a == int(lcm / a) and lcm / b == int(lcm / b):
        break
    lcm = lcm + 1

print("GCD =", gcd)
print("LCM =", lcm)