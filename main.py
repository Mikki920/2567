result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a should be greater than or equal to b")
        if b > 100:
            raise IndexError("b should be less than or equal to 100")
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except Exception as e:
        print(f"Exception: {e}")

data = {(10, 2): 2, (2, 5): 5, ("123", 4): 4, (18, 0): 0, ((), 15): 15, (8, 4): 4}

for key in data:
    res = divider(key[0], key[1])
    result.append(res)

print(result)
