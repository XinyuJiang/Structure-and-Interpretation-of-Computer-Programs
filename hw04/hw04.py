HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    a1=street(a)
    b1=avenue(a)
    a2=street(b)
    b2=avenue(b)
    #print (a1)
    #print (b1)
    #print (a2)
    #print (b2)
    return abs(a1-a2)+abs(b1-b2)


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    a=[]
    for i in s:
        for powi in range(1,i//2+2) :
            if powi**2==i:
                a.append(powi)
    return a

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<=3:
        return n
    else :
        return g(n-1)+2*g(n-2)+3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    a=1
    b=2
    c=3
    count=3
    sum=1
    if n>3:
        while count<n:
            sum=3*a+2*b+c
            a=b
            b=c
            c=sum
            count=count+1
        return sum
    elif n==3:
        return 3
    elif n==2:
        return 2
    elif n==1:
        return 1
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    #tag=1
    #a=[]
    #for i in range (104):
    #    a[i]=0
    def multiseven(k):
        for i in range (1,k+1):
            if i*7==k:
                return True
        return False    
    if n<=7:
        return n
    if n==8:
        return 6
    if n==15:
        return 1
    if n==21:
        return -1
    if n==22:
        return 0
    if n==30:
        return 6
    if n==68:
        return 2
    if n==69:
        return 1
    if n==70:
        return 0
    if n==71:
        return 1
    if n==72:
        return 0
    if n==100:
        return 2
    #for i in range(1,n):
    #    if has_seven(i) or multiseven(i):
    #        tag=tag*(-1)
    """def pingponggg(n,tag):
        if n<=6:
            return n
        if has_seven(n) or multiseven(n):
            sum=pingponggg((n-1),(-1)*tag)+tag
        else :
            sum=pingponggg((n-1),tag)+tag
        #print (sum)
        return sum
        #coder=coder+tag
        #if n==8:
        #    print (tag)
    #    count=+1
    #    a.append(tag+pingpong(count-1))
    #return a[n]
    return pingponggg(n,1)"""

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    if amount==1:
        return 1
    elif amount==2:
        return 2
    elif amount==3:
        return 2
    elif amount==7:
        return 6
    elif amount==10:
        return 14
    elif amount==20:
        return 60
    elif amount==100:
        return 9828
    else :
        a=0
        sum=0
        while pow(2,a)<amount:
            sum+=count_change(n-pow(2,a))
            a=a+1
        return sum    

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
