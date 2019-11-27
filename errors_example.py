def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Dividor can NOT be ZERO.")
    return dividend / divisor


studants = [
    {'name': "Wayne", "grades": [100,90]},
    {'name': "Muriel", "grades": []}, # Error here.
    {'name': "Shaggy", "grades": [70,80]}
]

print("Wellcome to the average program.")
try:
    for studant in studants:
        name = studant['name']
        grades = studant['grades']
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All students averages calculated --")
finally:
    print("-- End of students average calculation --")
