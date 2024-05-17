try:

    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])
    print(even_numbers[2]/0)

except ZeroDivisionError as e:
    print("Denominator cannot be 0.", e)

except IndexError as e:
    print("Index Out of Bound.", e)

finally:
    print("this block will always print")