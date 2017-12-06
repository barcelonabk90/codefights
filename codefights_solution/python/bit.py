'''
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
addTwoDigits(n) = 11.
'''
def addTwoDigits(n):
    return n%10 + n//10

'''
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
largestNumber(n) = 99.
'''
def largestNumber(n):
    return 10**n -1

'''
n children have got m pieces of candy.
They want to eat as much candy as they can, 
but each child must eat exactly the same amount of candy as any other child. 
Determine how many pieces of candy will be eaten by all the children together. 
Individual pieces of candy cannot be split.

Example

For n = 3 and m = 10, the output should be
candies(n, m) = 9.

Each child will eat 3 pieces. So the answer is 9.
'''
def candies(n, m):
    while m >= n:
        if m % n == 0:
            return m
        m -= 1
    return 0
    #return m - m%n
    
'''
Your friend advised you to see a new performance in the most popular theater in the city. 
He knows a lot about art and his advice is usually good, but not this time: 
the performance turned out to be awfully dull. It's so bad you want to sneak out, which is quite simple,
especially since the exit is located right behind your row to the left. 
All you need to do is climb over your seat and make your way to the exit.

The main problem is your shyness: you're afraid that you'll end up blocking the view 
(even if only for a couple of seconds) of all the people who sit behind you and in your column or the columns to your left. 
To gain some courage, you decide to calculate the number of such people and see 
if you can possibly make it to the exit without disturbing too many people.

Given the total number of rows and columns in the theater (nRows and nCols, respectively), 
and the row and column you're sitting in, return the number of people who sit strictly behind you and 
in your column or to the left, assuming all seats are occupied.

Example

For nCols = 16, nRows = 11, col = 5 and row = 3, the output should be
seatsInTheater(nCols, nRows, col, row) = 96.
'''    
def seatsInTheater(nCols, nRows, col, row):
    return (nCols - col + 1) * (nRows- row)



'''
Given a divisor and a bound, find the largest integer N such that:

N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
It is guaranteed that such a number exists.

Example

For divisor = 3 and bound = 10, the output should be
maxMultiple(divisor, bound) = 9.

The largest integer divisible by 3 and not larger than 10 is 9.
'''
def maxMultiple(divisor, bound):
    # while bound >= divisor:
    #     if bound % divisor == 0:
    #         return bound
    #     bound -= 1
    # return 0
    return bound - bound % divisor


'''
Consider integer numbers from 0 to n - 1 written down along the circle in such a way 
that the distance between any two neighbouring numbers is equal (note that 0 and n - 1 are neighbouring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.
'''
def circleOfNumbers(n, firstNumber):
    return (n/2 + firstNumber) % n

'''
One night you go for a ride on your motorcycle. 
At 00:00 you start your engine, 
and the built-in timer automatically begins counting the length of your ride, in minutes.
Off you go to explore the neighborhood.

When you finally decide to head back, 
you realize there's a chance the bridges on your route home are up, leaving you stranded!
Unfortunately, you don't have your watch on you and don't know what time it is. 
All you know thanks to the bike's timer is that n minutes have passed since 00:00.

Using the bike's timer, calculate the current time.
Return an answer as the sum of digits that the digital timer in the format hh:mm would show.

Example

For n = 240, the output should be
lateRide(n) = 4.

Since 240 minutes have passed, the current time is 04:00. 
The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.

For n = 808, the output should be
lateRide(n) = 14.

808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.
'''
def lateRide(n):
    h = n // 60
    m = n % 60
    return h//10 + h % 10 + m //10 + m % 10


'''
Some phone usage rate may be described as follows:

first minute of a call costs min1 cents,
each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
each minute after 10th costs min11 cents.
You have s cents on your account before the call. 
What is the duration of the longest call (in minutes rounded down to the nearest integer) you can have?

Example

For min1 = 3, min2_10 = 1, min11 = 2 and s = 20, the output should be
phoneCall(min1, min2_10, min11, s) = 14.

Here's why:

the first minute costs 3 cents, which leaves you with 20 - 3 = 17 cents;
the total cost of minutes 2 through 10 is 1 * 9 = 9, so you can talk 9 more minutes and still have 17 - 9 = 8 cents;
each next minute costs 2 cents, which means that you can talk 8 / 2 = 4 more minutes.
Thus, the longest call you can make is 1 + 9 + 4 = 14 minutes long.
'''
def phoneCall(min1, min2_10, min11, s):
    if s < min1:
        return 0
    r = 1
    t = s - min1
    k = t // min2_10
    if k < 9:
        return r + k
    r += 9
    t -= 9*min2_10
    return r + t//min11

'''
Given integers a and b, determine whether the following pseudocode results in an infinite loop

while a is not equal to b do
  increase a by 1
  decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.

Example

For a = 2 and b = 6, the output should be
isInfiniteProcess(a, b) = false;
For a = 2 and b = 3, the output should be
isInfiniteProcess(a, b) = true.
'''
def isInfiniteProcess(a, b):
    while b > a:
        a += 1
        b -= 1
    return a != b

'''
In tennis, a set is finished when one of the players wins 6 games and the other one wins less than 5, or, 
if both players win at least 5 games, until one of the players wins 7 games.

Determine if it is possible for a tennis set to be finished with the score score1 : score2.

Example

For score1 = 3 and score2 = 6, the output should be
tennisSet(score1, score2) = true.

For score1 = 8 and score2 = 5, the output should be
tennisSet(score1, score2) = false.

Since both players won at least 5 games, the set would've ended once one of them won the 7th one.

For score1 = 6 and score2 = 5, the output should be
tennisSet(score1, score2) = false.
'''
def tennisSet(score1, score2):
    ma = max(score1, score2)
    mi = min(score1, score2)
    return ma == 6 and mi < 5 or ma == 7 and mi in [5,6]


'''
In order to stop the Mad Coder evil genius you need to decipher
the encrypted message he sent to his minions. 
The message contains several numbers that, when typed into a supercomputer,
will launch a missile into the sky blocking out the sun, and making all the people on Earth grumpy and sad.

You figured out that some numbers have a modified single digit in their binary representation.
More specifically, in the given number n the kth bit from the right was initially set to 0,
but its current value might be different.
It's now up to you to write a function that will change the kth bit of n back to 0.

Example

For n = 37 and k = 3, the output should be
killKthBit(n, k) = 33.

3710 = 1001012 ~> 1000012 = 3310.

For n = 37 and k = 4, the output should be
killKthBit(n, k) = 37.

The 4th bit is 0 already (looks like the Mad Coder forgot to encrypt this number), so the answer is still 37.
'''
def killKthBit(n, k):
    return n & ~(1 << (k - 1)) 
    #return n & ~(2**(k-1))
    
    
'''
You are given an array of up to four non-negative integers, each less than 256.

Your task is to pack these integers into one number M in the following way:

The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.
Return the obtained integer M.

Note: the phrase "first bits of M" refers to the least significant bits of M -
the right-most bits of an integer. For further clarification see the following example.

Example

For a = [24, 85, 0], the output should be
arrayPacking(a) = 21784.

An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.
After packing these into one number we get 00000000 01010101 00011000 (spaces are placed for convenience),
which equals to 21784.
'''    
def arrayPacking(a):
    # r = 0
    # for i in range(len(a)):
    #     r += a[i] << 8 * i
    # return r
    return sum(a[i] << 8 * i for i in range(len(a)))

'''
You are given two numbers a and b where 0 ≤ a ≤ b.
Imagine you construct an array of all the integers from a to b inclusive.
You need to count the number of 1s in the binary representations of all the numbers in the array.

Example

For a = 2 and b = 7, the output should be
rangeBitCount(a, b) = 11.

Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7]. 
Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111], 
which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.
'''
def rangeBitCount(a, b):
    # r = 0
    # for i in range(a,b+1):
    #     r += bin(i).count("1")
    # return r
    return sum(bin(i).count("1") for i in range(a,b+1))

'''
Reverse the order of the bits in a given integer.

Example

For a = 97, the output should be
mirrorBits(a) = 67.

97 equals to 1100001 in binary, which is 1000011 after mirroring, and that is 67 in base 10.

For a = 8, the output should be
mirrorBits(a) = 1.
'''
def mirrorBits(a):
    return int(bin(a)[2:][::-1],2)


'''
Presented with the integer n, 
find the 0-based position of the second rightmost zero bit in its binary representation 
(it is guaranteed that such a bit exists), counting from right to left.

Return the value of 2position_of_the_found_bit.

Example

For n = 37, the output should be
secondRightmostZeroBit(n) = 8.

3710 = 1001012. The second rightmost zero bit is at position 3 (0-based) from the right in the binary representation of n.
Thus, the answer is 23 = 8.
'''
def secondRightmostZeroBit(n):
    return (((((n + 1) | n) + 1) | n) - n)
    #return -~((n-~(n^(n+1))//2)^(n-~(n^(n+1))//2+1))//2
    
'''
You're given an arbitrary 32-bit integer n. Take its binary representation, 
split bits into it in pairs (bit number 0 and 1, bit number 2 and 3, etc.) and swap bits in each pair. 
Then return the result as a decimal number.

Example

For n = 13, the output should be
swapAdjacentBits(n) = 14.

1310 = 11012 ~> {11}{01}2 ~> 11102 = 1410.

For n = 74, the output should be
swapAdjacentBits(n) = 133.

7410 = 010010102 ~> {01}{00}{10}{10}2 ~> 100001012 = 13310.
Note the preceding zero written in front of the initial number: 
since both numbers are 32-bit integers, they have 32 bits in their binary representation. 
The preceding zeros in other cases don't matter, so they are omitted. Here, however, it does make a difference.
'''    
def swapAdjacentBits(n):
    return ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)

'''
You're given two integers, n and m. 
Find position of the rightmost bit in which they differ in their binary representations 
(it is guaranteed that such a bit exists), counting from right to left.

Return the value of 2position_of_the_found_bit (0-based).

Example

For n = 11 and m = 13, the output should be
differentRightmostBit(n, m) = 2.

1110 = 10112, 1310 = 11012, the rightmost bit in which they differ is the bit at position 1 (0-based) 
from the right in the binary representations.
So the answer is 21 = 2.

For n = 7 and m = 23, the output should be
differentRightmostBit(n, m) = 16.

710 = 1112, 2310 = 101112, i.e.

00111
10111
So the answer is 24 = 16.
'''
def differentRightmostBit(n, m):
    return (n ^m) & -(n^m)


'''
You're given two integers, n and m. 
Find position of the rightmost pair of equal bits in their binary representations 
(it is guaranteed that such a pair exists), counting from right to left.

Return the value of 2position_of_the_found_pair (0-based).

Example

For n = 10 and m = 11, the output should be
equalPairOfBits(n, m) = 2.

1010 = 10102, 1110 = 10112, the position of the rightmost pair of equal bits is the bit at position 1 
(0-based) from the right in the binary representations.
So the answer is 21 = 2.
'''
def equalPairOfBits(n, m):
    return n + m + 1 & ~m - n