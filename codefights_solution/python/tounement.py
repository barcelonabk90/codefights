'''
As an economist, you are interested in Pingland PING to Pongland PONG currency chart. 
In a conference that will take place really soon, you want to show everyone that PING/PONG rate has been increasing lately. 
In order to do this you decided to remove from the chart some points so that the remaining points form a strictly increasing sequence. 
Find the smallest number of points you have to remove.
Example
For chart = [3, 2, 6, 4, 5, 1, 7], the output should be
chartFix(chart) = 3.
After you remove points 2, 6, and 1 the remaining points will form a sequence [3, 4, 5, 7], which is strictly increasing. Check out the image below for better understanding:
'''
def chartFix(chart):
    n = len(chart)
    arr = [1] * n
    for i in range(n):
        for j in range(i):
            if chart[i] > chart[j]:
                arr[i] = max(arr[i], arr[j] + 1)
    return n - max(arr)

def chartFix(chart):
    toRemove = []
    for i in range(len(chart)):
        cur = i
        for j in range(i):
            if chart[j] < chart[i]:
                cur = min(cur, toRemove[j] + i - j - 1)
        toRemove.append(cur)
    res = float('inf')
    for i in range(len(toRemove)):
        res = min(res, toRemove[len(toRemove) - i - 1] + i)
    return res



'''
Given a string, find the shortest possible string which can be achieved by adding characters 
to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
'''
def buildPalindrome(st):
    if st[::-1] == st:
        return st
    for i in range(0, len(st)):
        tmp = st[0:i]
        r = st[0:len(st)] + tmp[::-1]
        if r[::-1] == r:
            break
    return r


'''
You've intercepted an encrypted message, and you are really curious about its contents.
You were able to find out that the message initially contained only lowercase English letters, 
and was encrypted with the following cipher:

Let all letters from 'a' to 'z' correspond to the numbers from 0 to 25, respectively.
The number corresponding to the ith letter of the encrypted message is then equal to 
the sum of numbers corresponding to the first i letters of the initial unencrypted message modulo 26.
Now that you know how the message was encrypted, implement the algorithm to decipher it.

Example

For message = "taiaiaertkixquxjnfxxdh", the output should be
cipher26(message) = "thisisencryptedmessage".

The initial message "thisisencryptedmessage" was encrypted as follows:

letter 0: t -> 19 -> t;
letter 1: th -> (19 + 7) % 26 -> 0 -> a;
letter 2: thi -> (19 + 7 + 8) % 26 -> 8 -> i;
etc.
'''
def cipher26(m):
    r = ''
    c = 0
    pre = 0 
    for i in range(len(m)):
        tmp = ord(m[i]) - 97 
        c = tmp - pre
        if c < 0:
            c += 26 
        r += chr(97 + c)
        pre = tmp
    return r



'''
You've got a role in TV series "The Walking Dead"!
Now you are trying to crack a safe with a gun, which you need to survive, zombies are very close.
But you see a note on the safe. It says that the password is a full square or a full cube. 
Also there is the number on this note. 
You should determine how many variants are there to rearrange the digits of the number to make a correct password. 
If the given number is already a full square or a full cube, you should just add this variant of rearranging to the answer.

Example

For number = 414, the output should be
fullSquareOrCude(number) = 2.
You can get numbers 144, which is a full square of 12, and 441, which is a full square of 21.
For number = 64, the output should be
fullSquareOrCube(number) = 1.
The number 64 is a full square of 8 and a full cube of 4.
For number = 71, the output should be
fullSquareOrCube(number) = 0.
71 and 17 aren't full squares or full cubes.
'''
from itertools import permutations
def fullSquareOrCube(number):
    arr = []
    res = 0
    for p in permutations(list(str(number))):
        y = int(''.join(p))
        for x in range(y + 1):
            if x ** 2 == y or x ** 3 == y:
                if y not in arr:
                    arr += [y]
                    res += 1
                    break
    return res



'''
You are given an n × m matrix, which contains all the integers from 1 to n * m, inclusive, each exactly once.

Initially you are standing in the cell containing the number 1. 
On each turn you are allowed to move to an adjacent cell, i.e. 
to a cell that shares a common side with the one you are standing on now. 
It is prohibited to visit any cell more than once.

Check if it is possible to visit all the cells of the matrix in the order of increasing numbers in the cells, 
i.e. get to the cell with the number 2 on the first turn, then move to 3, etc.

Example

For

matrix = [[1, 4, 5], 
          [2, 3, 6]]
the output should be
findPath(matrix) = true;

For

matrix = [[1, 3, 6], 
          [2, 4, 5]]
the output should be
findPath(matrix) = false.
'''

def findPath(a):
    m = len(a)
    n = len(a[0])
    for i in range(m):
        for j in range(n):
            if a[i][j] == 1:
                x = i
                y = j
    for i in range(2, n * m + 1):
        c = 0
        for j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            u = x + j[0]
            v = y + j[1]
            if 0 <= u < m and 0 <= v < n and a[u][v] == i:
                c = 1
                break
        if c:
            x = u
            y = v
        else:
            return 0 
    return 1

def findPath(m):
    M = sum(m, [])
    I = M.index
    return {abs(I(n) - I(n-1 or 2)) for n in M} <= {1, len(m[0])}
          

'''
A step(x) operation works like this: 
it changes a number x into x - s(x), where s(x) is the sum of x's digits. 
You like applying functions to numbers, so given the number n, 
you decide to build a decreasing sequence of numbers: n, step(n), step(step(n)), etc., with 0 as the last element.

Building a single sequence isn't enough for you, 
so you replace all elements of the sequence with the sums of their digits (s(x)). 
Now you're curious as to which number appears in the new sequence most often. 
If there are several answers, return the maximal one.

Example

For n = 88, the output should be
mostFrequentDigitSum(n) = 9.

Here is the first sequence you built: 88, 72, 63, 54, 45, 36, 27, 18, 9, 0;
And here is s(x) for each of its elements: 16, 9, 9, 9, 9, 9, 9, 9, 9, 0.
As you can see, the most frequent number in the second sequence is 9.

For n = 8, the output should be
mostFrequentDigitSum(n) = 8.

At first you built the following sequence: 8, 0
s(x) for each of its elements is: 8, 0
As you can see, the answer is 8 (it appears as often as 0, but is greater than it).
'''
def mostFrequentDigitSum(n):
    
    def f(a):
        r = 0
        while a:
            r += a % 10 
            a //= 10
        return r
    arr = 100 * [0]
    while n:
        arr[f(n)] += 1
        n = n - f(n)
    m = max(arr)
    return len(arr) - arr[::-1].index(m) -1



'''
You've got a role in TV series "The Walking Dead"!
Now you are trying to crack a safe with a gun, which you need to survive, 
zombies are very close. But you see a note on the safe.
It says that the password is a full square or a full cube. Also there is the number on this note. 
You should determine how many variants are there to rearrange the digits of the number to make a correct password. 
If the given number is already a full square or a full cube, you should just add this variant of rearranging to the answer.

Example

For number = 414, the output should be
fullSquareOrCude(number) = 2.
You can get numbers 144, which is a full square of 12, and 441, which is a full square of 21.
For number = 64, the output should be
fullSquareOrCube(number) = 1.
The number 64 is a full square of 8 and a full cube of 4.
For number = 71, the output should be
fullSquareOrCube(number) = 0.
71 and 17 aren't full squares or full cubes.
[time limit] 4000ms (py3)
[input] integer number

An integer, number on the note.  0 ≤ number < 1000.

[output] integer

The number of variants to rearrange digits of the number to get a full square or a full cube.
'''
def fullSquareOrCube(number):
    from itertools import permutations
    n = list(set(permutations(str(number))))
    r = 0
    for x in n:
        x = int("".join(x))
        if f(x):
            r += 1
    return r
def f(a):
    i = 1
    while i * i <= a:
        if i ** 2 == a or i ** 3 == a:
            return 1
        i += 1
    return 0



'''
In this problem, the product of the elements of an arbitrary array x is expressed as p(x).

You are given an array of integers a. 
Any array that you can obtain from a by removing some elements (possibly none, but not all) is denoted as s. 
Among all such arrays s, what is the maximum possible value of p(s)? 
Since the answer could potentially be very large, return the value of p(a) / p(s) instead.

Example

For a = [1, 2, -2, -3, 3, 5], the output should be
maximumSubsetProduct(a) = 1.

Consider s = a (no elements were removed from the original array): p(s) = 1 · 2 · (-2) · (-3) · 3 · 5 = 180. 
There is no other s that has elements with a product larger than that. In this case, p(a) = p(s), therefore p(a) / p(s) = 1.

For a = [10, -10], the output should be
maximumSubsetProduct(a) = -10.

p(a) = -100. For s = [10], p(s) = 10. p(s) cannot be any larger. Thus, the answer is p(a) / p(s) = -100 / 10 = -10.
'''
def maximumSubsetProduct(a):
    c = 0
    r = 0
    for i in a:
        if i < 0:
            if c == 0:
                r = i
            else:
                r = max(r, i)
            c += 1    
    if c % 2 == 0 or len(a) == 1:
        return 1
    return r

'''
Remove all characters from a given string that appear more than once in it.

Example
For str = "zaabcbd", the output should be
removeDuplicateCharacters(str) = "zcd".
'''
def removeDuplicateCharacters(a):
    r = ''
    for x in a:
        if a.count(x) == 1:
            r += x
    return r


'''
Given the prefix sums of some array A, return suffix sums for the same array, i.e. an array B that:

B[0] = A[0] + A[1] + A[2] + ... + A[n - 1]
B[1] =        A[1] + A[2] + ... + A[n - 1]
...
B[n - 2] =             A[n - 2] + A[n - 1]
B[n - 1] =                        A[n - 1]
Example

For prefixSums = [1, 3, 6, 10, 15], the output should be
prefixSumsToSuffixSums(prefixSums) = [15, 14, 12, 9, 5].

You may verify that the initial array A is [1, 2, 3, 4, 5] (just try to calculate the prefix and suffix sums for it).
'''
def prefixSumsToSuffixSums(s):
    s = s[::-1]
    r = [0]
    for i in range(1, len(s)):
        r.append(r[-1] + s[i-1] - s[i])
    r += [s[0]]
    return r[1:][::-1]



'''
The algorithm must replace the first digit in a string with '#' character.

It's guaranteed that the input string contains at least one digit.

Example

For input = "There are 12 points", the output should be
replaceFirstDigitRegExp(input) = "There are #2 points".
'''
def replaceFirstDigitRegExp(inputString):

    return re.sub('[0-9]', '#', inputString, count=1)


'''
Proper nouns always begin with a capital letter, followed by small letters.

Correct a given proper noun so that it fits this statement.

Example

For noun = "pARiS", the output should be
properNounCorrection(noun) = "Paris";
For noun = "John", the output should be
properNounCorrection(noun) = "John".
'''
def properNounCorrection(noun):
    return noun.title()

'''
Given integers l and r, 
find the number of trailing zeros in the decimal 
representation of l! * (l + 1)! * ... * r! (the exclamation mark means factorial).

Example

For l = 4 and r = 10, the output should be
factorialsProductTrailingZeros(l, r) = 7.
'''
def factorialsProductTrailingZeros(l, r):
    res = 0
    c = 0
    for i in range(1, r + 1):
        tmp = i 
        while tmp % 5 == 0:
            c += 1
            tmp //= 5
        if i >= l:
            res += c 
    return res

from math import factorial
from functools import reduce


def factorialsProductTrailingZeros(l, r):
    s = str(reduce(int.__mul__, map(factorial, range(l, r + 1))))
    s0 = s.rstrip('0')
    return len(s) - len(s0)



'''
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
'''
def arrayMaxConsecutiveSum(a, k):
    l = len(a)
    r = sum(a[:k])
    s = r
    for i in range(k, l):
        s += a[i] - a[i-k]
        r = max(r, s)
    return r


'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. 
You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.
'''
def avoidObstacles(inputArray):
    i = 2
    while 1:
        flg = 1
        for k in inputArray:
            if k % i == 0:
                flg = 0
                break
        if flg:
            return i 
        i += 1

        
        
'''
The factorial of n is defined as the product of all natural
numbers up to and including n - 1 * 2 * 3 * ... * n. 
The quasifactorial of n is different in that after each multiplication the result is decreased by one. 
So the quasifactorial of n is (...((1 * 2 - 1) * 3 - 1) * ... * n - 1). The quasifactorial of 1 is 1.

Given a positive integer n, calculate its quasifactorial.

Example

For n = 4, the output should be
quasifactorial(n) = 7.
'''
def quasifactorial(n):
    if n < 2:
        return 1
    return quasifactorial(n-1) * n - 1


'''
A rectangle with sides parallel to the axes can be written 
as a pair of opposing vertices' coordinates of this rectangle.

Find the area of the intersection of two rectangles given in the described format.

Example

For a = [0, 0], b = [2, 2], c = [1, 1] and d = [3, 3], the output should be
rectanglesIntersection(a, b, c, d) = 1.
'''
def rectanglesIntersection(a, b, c, d):
    arr = []
    for i in range(2):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
        if c[i] > d[i]:
            c[i], d[i] = d[i], c[i]
        if b[i] < c[i] or d[i] < a[i]:
            return 0
        arr += [min(b[i], d[i]) - max(a[i], c[i])]
    return arr[0] * arr[1]

'''
Given an integer product, 
find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. 
If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.
'''
def digitsProduct(product):
    if product == 0:
        return 10
    if product == 1:
        return 1
    arr = []
    r = 0
    for i in range(9, 1, -1):
        while product % i == 0:
            arr.append(i)
            product //= i
    if product > 1:
        return -1
    for i in range(len(arr) -1, -1, -1):
        r += arr[i] * 10 ** i
    return r

'''
Court is in session. 
We got a group of witnesses who have all taken an oath to tell the truth. 
The prosecutor is pointing at the defendants one by one and asking each 
witnesses a simple question - "guilty or not?". 
The witnesses are allowed to respond in one of the following three ways:

I am sure he/she is guilty.
I am sure he/she is innocent.
I have no idea.
The prosecutor has a hunch that one of the witnesses might not be telling 
the truth so she decides to cross-check all of their testimonies and see if the information gathered is consistent, i.e. 
there are no two witnesses A and B and a defendant C such that A says C is guilty while B says C is innocent.

Example

For

evidences = [[ 0, 1, 0, 1], 
             [-1, 1, 0, 0], 
             [-1, 0, 0, 1]]
the output should be
isInformationConsistent(evidences) = true;

For

evidences = [[ 1, 0], 
             [-1, 0], 
             [ 1, 1],
             [ 1, 1]]
the output should be
isInformationConsistent(evidences) = false.
'''
def isInformationConsistent(a):
    for i in range(len(a[0])):
        b = 1
        c = 1
        for j in range(len(a)):
            if a[j][i] == 1:
                b = 0 
            if a[j][i] == -1:
                c = 0
        if b + c == 0:
            return 0
    return 1

'''
Given integers p and n, find the smallest non-negative n-digit integer (represented as a string) 
whose digits add up to p. If there is no such number, return "-1" instead.

Example

For p = 15 and n = 3, the output should be
reversedSumOfDigits(p, n) = "159";

For p = 30 and n = 2, the output should be
reversedSumOfDigits(p, n) = "-1";

For p = 2 and n = 5, the output should be
reversedSumOfDigits(p, n) = "10001".
'''
def reversedSumOfDigits(p, n):
    if p == 0 and n > 1:
        return '-1'
    if p > 9 * n:
        return '-1'
    arr = ['0'] * n
    c = n-1
    p -= 1
    while p > 0 and c > 0:
        tmp = min(9, p)
        arr[c] = str(tmp) 
        p -= tmp 
        c -= 1
    if p > 9:
        return '-1'
    arr[0] = str(1 + p)
    return ''.join(arr)



'''
Let's say that number a feels comfortable with number b if a ≠ b and b lies 
in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.

How many pairs (a, b) are there, 
such that a < b, both a and b lie on the segment [l, r], 
and each number feels comfortable with the other?

Example

For l = 10 and r = 12, the output should be
comfortableNumbers(l, r) = 2.

Here are all values of s(x) to consider:

s(10) = 1, so 10 is comfortable with 9 and 11;
s(11) = 2, so 11 is comfortable with 9, 10, 12 and 13;
s(12) = 3, so 12 is comfortable with 9, 10, 11, 13, 14 and 15.
Thus, there are 2 pairs of numbers comfortable with each other within the segment [10; 12]: (10, 11) and (11, 12).
'''
def comfortableNumbers(l, r):
    res = 0
    for i in range(l, r + 1):
        a = f(i)
        for j in range(i + 1, r + 1):
            b = f(j)
            if i-a <= b <= i + a and j -b <= a <= j + b:
                res += 1
    return res
def f(a):
    res = 0
    while a:
        res += a % 10
        a //= 10
    return res

'''
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

For n = 9, the output should be
isSumOfConsecutive2(n) = 2.

There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
isSumOfConsecutive2(n) = 0.

There are no ways to represent n = 8.
'''
def isSumOfConsecutive2(n):
    r = 0
    i = 1
    while i < n // 2 + 1:
        c = i 
        a = n 
        while a > 0:
            a -= c 
            c += 1
        if a == 0:
            r += 1
        i += 1
    return r


def toAndFro(a, b, t):

    l = abs(b - a)
    t %= 2 * l
    if t <= l:
        return a + (b - a) / abs(b - a) * t
    else:
        return b - (b - a) / abs(b - a) * (t-l)
    
    
    
    
'''
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.
'''
def differentSquares(matrix):
    arr = []
    for i in range(len(matrix) -1):
        for j in range(len(matrix[0])-1):
            tmp = []
            for x in range(2):
                line = []
                for y in range(2):
                    line.append(matrix[i + x][j + y])
                tmp.append(line)
            if tmp not in arr:
                arr.append(tmp)
    return len(arr)

'''
You have two triangles A1B1C1 and A2B2C2 on a plane.
Your task is to determine whether they are rather similar, i.e.
if their corresponding angles have the same measurements.

In order for two triangles to be rather similar, the following equations must be true:

angle(A1B1, B1C1) = angle(A2B2, B2C2)
angle(A1C1, C1B1) = angle(A2C2, C2B2)
angle(B1A1, A1C1) = angle(B2A2, A2C2)
where angle(AB, CD) refers to an angle between segments AB and CD in the triangle.
Example

For coordinates = [0, 0, 0, 1, 1, 0, 0, 0, 0, -3, -3, 0], the output should be
areTrianglesSimilar(coordinates) = true.
'''
def areTrianglesSimilar(x):
    def z(a, b, c, d):
        return (a-c) ** 2 + (b-d) ** 2
    a = z(x[0], x[1], x[2], x[3])
    b = z(x[0], x[1], x[4], x[5])
    c = z(x[2], x[3], x[4], x[5])
    d = z(x[6], x[7], x[8], x[9])
    e = z(x[6], x[7], x[10], x[11])
    f = z(x[8], x[9], x[10], x[11])
    return a * e == d * b and a * f == c * d and b * f == c * e

'''
Consider a rectangular chess board of a × b squares.
For each of the squares imagine a lone queen standing on that square and compute the number of squares 
under the queen's attack. Add all the numbers you got for each of the a × b possible queen's positions.

Example

For a = 2 and b = 3, the output should be
chessBoardSquaresUnderQueenAttack(a, b) = 26.

Here are the squares that are under Queen attack:
'''
def chessBoardSquaresUnderQueenAttack(a, b):

    def go(x, y, dx, dy):
        if  x < 0 or x >= a or y < 0 or y >= b:
            return 0
        return go(x + dx, y + dy, dx, dy) + 1

    res = 0

    for i in range(a):
        for j in range(b):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx != 0 or dy != 0:
                        res += go(i + dx, j + dy, dx, dy)

    return res


'''
Define an integer's roundness as the number of trailing zeros in it. 
Sometimes it is possible to increase a number's roundness by swapping two of its digits.

Given an integer n, find the minimum number of swaps required to maximize n's roundness.

Example

For n = 902200100, the output should be
maximizeNumberRoundness(n) = 1.

It's enough to swap the leftmost 0 with 1.

For n = 11000, the output should be
maximizeNumberRoundness(n) = 0.

n already has the maximum roundness possible.
'''
def maximizeNumberRoundness(n):
    tmp = n 
    r = 0
    while tmp:
        if tmp % 10 == 0:
            r += 1
        tmp //= 10
        a = r
    for i in range(a):
        if n % 10 == 0:
            r -= 1
        n //= 10
    return r



'''
Given the prefix sums of some array A, return suffix sums for the same array, i.e. an array B that:

B[0] = A[0] + A[1] + A[2] + ... + A[n - 1]
B[1] =        A[1] + A[2] + ... + A[n - 1]
...
B[n - 2] =             A[n - 2] + A[n - 1]
B[n - 1] =                        A[n - 1]
Example

For prefixSums = [1, 3, 6, 10, 15], the output should be
prefixSumsToSuffixSums(prefixSums) = [15, 14, 12, 9, 5].

You may verify that the initial array A is [1, 2, 3, 4, 5]
(just try to calculate the prefix and suffix sums for it).
'''
def prefixSumsToSuffixSums(a):
    arr = [0] * len(a)
    arr[0] = a[len(a) -1]
    for i in range(1, len(a)):
        arr[i] = arr[0] - a[i-1]
    return arr

        
        
'''
Consider the following operation - we take a positive integer n and replace 
it with the sum of its prime factors (if a prime number is presented multiple 
times in the factorization of n, then it's counted the same number of times in the sum). 
This operation is applied sequentially first to the given number, then to the first result, 
then to the second result and so on, until the result remains the same.

Given any number, find the final result of the operation.

Example

For n = 24, the output should be
factorSum(n) = 5.

24 -> (2 + 2 + 2 + 3) = 9 -> (3 + 3) = 6 -> (2 + 3) = 5 -> 5.
So the answer for n = 24 is 5.
'''        
def factorSum(n):
    arr = [n]
    while 1:
        r = 0
        i = 2
        while n > 1:
            while n % i == 0:
                r += i 
                n //= i
            i += 1
        n = r
        if n in arr:
            return n
        arr.append(n)
        
       
'''
A pile of boxes can be constructed by placing boxes one on top of the other forming a vertical column 
(it is not possible to place more than one box on top of another one directly). 
Each box has a strength value - the number of boxes that it can be under without collapsing.

Given some boxes with their strength values, calculate the minimal number of piles 
that need to be constructed to use up all of these boxes.

Example

For a = [4, 3, 1, 1, 0, 0], the output should be
boxPiles(a) = 2.

It is possible to construct 2 piles: [4, 3, 1, 0] and [1, 0].
'''         
def boxPiles(a):
    a.sort()
    arr = [0] * len(a)
    res = 0
    tmp = 0
    while tmp < len(a):
        c = 0
        for i in range(len(a)):
            if a[i] >= c and not arr[i]:
                arr[i] = 1
                c += 1
                tmp += 1
        res += 1
    return res


'''
Given positive integer numbers a, b and n 
return the maximum number that can be obtained by lengthening number a repeatedly no more than n times.

Lengthening number a means appending exactly one digit (in the decimal notation) 
to the right hand side of a such that the resulting number is divisible by number b. 
If it is impossible to obtain a number that is divisible by b, then the lengthening operation cannot be performed.

Example

For a = 12, b = 11 and n = 2, the output should be
addDigits(a, b, n) = "1210".

Lengthening operations can be 12->121->1210.
'''
def addDigits(a, b, n):
    c = a % b
    res = []
    res.append(str(a))
    for i in range(n):
        tmp = -1
        for j in range(9, -1, -1):
            if (c * 10 + j) % b == 0:
                tmp = j
                break
        if tmp == -1:
            break
        res.append(str(tmp));
        c = 0
    return ''.join(res)


'''
Given array of integers, for each position i, 
search among the previous positions for the last (from the left) position that contains a smaller value. 
Store this value at position i in the answer. If no such value can be found, store -1 instead.

Example

For items = [3, 5, 2, 4, 5], the output should be
arrayPreviousLess(items) = [-1, 3, -1, 2, 4].
'''
def arrayPreviousLess(a):
    r = [-1] * len(a)
    for i in range(1, len(a)):
        s = 0
        for j in range(i):
            if a[j] < a[i]:
                s = a[j]
        if s:
            r[i] = s 
    return r

def arrayPreviousLess(items):
    arr = []
    for i in range(len(items)):
        tmp = -1
        for j in range(i):
            if items[j] < items[i]:
                tmp = items[j]
        arr.append(tmp)
    return arr
                
                
                
'''
You are given a positive integer x and you should perform n operations, 
where on the ith operation you increase x in such a way that its new value is
divisible by i (operations are numbered from 1 to n).

Find the minimal value of x you can obtain by performing n operations described above.

Example

For x = 9 and n = 5, the output should be
increasingNumber(x, n) = 15.
'''                
def increasingNumber(x, n):
    for i in range(1, n + 1):
        while x % i:
            x += 1
    return x

'''
You're given two integers, n and m. Find position of the 
rightmost pair of equal bits in their binary representations 
(it is guaranteed that such a pair exists), counting from right to left.

Return the value of 2position_of_the_found_pair (0-based).

Example

For n = 10 and m = 11, the output should be
equalPairOfBits(n, m) = 2.

1010 = 10102, 1110 = 10112, the position of the rightmost pair of equal bits is 
the bit at position 1 (0-based) from the right in the binary representations.
So the answer is 21 = 2.
'''
def equalPairOfBits(n, m):

    return n + m + 1 & ~ m - n


def equalPairOfBits(n, m):
    ans = 1
    while n % 2 != m % 2:
        ans *= 2
        n //= 2
        m //= 2
    return ans

'''
Given a string s and an integer k, can you compose exactly k non-empty palindromes 
using each letter of s exactly once?

Example

For s = "abracadabra" and k = 3, the output should be
composeKPalindromes(s, k) = true.

The answer is true since you are able to compose 3 palindromes using each letter of "abracadabra" once.
3 possible palindromes that fulfill this requirement are: "araaara", "bcb", and "d".

For s = "abracadabra" and k = 2, the output should be
composeKPalindromes(s, k) = false.
'''
def composeKPalindromes(s, k):
    D = {}
    for i in s:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
            
    T = 0
    for a in D:
        T += D[a] % 2
    return T <= k and len(s) >= k

'''
Caesar Box is a simple transposition cipher used in the Roman Empire. 
It is described as the following two-step process:

The characters of the given message are broken into n lines of equal lengths and stacked up;
The letters from the resulting rectangle are written from top to bottom column by column.
Given a word, count the number of different n such that the message, obtained by applying encoding two times, 
is the same as initial message.

Example

For message = "abaaba", the output should be
caesarBoxCipherEncoding2(message) = 2.

It is possible to apply the encoding algorithm for n = 2 or n = 3.
For n = 2:

The first encoding: "abaaba" -> "aabbaa";

aba
aba
The second encoding: "aabbaa" -> "abaaba".

aab
baa
'''
def caesarBoxCipherEncoding2(message):
    r = 0
    for i in range(2, len(message)):
        if len(message) % i != 0:
            continue
        if encode(encode(message, i), i) == message:
            r += 1
    return r

def encode(a, n):
    r = ''
    for i in range(n):
        for c in range(i, len(a), n):
            r += a[c]
    return r


'''
Given a string with at least one digit, extract the rightmost digit from it.

Example

For inputString = "var_1__Int", the output should be
lastDigitRegExp(inputString) = '1';
For inputString = "qq2q", the output should be
lastDigitRegExp(inputString) = '2';
For inputString = "0ss", the output should be
lastDigitRegExp(inputString) = '0'.
'''
def lastDigitRegExp(inputString):
    return re.findall(r'\d+', inputString,)[-1]
    #return re.findall(r'\d+', inputString[::-1])[0]
    
    
    
'''
Given some integer, find the maximal number you can obtain 
by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.
'''    
def deleteDigit(n):
    r = 0
    n = list(str(n))
    for i in range(len(n)):
        tmp = n[:i] + n[i + 1:]
        tmp = ''.join(tmp)
        tmp = int(tmp)
        if tmp > r:
            r = tmp 
    return r

'''
Let's consider a sequence X1 = 1, X2 = 1 ^ 2, ..., Xn = 1 ^ ... ^ n, where ^ is a bitwise xor.

Given l and r, find the value of Xl ^ Xl + 1 ^ ... ^ Xr.

Example

For l = 1 and r = 5, the output should be
rangeConsecutiveXor(l, r) = 7;
For l = 3 and r = 4, the output should be
rangeConsecutiveXor(l, r) = 4.
'''
def rangeConsecutiveXor(l, r):
    res = 0
    while l <= r:
        res ^= [l, 1, l + 1, 0][l % 4]
        l += 1
        if l % 8 < 1 and r - l > 8:
            l = r - r % 8
    return res


'''
You are given an array of integers inputArray. Consider all its contiguous 
subarrays of length k and pick the one with the maximum sum. 
If there are several contiguous subarrays with the maximum sum, pick the leftmost one.
Put the 0-based index of the first (leftmost) element of that subarray into result[k - 1]. 
Do this for all k from 1 up to the length of the inputArray. Return result.

Example

For inputArray = [-1, 2, 1, 3, -2], the output should be
maxSumSegments(inputArray) = [3, 2, 1, 0, 0].
The contiguous subarray of length 1 is the element with index 3, so result[0] = 3; 
of length 2 is subarray [1, 3], which starts at the index 2; of length 3 is - [2, 1, 3], 
which starts at index 1; of length 4 - [-1, 2, 1, 3], which starts at index 0; of length 5 is an inputArray itself.
'''
def maxSumSegments(a):
    arr = [0] * len(a)
    for i in range(1, len(a) + 1):
        s = 0
        maxS = 0
        index = -1
        for j in range(len(a)):
            s += a[j]
            if j >= i:
                s -= a[j-i]
            if j >= i-1 and (index == -1 or s > maxS):
                maxS = s
                index = j -i + 1
        arr[i-1] = index
    return arr


        
        
        
'''
Consider a digital chess clock, which shows the time in the format "m.ss" on each of the two displays.



Here is how the chess clock works: At any given moment, 
only one side of the clock is active, meaning that the time on one of the displays goes backwards 
while the time on the other side remains the same. After a player makes a move, they press the button, 
and their side of the clock pauses while the time on their opponent's side starts going backwards.

Assume that the time initially displayed on the clock is precise, i.e. 
for the active display the time decreases by one second after exactly one second has elapsed. 
The first player's clock is active at the moment when we begin observing the game.

Note that the players can press the button at any moment - for example, 
at 2.5 seconds from the initial time. Assume that during the game, 
the button can be pressed an arbitrary number of times. When one of the displays shows "0:00", 
the game ends immediately.

Given initialTime for both sides of the clock and a positive integer k, 
what are the maximum and the minimum sum of digits that can possibly 
appear on the clock within the next k + 0.5 seconds?

Example

For initialTime = ["3.05", "9.02"], k = 9, the output should be
chessClockSumOfDigits(initialTime, k) = [12, 38].

The situation in which you can obtain the minimum sum is ["3.00", "9.00"]. 
For instance, the first player can spend 5 seconds on their move, after 
which the second player can think for 2 seconds (not necessarily pressing the button after that). 
After that, the clock will show ["3.00", "9.00"]. The sum of these digits is 12. 
During the remaining 2.5 seconds (out of k + 0.5 that we are considering), 
the sum of the digits cannot become smaller, so 12 is the answer.

The situation in which you can obtain the maximum sum is ["2.59", "8.59"]. 
For instance, the first player (whose side of clock was initially active) can press 
the clock 1.5 second after the beginning (when the clock showed ["3.04", "9.02"]), 
then the second player can spend three seconds until pressing the button 
(after which the clock showed ["3.04", "8.59"]). 4.5 seconds later 
(during which the first player was thinking) the clock will show ["2.59", "8:59"]. 
Only 0.5 seconds remain out of the k + 0.5 that we are considering, so the values on display cannot change any more. 
The sum of these digits is 38.
'''
def chessClockSumOfDigits(initialTime, k):
    def toSec(t):
        m, s = t.split('.')
        return int(m) * 60 + int(s)
    
    def sumOfDigit(t):
        if t <= 0:
            return 0
        s = t // 60
        t -= s * 60 
        s += t % 10 + t // 10 
        return s
    
    a, b = map(toSec, initialTime)
    mi = mx = sumOfDigit(a) + sumOfDigit(b)
    
    for i in range(k + 1):
        for j in range(k + 1-i):
            s = sumOfDigit(a-i) + sumOfDigit(b-j)
            if s > 0:
                mi = min(mi, s)
                mx = max(mx, s)
    return mi, mx
            
'''
Every positive integer can be uniquely represented as a sum of different positive powers of two.

Given a number n, return a sorted array of different powers of two that sum up to n.

Example

For n = 5, the output should be
powersOfTwo(n) = [1, 4].
'''            
def powersOfTwo(n):
    arr = []
    a = 1
    while n:
        if (n & 1) != 0:
            arr.append(a)
        n >>= 1
        a <<= 1
    return arr

'''
A masked number is a string that consists of digits and one asterisk (*) 
that should be replaced by exactly one digit. 
Given a masked number find all the possible options to replace the asterisk
with a digit to produce an integer divisible by 6.

Example

For inputString = "1*0", the output should be
isDivisibleBy6(inputString) = ["120", "150", "180"].

Input/Output

[time limit] 4000ms (py3)
[input] string inputString

A masked number.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] array.string

Sorted array of strings representing all non-negative 
integers that correspond to the given mask and are divisible by 6.
'''
def isDivisibleBy6(a):
    arr = []
    for i in range(10):
        tmp = a.replace('*', str(i))
        if int(tmp) % 6 == 0:
            arr.append(tmp)
    return arr

'''
Given a permutation, produce its inverse permutation.

Example

For permutation = [1, 3, 4, 2], the output should be
inversePermutation(permutation) = [1, 4, 2, 3].
'''
def inversePermutation(a):
    res = [0] * len(a)
    for i in range(len(a)):
        res[a[i] - 1] = i + 1
    return res



'''
Given an integer product, find the smallest positive (i.e. greater than 0) integer 
the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.
'''
def digitsProduct(product):
    arr = []
    res = 0
    if product == 0:
        return 10
    if product < 10:
        return product
    # Check from 9 to 2, push to list
    for i in range(9, 1, -1):
        while product % i  == 0:
            arr.append(i)
            product //= i 
    if product > 1:
        return -1
    for i in range(len(arr)-1, -1, -1):
        res = res * 10 + arr[i]
    return res


'''
You are given an array of desired filenames in the order of their creation.
Since two files cannot have equal names, the one which comes later 
will have an addition to its name in a form of (k), 
where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
'''
def fileNaming(names):
    res = [names[0]]
    for i in range(1, len(names)):
        if names[i] in names[0:i] or names[i] in res[0:i]:
            j = names[0:i].count(names[i])
            k = res[0:i].count(names[i])
            j = max(j, k)
            temp = names[i] + "(" + str(j) + ")"
            while temp in res[0:i]:
                j += 1
                temp = names[i] + "(" + str(j) + ")"
            res.append(temp)
        else:
            res.append(names[i])
    return res

'''
A robot is standing at the (0, 0) point of the Cartesian plane and is oriented
towards the vertical (y) axis in the direction of increasing y values (in other words, he's facing up, or north). 
The robot executes several commands each of which is a single positive integer. 
When the robot is given a positive integer K it moves K squares forward and then turns 90 degrees clockwise.

The commands are such that both of the robot's coordinates stay non-negative.

Determine if there is a square that the robot visits at least twice after executing all the commands.

Example

For a = [4, 4, 3, 2, 2, 3], the output should be
robotWalk(a) = true.

The path of the robot looks like this:
'''
robotWalk = lambda a: any(a[i] >= a[i-2] for i in range(3, len(a)))

def robotWalk(a):
    for i in range(3, len(a)):
        if a[i] >= a[i-2]:
            return True
    return False 


'''
Several friends live along a straight street. 
They are friends, thus they enjoy visiting each other. 
However, they are lazy so none of them wants to visit a friend living more than maxDist meters away from them.

Given array houses representing coordinates of points where the friends live 
(in meters) and an integer maxDist, return an array representing the number of friends 
each person would be willing to visit.

Example

For houses = [1, 2, 4, 8, 10] and maxDist = 5, the output should be
lazyFriends(houses, maxDist) = [2, 2, 3, 2, 1].

Check out the image below for better understanding:
'''
def lazyFriends(h, m):
    c = len(h)
    a = []
    l = r = 0
    for i in h:
        while i - h[l] > m:
            l += 1
        while r + 1 < c and h[r + 1] - i <= m:
            r += 1
        a.append(r-l)
    return a


'''
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, 
starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
'''
def spiralNumbers(n):
    arr = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    a = [[0 for i in range(n)] for i in range(n)]
    cur_p = (0, 0)
    cur_d = 0
    for i in range(1, n * n + 1):
        a[cur_p[0]][cur_p[1]] = i
        nxt_p = cur_p[0] + arr[cur_d][0], cur_p[1] + arr[cur_d][1] 
        if nxt_p[0] >= n or nxt_p[0] < 0 or nxt_p[1] >= n or nxt_p[1] < 0 or a[nxt_p[0]][nxt_p[1]] != 0:
            cur_d = (cur_d + 1) % 4
            nxt_p = cur_p[0] + arr[cur_d][0], cur_p[1] + arr[cur_d][1] 
        cur_p = nxt_p
    return a



'''
Return the value of Z-function for a given string.

Example

For s = "acacbab", the output should be
zFunctionNaive(s) = [7, 0, 2, 0, 0, 1, 0].

Here's where the non-zero values of Z-function came from:
'''
def zFunctionNaive(s):
    res = [0] * len(s)
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[j] == s[res[i]]:
                res[i] += 1
            else:
                break
    return res
    
    
'''
It is a common tradition to play Hangman game during classes. 
Too bad it's difficult to do so if you and your friend sit far from each other.
You, however, came up with a great idea.

First, you write down a word. After that your friend writes down distinct 
letters and passes the list with them to you.
Now you look at the letters in his list one by one. 
If the current letter is present in your word, you erase all occurrences of this letter from it,
otherwise you call it a miss. If you erase the entire word before 6 misses, then your friend wins. 
If you count 6 misses or run out of letters before the word is erased, you win.

Given the word you made and your friend's letters, return true if he wins or false otherwise.
Example
For word = "hello" and letters = "aenmrolhtg", the output should be
hangman(word, letters) = true.

The stages of the game are:
'a' - 1st miss;
'e' - correct letter (_ e _ _ _);
'n' - 2nd miss;
'm' - 3rd miss;
'r' - 4th miss;
'o' - correct letter (_ e _ _ o);
'l' - correct letter (_ e l l o);
'h' - correct letter (h e l l o);
Other letters don't matter since the word is guessed already.
'''    
def hangman(word, letters):
    arr = [0] * 26
    c = 0
    for i in range(len(word)):
        tmp = ord(word[i]) - ord('a')
        if not arr[tmp]:
            arr[tmp] = 1
            c += 1
    cnt = 0
    i = 0
    while cnt < 6 and c > 0 and i < len(letters):
        tmp = ord(letters[i]) - ord('a')
        if arr[tmp]:
            arr[tmp] = 0
            c -= 1
        else:
            cnt += 1
        i += 1
        
    return cnt < 6 and c == 0

'''
You are given an array of up to four non-negative integers, each less than 256.

Your task is to pack these integers into one number M in the following way:

The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.
Return the obtained integer M.

Note: the phrase "first bits of M" refers to the least significant bits 
of M - the right-most bits of an integer. For further clarification see the following example.

Example

For a = [24, 85, 0], the output should be
arrayPacking(a) = 21784.

An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.
After packing these into one number we get 00000000 01010101 00011000 (spaces are placed for convenience),
which equals to 21784.
'''
def arrayPacking(a):
    r = 0
    for i in range(len(a)):
        r += a[i] << (8 * i)   
    return r



'''
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint
substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is 
replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".
'''
def lineEncoding(s):
    i = 1
    cur = s[0]
    cnt = 1
    res = ''
    while i < len(s):
        tmp = s[i]
        if tmp == cur:
            cnt += 1
        else:
            if cnt > 1:
                res += str(cnt) + cur 
            else:
                res += cur
            cnt = 1
            cur = tmp
        i += 1
    if cnt > 1:
        res += str(cnt) + cur 
    else:
        res += cur
    return res

            
'''
The positive divisor of X is called trivial if it is equal to 1 or to X. 
All other positive divisors are called non-trivial.

Given array of integers superset and integer n, 
find the number of integers between 1 and n, inclusive, 
such that for each of these integers superset is the superset of its non-trivial divisors (i.e. it contains all of them).

Example

For superset = [3, 2] and n = 13, the output should be
divisorsSuperset(superset, n) = 10.

Here are these numbers: 1, 2, 3, 4, 5, 6, 7, 9, 11, 13.
'''            
def divisorsSuperset(superset, n):
    res = 0
    for i in range(1, n + 1):
        flg = 1
        j = 2
        while j * j <= i:
            if i % j == 0:
                if i == j or i // j not in superset:
                    flg = 0
                    break
            j += 1
        if flg:
            res += 1
    return res


def sequenceElement(a, n):
    t = n 
    l = a[:]
    while n:
        a += [sum(a[-5:]) % 10]
        if a[-5:] == l:
            return a[t % (len(a) -5)]
        n -= 1
    return a[t]



'''
Given an array of integers, sort its elements by the difference of their largest and smallest digits. 
In the case of a tie, that with the larger index in the array should come first.

Example

For a = [152, 23, 7, 887, 243], the output should be
digitDifferenceSort(a) = [7, 887, 23, 243, 152].

Here are the differences of all the numbers:

152: difference = 5 - 1 = 4;
23: difference = 3 - 2 = 1;
7: difference = 7 - 7 = 0;
887: difference = 8 - 7 = 1;
243: difference = 4 - 2 = 2.
23 and 887 have the same difference, but 887 goes after 23 in a, so in the sorted array it comes first.
'''
def digitDifferenceSort(a):
    return sorted(a[::-1], key=f)
def f(n):
    arr = []
    while n:
        arr.append(n % 10)
        n //= 10
    if len(arr) == 0:
        return 0
    return max(arr) - min(arr)
        
    
    
    
'''
Given integers n and k, find the number of strictly increasing sequences 
of length n consisting of positive integers not exceeding k

Example

For n = 2 and k = 3, the output should be
countIncreasingSequences(n, k) = 3.
They are: [1, 2], [1, 3] and [2, 3].
'''    
def countIncreasingSequences(n, k):
    res = 0
    arr = []
    
    for i in range(n + 1):
        line = []
        for j in range(k + 1):
            line.append(0)
        arr.append(line)
    
    arr[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for x in range(j):
                arr[i][j] += arr[i-1][x]
                
    for i in range(1, k + 1):
        res += arr[n][i]
    return res


'''
Given array of integers, check whether each integer, that occurs in it,
is contained there the same number of times as any other integer from the given array.

Example

For inputArray = [1, 2, 2, 1], the output should be
checkEqualFrequency(inputArray) = true;
For inputArray = [1, 2, 2, 3, 1, 3, 1, 3], the output should be
checkEqualFrequency(inputArray) = false.
'''
def checkEqualFrequency(a):
    return len(set(a.count(i)  for i in set(a))) == 1


'''
Consider the following operation on a string containing digits from 1 to 9:

if the leftmost digit of the string is divisible by 3, remove it from the string;
otherwise, if the rightmost digit of the string is divisible by 3, remove it from the string;
otherwise, if the sum of two digits on the sides of the string is divisible by 3, remove both digits from the string;
This operation is applied sequentially until the string is empty or neither of the three given conditions is met.

For a given string find the result of applying the given algorithm to it.

Example

For s = "312248", the output should be
truncateString(s) = "2".

Here's how the answer is obtained:

3 is divisible by 3 and should be removed ("12248");
neither 1 nor 8 is divisible by 3, but their sum is, so both digits should be removed ("224");
neither 2 nor 4 is divisible by 3, but their sum is, so both digits should be removed ("2");
the resulting string "2" doesn't meet any condition, so it is the final answer.
'''
def truncateString(s):
    while len(s) > 0 and (int(s[0]) % 3 == 0 or int(s[-1]) % 3 == 0 or (int(s[0]) + int(s[-1])) % 3 == 0):
        if int(s[0]) % 3 == 0:
            s = s[1:]
            continue
        if int(s[-1]) % 3 == 0:
            s = s[:-1]
            continue
        if (int(s[0]) + int(s[-1])) % 3 == 0:
            s = s[1:-1]
        
    return s

def truncateString(s):
    flg = 1
    while len(s) and flg:
        if int(s[0]) % 3 == 0:
            s = s[1:]
            continue
        if int(s[-1]) % 3 == 0:
            s = s[:-1]
            continue
        if (int(s[0]) + int(s[-1])) % 3 == 0:
            s = s[1:-1]
            continue
        flg = 0
    return s






'''
Given an array of integers inputArray and an integer maxSum, 
for each i (0 ≤ i < length of inputArray) find the rightmost j (j < length of inputArray) 
such that the sum of all elements between the ith and jth elements (both inclusive) is not greater than maxSum.

Example

For inputArray = [2, 3, 0, 1, 2] and maxSum = 4, the output should be
maximalAllowableSubarrays(inputArray, maxSum) = [0, 3, 4, 4, 4].
'''
def maximalAllowableSubarrays(inputArray, maxSum):
    arr = []
    s = 0
    k = -1
    for i in range(len(inputArray)):
        if i > 0:
            s -= inputArray[i-1]
        while k < len(inputArray) - 1 and s + inputArray[k + 1] <= maxSum:
            k += 1
            s += inputArray[k]
        arr.append(k)
    return arr

'''
Let's call an integer unusual if the sum of its digits is larger than the product of its digits. 
For example, the numbers 21 and 990 are unusual, while the numbers 22 and 991 aren't.

Given an integer a (represented as a string), find the smallest unusual integer x such that x ≥ a. 
Since both x and a can be very large, return the value of x - a.

Example

For a = "42", the output should be
smallestUnusualNumber(a) = 8.

The smallest unusual number that is greater than or equal to 42 is 50, and 50 - 42 = 8
'''
def smallestUnusualNumber(a):
    tmp = list(a)
    arr = []
    for i in tmp:
        arr.append(int(i))
    s = 0
    p = 1
    for i in arr:
        s += i
        p *= i
    res = 0
    last = arr[-1]
    while p >= s:
        last += 1
        res += 1
        if last == 10:
            return res
    return res


'''
You have found a machine which, when fed with two numbers s and e, 
produces a strange code consisting of the letters a and b. The machine seems to be using the following algorithm.

Check if s is less than e - 1. If so, continue to step 2. If not, exit.
Increment s by 1
Decrement e by 1
If this is the first letter you're producing, produce a. 
Otherwise produce a letter different from the one you last produced (only a and b may be produced)
go to step 1.
You are to write a function that simulates the workings of the machine.
'''
def strangeCode(s, e):
    prev = '-';
    res = "";

    while s < e - 1:
        s += 1
        e -= 1
        if prev == '-' or prev == 'b':
            prev = 'a'
            res += prev
        else:
            prev = 'b'
            res += prev
    return res


def sumOfEvenFibs():
    # a,b,c in the Fibonacci sequence
    a = 1
    b = 1
    result = 2
    while b < 4000000:
        c = a + b
        a = b 
        b = c
        if b % 2:
            result += b
    return result
        
    
        
'''
Determine if it is possible to sort an array by reversing one of its contiguous subarrays.

It's guaranteed that array is not initially sorted.

Example

For inputArray = [-1, 5, 4, 3, 2, 8], the output should be
reverseToSort(inputArray) = true.

We can reverse [5, 4, 3, 2] to make it sorted.

For inputArray = [1, 3, 2, 5, 4, 6], the output should be
reverseToSort(inputArray) = false.
'''        
def reverseToSort(inputArray):
    def f(a):
        for i in range(0, len(a)):
            if a[i] <= a[i-1]:
                return 0
        return 1
    for i in range(1, len(inputArray)):
        left = inputArray[:i]
        for j in range(i, len(inputArray) + 1):
            center = inputArray[i:j]
            center = center[::-1]
            right = inputArray[j:]
            s = left + center + right
            if f(s):
                return 1
    return 0

'''
Given a number of the pages in some book find 
the number of digits one needs to print to enumerate the pages of the book.

Example

For n = 11, the output should be
pagesNumbering(n) = 13.
'''
def pagesNumbering(n):
    #number of digits of n 
    c  = len(str(n))
    if c == 1:
        return n
    # result
    r = 0
    #number of digits
    i = 1
    while i < c:
        r += i * (10 ** i - 10 ** (i-1))
        i += 1
    return r + (n-10 ** (c-1) + 1) * c


'''
For a given integer n, return the shortest possible list of distinct
Fibonacci numbers that sum up to n, sorted in ascending order.

Example

For n = 20, the output should be
fibonacciSum(n) = [2, 5, 13].
'''
def fibonacciSum(n):
    arr = [1, 1]
    a = 1
    b = 1
    c = a + b 
    while c <= n:
        arr.append(c)
        a = b
        b = c
        c = a + b
    arr = arr[::-1]
    res = []
    for i in arr:
        if n - i >= 0:
            n -= i
            res.append(i)
        if n == 0:
            break
    return res[::-1]
            
'''
Let's define a specific geometric shape on an infinite grid:

A shape with an order of 1 is just a single cell.
A shape with an order of 2 can be visualized as a shape with an order of 1 
with a new cell added to each edge of the original shape, as in the diagram below.
Following that same pattern, a shape with an order of n can be visualized 
as a shape with an order of n - 1 with a new cell added to each edge of each cell in the original shape.
You have two such shapes. 
Each shape is represented as an array containing three integers: 
the first element indicates the order of the shape,
while the second and third elements indicate the coordinates of the shape's center on the grid. 
Calculate the number of cells in the area where the shape1 and shape2 intersect - in other words, 
the cells that the two shapes have in common.

Example

For shape1 = [3, 0, -1] and shape2 = [5, 3, 0], the output should be
areaOfIntersection(shape1, shape2) = 8.
'''        
def areaOfIntersection(shape1, shape2):
    r1, x1, y1 = shape1
    r2, x2, y2 = shape2
    result = 0
    for i in range(-1000, 1001):
        low = max(y1 - (r1 - abs(i-x1)), y2 - (r2 - abs(i-x2)))
        height = min(y1 + (r1 - abs(i-x1)), y2 + (r2 - abs(i-x2)))
        result += max(height - low - 1, 0)
    return result


'''
A number is considered special, 
if it remains the same (and continues being a valid number) when rotated by 180°. 
For example, number 986 is special, but 11 or 9 aren't, 
because 1 ceases to be a digit after the rotation and 9 becomes 6 after the rotation.

Determine the number of special integers between l and r, inclusive.

Example

For l = 8 and r = 8, the output should be
specialNumbers(l, r) = 1;
For l = 66 and r = 96, the output should be
specialNumbers(l, r) = 3.
'''
def specialNumbers(l, r):
    res = 0
    for i in range(l, r + 1):
        if special(str(i)):
            res += 1
    return res
    
def special(s):
    a = '0689'
    b = '0986'
    t = ''
    for i in s:
        if i not in a:
            return 0
        t += b[a.index(i)]
    return s == t[::-1]


from itertools import permutations
def numberMinimization(n, d):
    res = {n}
    qq = set()
    q = [n]
    while q:
        c = q.pop()
        if c % d == 0 and c // d not in res:
            res.add(c // d)
            q.append(c // d)
        if c not in pp:
            for p in permutations(str(c)):
                e = int("".join(p))
                pp.add(e)
                if e not in res:
                    res.add(e)
                    q.append(e)
    return min(res)

'''
After recently joining Instacart's beta testing developer group, 
you decide to experiment with their new API. 
You know that the API returns item-specific display-ready strings like 10.0% higher 
than in-store or 5.0% lower than in-store that inform users 
when the price of an item is different from the one in-store. 
But you want to extend this functionality by giving people a better sense of 
how much more they will be paying for their entire shopping cart.

Your app lets a user decide the total amount x they are willing to pay via Instacart over in-store prices. 
This you call their price sensitivity.

Your job is to determine whether a given customer will be willing to pay
for the given items in their cart based on their stated price sensitivity x.
'''
def isAdmissibleOverpayment(prices, notes, x):
    r = 0.0
    for i in range(len(prices)):
        tmp = notes[i]
        if "Same as" in tmp:
            continue
        elif "higher than" in tmp:
            c = tmp.split("%")
            y = float(c[0]) / 100
            z = prices[i] - prices[i] / (1 + y)
        else:
            c = tmp.split("%")
            y = float(c[0]) / 100
            z = prices[i] - prices[i] / (1 - y)
        r += z
    return x  > r - 0.0001

'''
A rational number is the ratio of two integers, where the denominator is not zero. 
We are going to represent the rational number numerator / denominator as the ordered pair (numerator, denominator).

There are many different tuples representing the same rational number. 
For instance, one-half is (1, 2), (2, 4), (3, 6), etc. Your task is to write a function that, 
given the numbers numerator and denominator representing the ratio numerator / denominator, 
returns an array [a, b] of two integers where:

(a, b) represents the same rational number as (numerator, denominator) but in simplified format;
a and b have no non-trivial factors;
b is positive.
Example

For numerator = 3 and denominator = 6, the output should be
simplifyRational(numerator, denominator) = [1, 2].

The number 3 / 6 can be reduced to 1 / 2.

For numerator = 8 and denominator = 5, the output should be
simplifyRational(numerator, denominator) = [8, 5].

There is no way to simplify 8 / 5 any further, as the only factor that 8 and 5 have in common is 1.

For numerator = 8 and denominator = -5, the output should be
simplifyRational(numerator, denominator) = [-8, 5].

One of the requirements is that the denominator should be positive, so 8 / (-5) didn't fit our format, but -8 / 5 does.
'''
def simplifyRational(numerator, denominator):
    if numerator == 0:
        return [0, 1]
    if denominator < 0:
        denominator *= -1
        numerator *= -1
    c = gcd(numerator, denominator)    
    return [numerator / c, denominator / c]

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

'''
Given a string s, find all its potential permutations. 
The output should be sorted in lexicographical order.

Example

For s = "CBA", the output should be
stringPermutations(s) = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"];
For s = "ABA", the output should be
stringPermutations(s) = ["AAB", "ABA", "BAA"].
'''
from itertools import permutations
def stringPermutations(s):
    arr = [''.join(i) for i in permutations(s)]
    a = sorted(arr)
    arr = []
    for i in a:
        if i not in arr:
            arr.append(i)
    return arr

'''
Solve quadratic equation of the form a * x2 + b * x + c = 0 
and return sorted array of all its different real roots.

Example

For a = 1, b = -3 and c = 2, the output should be
quadraticEquation(a, b, c) = [1, 2];
For a = 1, b = 2 and c = 1, the output should be
quadraticEquation(a, b, c) = [-1];
For a = 2, b = 2 and c = 1, the output should be
quadraticEquation(a, b, c) = [].
'''
def quadraticEquation(a, b, c):
    if a == 0:
        if b == 0 and c != 0:
            return []
        return [-c/b]
    delta = b* b - 4*a*c
    if delta < 0:
        return []
    if delta == 0:
        return [-b/(2 * a)]
    t = math.sqrt(delta)
    arr =  (-b-t)/(2*a), (-b+t)/(2*a)
    return sorted(arr)


'''
Given an integer n, you can remove either its first or last digit in one step. 
After applying this operation several times, you'll get a number x with a length of k. 
It's possible that the number will contain leading zeros. 
What is the minimal and the maximal possible value of x that you can obtain?

Example

For n = 15243 and k = 2, the output should be
removeDigits(n, k) = [15, 52].

To obtain the minimal number with a length of k, 
we can use the following sequence of operations: 15243 -> 1524 -> 152 -> 15;
To obtain the maximal number with a length of k, 
we can use the following sequence of operations: 15243 -> 1524 -> 152 -> 52.
For n = 123 and k = 1, the output should be
removeDigits(n, k) = [1, 3].
'''
def removeDigits(n, k):
    n = str(n)
    minNum = maxNum = int(n[0:k])
    for i in range(len(n)):
        if i+k > len(n):
            break
        tmp = int(n[i:i+k])
        minNum = min(minNum, tmp)
        maxNum = max(maxNum, tmp)
    return minNum, maxNum


'''
Map the given integer to a month.

Example

For mo = 1, the output should be
getMonthName(mo) = "Jan";
For mo = 0, the output should be
getMonthName(mo) = "invalid month".
'''
import calendar as c
def getMonthName(m):
    if 0 < m < 13:
        return c.month_name[m][:3]
    return  "invalid month"



'''
Given a set of complex values, find their product.

Example

For real = [1, 2] and imag = [1, 3], the output should be
arrayComplexElementsProduct(real, imag) = [-1, 5].
The task is to calculate product of 1 + 1 * i and 2 + 3 * i,
so the answer is (1 + 1i) * (2 + 3i) = -1 + 5i.
'''
def arrayComplexElementsProduct(real, imag):
    res = [real[0], imag[0]]
    for i in range(1, len(real)):
        res = product(res, [real[i], imag[i]])
    return res
def product(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


'''
The look-and-say sequence is defined as follows:

Its first term is equal to 1.
The nth term (for n > 1) is generated by reading the (n-1)th term.
Thus,

the second term is 11, generated by reading the first term as "One 1" (There is one 1 in previous term);
the third term is 21, generated by reading the second term as "Two 1";
the fourth term is 1211, generated by reading the third term as "One 2 One 1";
and so on.

Given some element of the look-and-say sequence, generate the next one.

Example

For element = "1", the output should be
lookAndSaySequenceNextElement(element) = "11";
For element = "1211", the output should be
lookAndSaySequenceNextElement(element) = "111221".
'''
def lookAndSaySequenceNextElement(element):
    res = ""
    cur = element[0]
    cnt = 1
    for i in range(1, len(element)):
        tmp = element[i]
        if tmp == cur:
            cnt += 1
        else:
            res += str(cnt) + cur
            cnt = 1
            cur = tmp
    return res + str(cnt) + cur

'''
 Python program for implementation of Insertion Sort
'''
def insertionSort(a):
    # Traverse through 1 to len(a)
    for i in range(1, len(a)):
        key = a[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - i 
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j-=1
        a[j+1] = key
    return a


'''
Python program for implementation of Selection Sort
'''
def selectionSort(a):
    # Traverse through all array elements
    for i in range(len(a)):
        # Find the minimum element in remaining 
        # unsorted array
        minIdx = i
        for j in range(i+1, len(a)):
            if a[minIdx] > a[j]:
                minIdx = j
                
        # Swap the found minimum element with 
        # the first element      
        if i != minIdx:
            a[i],a[minIdx]  = a[minIdx], a[i]
    return a


'''
Given a rectangular matrix of integers and integers n and m, 
we are looking for the submatrix of size n × m that has the maximal sum among all submatrices of the given size.

Example

For

matrix = [[1, 12, 11, 10], 
          [4,  3,  2,  9], 
          [5,  6,  7,  8]]
n = 2 and
m = 1, the output should be
maxSubmatrixSum(matrix, n, m) = 19.
'''
def maxSubmatrixSum(matrix, n, m):
    res = -1000000
    for i in range(len(matrix) - n+1):
        for j in range(len(matrix[0]) - m+1):
            s = 0
            for u in range(n):
                for v in range(m):
                    s += matrix[i + u][v + j]
            res = max(s, res)
    return res


'''
We define the weakness of number x as the number of positive integers smaller than x that have more divisors than x.

It follows that the weaker the number, the greater overall weakness it has.
For the given integer n, you need to answer two questions:

what is the weakness of the weakest numbers in the range [1, n]?
how many numbers in the range [1, n] have this weakness?
Return the answer as an array of two elements, 
where the first element is the answer to the first question,
and the second element is the answer to the second question.

Example

For n = 9, the output should be
weakNumbers(n) = [2, 2].

Here are the number of divisors and the specific weakness of each number in range [1, 9]:

1: d(1) = 1, weakness(1) = 0;
2: d(2) = 2, weakness(2) = 0;
3: d(3) = 2, weakness(3) = 0;
4: d(4) = 3, weakness(4) = 0;
5: d(5) = 2, weakness(5) = 1;
6: d(6) = 4, weakness(6) = 0;
7: d(7) = 2, weakness(7) = 2;
8: d(8) = 4, weakness(8) = 0;
9: d(9) = 3, weakness(9) = 2.
As you can see, the maximal weakness is 2, and there are 2 numbers with that weakness level.
'''
def weakNumbers(n):
    arr = []
    for i in range(n+1):
        arr.append(numberDiv(i))
    a = []
    for i in range(len(arr)):
        c = 0
        for j in range(i):
            if arr[j] > arr[i]:
                c+=1
        a.append(c)
    a = a[]
    m = max(a)
    r = 0
    for i in a:
        if i == m:
            r += 1
    return m,r

def numberDiv(a):
    r = 1
    for i in range(2, a + 1):
        if a % i ==0:
            r += 1
    return r


'''
We want to turn the given integer into a number that has 
only one non-zero digit using a tail rounding approach. 
This means that at each step we take the last non 0 digit of the number and round it to 0 or to 10. 
If it's less than 5 we round it to 0 if it's larger than or equal to 5 we round it to 10
(rounding to 10 means increasing the next significant digit by 1).
The process stops immediately once there is only one non-zero digit left.

Example

For value = 15, the output should be
rounders(value) = 20;

For value = 1234, the output should be
rounders(value) = 1000.

1234 -> 1230 -> 1200 -> 1000.

For value = 1445, the output should be
rounders(value) = 2000.

1445 -> 1450 -> 1500 -> 2000.
'''
def rounders(a):
    c = len(str(a))
    i = 1
    while i < c:
        p = 10 ** i
        tmp = a % 10 
        a //= 10
        if tmp >= 5:
            a += 1
        i += 1
    return a * 10 ** (c-1)

'''
Consider a robot standing on a 2-dimensional grid at point (0, 0). 
It follows a sequence of instructions.

Each instruction is processed as follows:

'L' decreases the first coordinate by one,
'R' increases the first coordinate by one,
'U' increases the second coordinate by one,
'D' decreases the second coordinate by one.
But the robot isn't allowed to leave a pre-defined square
(with sides parallel to the axes) centered at (0,0).
If the execution of the current instruction would lead to the robot leaving the square, 
that instruction is just ignored.

Given a sequence of instructions and a restricting square, 
output an array of two integers representing the final position of the robot after executing all the instructions.

Example

For instructions = "LLLLUUUUDR" and bound = 2, the output should be
robotPath(instructions, bound) = [-1, 1].

The restricting square is (2, 2), (2, -2), (-2, -2), (-2, 2).
'''
def robotPath(instructions, bound):
    x, y = 0,0
    for i in instructions:
        if i == 'L':
            a = [-1, 0]
        elif  i == 'U':
            a = [0, 1]
        elif i == 'R':
            a = [1, 0]
        else:
            a = [0, -1]
        if abs(x + a[0]) <= bound and abs(y+ a[1]) <= bound :
            x += a[0]
            y += a[1]
    return x,y

'''
Given an array of integers subset and an integer n, find the number of integers between 1 and n, 
inclusive, whose set of divisors contains subset as a subset.

Example

For subset = [2, 3] and n = 13, the output should be
divisorsSubset(subset, n) = 2.
These integers are 6 and 12.
'''
def divisorsSubset(subset, n):
    res = 0
    for i in range(1,n+1):
        flg = 1
        for j in subset:
            if i % j != 0:
                flg = 0
                break
        if flg :
            res += 1
    return res


'''
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

For n = 9, the output should be
isSumOfConsecutive2(n) = 2.

There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
isSumOfConsecutive2(n) = 0.

There are no ways to represent n = 8.
'''
def isSumOfConsecutive2(n):
    res  =0
    i = 1
    while i* 2 < n:
        j = i
        tmp = n
        while tmp >= j:
            tmp -= j
            j += 1
            
        if tmp == 0:
            res += 1
        i+=1
    return res

'''
You are given a rectangular array of characters,
where each symbol '*' can either be replaced with any character or left unchanged, 
whereas all other elements cannot be changed. 
You would like to make the minimum possible number of replacements to make
the array symmetric with respect to both the horizontal and vertical middle axes, i.e. 
such an array that looks the same when flipped horizontally or vertically.

Given array a, return the resulting symmetric array. 
If this symmetry is impossible to obtain, return an empty 2D array instead.

Example

For

a = [['*', '*', 'c', '*'],
     ['*', 'b', '*', 'a'],
     ['a', '*', '*', '*'],
     ['*', '*', 'c', '*']]
the output should be

fastSymmetrization(a) = [['*', 'c', 'c', '*'],
                         ['a', 'b', 'b', 'a'],
                         ['a', 'b', 'b', 'a'],
                         ['*', 'c', 'c', '*']]
For

a = [['*', 'a', 'b', '*'],
     ['*', 'a', 'b', '*']]
the output should be

fastSymmetrization(a) = []
Since only asterisks can be changed, symmetry along the vertical axis is impossible to obtain
'''
def fastSymmetrization(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            u, v = len(a) - i - 1, len(a[0]) - j - 1
            arr = set([a[i][j], a[i][v], a[u][j], a[u][v]])
            if len(arr) > 2 or (len(arr) == 2 and "*" not in arr):
                return []
            arr.discard('*')
            for x in arr:
                a[i][j] = a[i][v] = a[u][j] = a[u][v] = x
    return a

'''
Consider the following template for an equation:

a ? b ? c ? d

Here each letter stands for an integer value, and ?
stands for either an equals sign or a multiplication operator.

You have an array values that contains four integers. 
Can you fill the template with the integers, two multiplication operators, and one equals sign,
such that the resulting equation will be correct?

Example

For values = [2, 4, 3, 6], the output should be
equationTemplate(values) = true.

Here is how the template can be filled to result in a correct equation: 2 * 6 = 3 * 4.

For values = [2, 3, 30, 5], the output should be
equationTemplate(values) = true.

Here is one of the ways to fill the template to get a correct equation: 30 = 2 * 3 * 5.

For values = [2, 3, 5, 5], the output should be
equationTemplate(values) = false.

There is no way to fill the template that will result in a correct equation.
'''
def equationTemplate(values):
    values.sort()
    a,b,c,d  = values
    return a * b == c * d or a * b*c == d or a* c == b* d or a * d == b*c or a == b*c*d


def hangman(word, letters):
    arr = set(list(word))
    miss = 6
    for i in letters:
        if i not in word:
            miss -= 1
        else:
            arr.discard(i)
        if len(arr) == 0:
            return 1
        if miss == 0:
            return 0
    return 0



'''
Given a rectangular matrix consisting of zeroes,
replace each zero with the number of neighboring cells for that cell.

Example

For

matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
the output should be

neighboringCells(matrix) = [[2, 3, 2],
                            [3, 4, 3],
                            [2, 3, 2]]
'''
def neighboringCells(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            r = 0
            if i > 0:
                r += 1
            if i < n-1 :
                r += 1
            if j > 0:
                r += 1
            if j < m -1:
                r += 1
            matrix[i][j] = r
    return matrix