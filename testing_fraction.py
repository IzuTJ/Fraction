from Fraction import Fraction

n = int(input("Numerator = "))
d = int(input("Denominator = "))

frac1 = Fraction(n, d)

n = int(input("Numerator = "))
d = int(input("Denominator = "))

frac2 = Fraction(n, d)

test_int = int(input("Integer for testing: "))

print(f"\nFirst fraction = {frac1}")
print(f"Second fraction = {frac2}\n")

print(f"{frac1} +  {frac2} = {frac1 + frac2}")
print(f"{frac1} -  {frac2} = {frac1 - frac2}")
print(f"{frac1} *  {frac2} = {frac1 * frac2}")
print(f"{frac1} /  {frac2} = {frac1 / frac2}")

print(f"{frac1} +  {test_int} = {frac1 + test_int}")
print(f"{frac1} -  {test_int} = {frac1 - test_int}")
print(f"{frac1} *  {test_int} = {frac1 * test_int}")
print(f"{frac1} /  {test_int} = {frac1 / test_int}")

print(f"\n{frac1} in lowest terms: {frac1.is_in_lowest_terms()}")
print(f"{frac2} in lowest terms: {frac2.is_in_lowest_terms()}\n")

print(f"Reciprocal of {frac1} is {frac1.reciprocal()}")
print(f"Reciprocal of {frac2} is {frac2.reciprocal()}")

print(f"\n{frac1} expanded by {test_int} = {frac1.expand(test_int)}")
print(f"{frac1} reduced by {test_int} = {frac1.reduce_by(test_int)}\n")

frac1.n = "Hello "
print(frac1)
frac2.n = "World!"
print(frac1 + frac2)
