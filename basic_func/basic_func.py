def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0 or b == 0:
        return False
    else:
        return a / b


def power(base, pow):
    if pow == 0:
        return 1
    else:
        return base ** pow


def square(base):
    if base == 0:
        return False
    else:
        a = base ** 0.5
        return a


def greet(이름="낯선자", 나이=20):
    if 나이 >= 50:
        print(f"안녕하십니까 {이름}!")
    elif 나이 < 20:
        print(f"안녕 {이름}!")
    else:
        print(f"안녕하신가 {이름}!")
    