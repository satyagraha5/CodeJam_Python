def gcd(a,b):
        if a < b:
            a, b = b, a
        while b > 0:
            a, b = b, a % b
        return a 


def lcm(a,b):
    print("gcd of {} and {} is {}".format(a,b,gcd(a,b)))
    return int((a*b)/gcd(a,b))

if __name__ == "__main__":
    print("lcm of {} and {} is {}".format(1,2,lcm(1,2)))