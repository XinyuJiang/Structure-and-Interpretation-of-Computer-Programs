def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    def compu(n,a):
        if n==0:
            return 0
        elif n==1:
            return a
        elif n==2:
            return a+a
        elif n==3:
            return a+a+a
        elif n==4:
            return a+a+a+a
        elif n==5:
            return a+a+a+a+a
        elif n==6:
            return a+a+a+a+a+a
        elif n==7:
            return a+a+a+a+a+a+a
        elif n==8:
            return a+a+a+a+a+a+a+a
        elif n==9:
            return a+a+a+a+a+a+a+a+a
        elif n==10:
            return a+a+a+a+a+a+a+a+a+a
        elif n==11:
            return a+a+a+a+a+a+a+a+a+a+a
        else :
            return a+compu(n-1,a)
    return compu(a,b)+c

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    def computgcd(c):
        if a%c==0 and b%c==0:
            return c
        else :return computgcd(c-1)
    return computgcd(min(a,b))

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    def computehail(n,a):
        if n%2==0 :
            print (n//2)
            return computehail(n//2,a+1)
        elif n!=1 :
            print (3*n+1)
            return computehail(3*n+1,a+1)
        else: 
            return a
    print (n)
    return computehail(n,1)
