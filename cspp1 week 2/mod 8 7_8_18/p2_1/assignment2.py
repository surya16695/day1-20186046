# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    i = 0
    b = a
    while i <= length(b):
        sum = b[i] + sumofdigits(b[i+1])
        i += 1
    return sum

def main():
    a = input()
    print(sumofdigits(int(a)))  

if __name__ == "__main__":
    main()

