# Tree definition

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def replace_leaf(t, old, new):
    """Returns a new tree where every leaf value equal to old has
    been replaced with new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('loki')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        loki
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    prtree=t[:]
    #while tree!=0:
    #for b in branches(prtree):
    if is_leaf(prtree) and prtree[0]==old:
        prtree[0]=new
    return tree(label(prtree),[replace_leaf(b,old,new) for b in branches(prtree)])


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n==2:
        print ("Move the top disk from rod %d to rod %d"%(start, 6-start-end))
        print ("Move the top disk from rod %d to rod %d"%(start, end))
        print ("Move the top disk from rod %d to rod %d"%(6-start-end,end))
    #if n>1:
        #print ("Move the top disk from rod %d to rod %d"%(start, 6-start-end))
    elif n==1:
        print ("Move the top disk from rod %d to rod %d"%(start, end))
    else :
        move_stack(n-1,start,6-start-end)
        move_stack(1,start,end) 
        move_stack(n-1,6-start-end,end)
    #if n==1:
    #    print ("Move the top disk from rod %d to rod %d"%(start, end))


def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""

    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    #print ("p0:",p1)
    #print ("p1:",p2)
    #print ("p2:",p3)
    #print ("p3:",p4)
    #print ("aaaaaa",[min(p1, p2, p3, p4), max(p1, p2, p3, p4)])
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    p1 = lower_bound(x) - lower_bound(y)
    p2 = lower_bound(x) - upper_bound(y)
    p3 = upper_bound(x) - lower_bound(y)
    p4 = upper_bound(x) - upper_bound(y)
    #print ("p0:",p1)
    #print ("p1:",p2)
    #print ("p2:",p3)
    #print ("p3:",p4)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    assert (upper_bound(y)>=0  and lower_bound(y)>=0) or   (upper_bound(y) <=0 and  lower_bound(y)<=0), "AsserttionError"    
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(2, 3) # Replace this line!
    r2 = interval(1, 2) # Replace this line!
    return r1, r2

def multiple_references_explanation():
    return """I agree with her.because r1 and r2 are not numbers,they are intervals.
            When we use par1, it will multiply 2 and 1/5 as the min of mul_interval,
            but actually we do not want to get the min of the mul_interval,we just want to 
            get the correct combination, it should be "2*1/3" and "6*1/5" """

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    min1=lower_bound(x)
    max1=upper_bound(x)
    if a !=0:
        if b/(-2*a)<=max1 and b/(-2*a)>=min1:
            if a>0 and b!=0:
                return interval(c-b*b/(4*a),max(a*max1*max1+b*max1+c,a*min1*min1+b*min1+c))
            elif a<0 and b!=0 :
                return interval(min(a*max1*max1+b*max1+c,a*min1*min1+b*min1+c),c-b*b/(4*a))
        elif b/(-2*a)>max1:
            if a>0:
                return interval(min(a*max1*max1+b*max1+c,a*min1*min1+b*min1+c),max(a*max1*max1+b*max1+c,a*min1*min1+b*min1+c))
            if a<0:
                return interval(min(a*min1*min1+b*min1+c,a*max1*max1+b*max1+c),max(a*max1*max1+b*max1+c,a*min1*min1+b*min1+c))
        else :
            if a>0:
                return interval(min(a*min1*min1+b*min1+c,a*max1*max1+b*max1+c),max(a*max1*max1+b*max1+c,a*min1*min1+b*min1+c))
            if a<0:
                return interval(min(a*max1*max1+b*max1+c,a*min1*min1+b*min1+c),max(a*max1*max1+b*max1+c,a*min1*min1+b*min1+c))
    elif b>0:
            return interval(b*lower_bound(x)+c,b*upper_bound(x)+c)
    else :
            return interval(b*upper_bound(x)+c,b*lower_bound(x)+c)



def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"

