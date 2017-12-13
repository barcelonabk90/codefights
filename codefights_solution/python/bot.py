'''
Before delivery, all orders at Jet are packed into boxes to protect them from damage.

Consider a package pkg of a given size that needs to be packed into a box chosen from a list of available boxes. 
The package should fit inside the box, 
keeping in mind that the size of the package should not exceed the size of the box in any dimension 
(note that the package can be rotated to fit and it can be positioned upside down).
For the sake of efficiency, among the available boxes that fit, the one with smallest volume should be chosen.

Given a package pkg and available boxes, 
find the 0-based index of the smallest-by-volume box such that the package fits inside it, 
or return -1 if there is no such box.

Example

For pkg = [4, 2, 5] and boxes = [[4, 3, 5], [5, 2, 5]], the output should be
packageBoxing(pkg, boxes) = 1.
The package fits into both boxes, but the volume of the first one (4 * 3 * 5 = 60)
is greater than the volume of the second (5 * 5 * 2 = 50).

For pkg = [4, 4, 2] and boxes = [[2, 4, 4], [4, 4, 3]], the output should be
packageBoxing(pkg, boxes) = 0.
The package can fit into the first box if it is rotated, and into the second box as-is, 
but the first box is chosen because it has less volume overall.

For pkg = [4, 5, 3] and boxes = [[3, 10, 2], [2, 6, 7], [1, 1, 1]], the output should be
packageBoxing(pkg, boxes) = -1.
The package doesn't fit into any of the available boxes.
'''
def packageBoxing(pkg, boxes):
    
    arr = sorted(boxes, key = product)
    pkg.sort()
    for box in arr:
        flg = 1
        tmp = sorted(box)
        for i in range(3):
            if pkg[i] > tmp[i]:
                flg = 0
                break
        if flg:
            return boxes.index(box)
    return -1
                
    
def product(a):
    r = 1
    for i in a:
        r *= i
    return r

def catalogUpdate(catalog, updates):
    for a in updates:
        flg = 0
        for i in range(len(catalog)):
            tmp = catalog[i]
            if a[0] == tmp[0]:
                flg = 1
                #merge 
                arr = tmp[1:] + a[1:]
                catalog[i] = [tmp[0]] + sorted(arr)
                break
        # add new
        if not flg:
            catalog.append(a)
            insertionSort(catalog)
    return catalog
            
def insertionSort(arr):
# Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
        
def catalogUpdate(catalog, updates):
    for u in updates:
        found = False
        for c in catalog:
            if c[0] == u[0]:
                found = True
                c.append(u[1])
                c[1:len(c)] = sorted(c[1:len(c)])
        if found == False:
                catalog.append(u)
    return sorted(catalog)



'''
One Very Important User (VIU) has a Very Confidential Document (VCD) stored on his Dropbox account.
He doesn't let anyone see the VCD, especially his roommates who often have access to his devices.

Opening the Dropbox mobile app on the VIU's tablet requires a four-digit passcode. 
To ensure the confidentiality of the stored information, 
the device is locked out of Dropbox after 10 consecutive failed passcode attempts.
We need to implement a function that given an array of attempts made throughout
the day and the correct passcode checks to see if the device should be locked, i.e.
10 or more consecutive failed passcode attempts were made.

Example

For
passcode = "1111" and

attempts = ["1111", "4444",
            "9999", "3333",
            "8888", "2222",
            "7777", "0000",
            "6666", "7285",
            "5555", "1111"]
the output should be
incorrectPasscodeAttempts(passcode, attempts) = true.

The first attempt is correct, so the user must have successfully logged in.
However, the next 10 consecutive attempts are incorrect, so the device should be locked.
Thus, the output should be true.

For
passcode = "1234" and

attempts = ["9999", "9999",
            "9999", "9999",
            "9999", "9999",
            "9999", "9999",
            "9999", "1234",
            "9999", "9999"]
the output should be
incorrectPasscodeAttempts(passcode, attempts) = false.

There are only 9 consecutive incorrect attempts, so there's no need to lock the device.
'''
def incorrectPasscodeAttempts(passcode, attempts):
    i = 0
    for a in attempts:
        if a == passcode:
            i = 0
        else:
            i += 1
        if i == 10:
            return 1
    return 0



'''
In its effort to push the limits of file compression,
Dropbox recently developed a lossless compression algorithm for H.264 and JPEG files.
Since you are thinking about applying for a job at Dropbox, 
you decided to experiment with simple lossless compression as part of your interview prep.

One of the most widely known approaches in the field of compression algorithms is sliding window compression. 
It works as follows:

Consider characters one by one. Let the current character index be i.
Take the last width characters before the current one (i.e. s[i - width, i - 1], 
where s[i, j] means the substring of s from index i to index j, both inclusive), and call it the window.
If there are less than width characters before the current one, then you should use s[0, i - 1] as the window.
Find such startIndex and length that s[i, i + length - 1] = s[startIndex, startIndex + length - 1] and s[startIndex,
startIndex + length - 1] is contained within the window. 
If there are several such pairs, choose the one with the largest length. 
If there still remains more than one option, choose the one with the smallest startIndex.
If the search was successful, append "(startIndex,length)" to the result and move to the index i + length.
Otherwise, append the current character to the result and move on to the next one.
Given a string, apply sliding window compression to it.

Example

For inputString = "abacabadabacaba" and width = 7, the output should be
losslessDataCompression(inputString, width) = "ab(0,1)c(0,3)d(4,3)c(8,3)".

Step 1: i = 0, inputString[i] = 'a', window = "". 'a' is not contained within the window,
so it is appended to the result.
Step 2: i = 1, inputString[i] = 'b', window = "a". 'b' is not contained within the window, 
so it is appended to the result.
Step 3: i = 2, inputString[i] = 'a', window = "ab". 'a' can be found in the window.
'a' in the window corresponds to the inputString[0], so (0,1) representing the substring "a" is appended to the result.
Step 4: i = 3, inputString[i] = 'c', window = "aba". The same situation as in the first two steps.
Step 5: i = 4, inputString[i] = 'a', window = "abac". Consider startIndex = 0, length = 3.
inputString[startIndex, startIndex + length - 1] = "aba" and it is contained within the window, 
inputString[i, i + length - 1] = "aba". Therefore, "(0,3)" should be added to the result. i += length.

Step 6: i = 7, inputString[i] = 'd', window = inputString[0, 6] = "abacaba". The same situation as in the first two steps.
Step 7: i = 8, inputString[i] = 'a', window = inputString[1, 7] = "bacabad".
Consider length = 3 again. inputString[i, i + b - 1] = "aba", window[3, 5] = "aba",
and it corresponds to inputString[4, 6] since inputString[0, 2] is no longer within the window. 
So, "(4,3)" should be appended. i += length.
Step 8: i = 11, inputString[i] = 'c', window = "abadaba". The same situation as at the first two steps.
Step 9: i = 12, inputString[i] = 'a', window = "badabac". length = 3, inputString[i, i + length - 1] = "aba",
window[3, 5] = "aba", and it corresponds to inputString[8, 10]. So, "(8,3)" should be appended. i += length.


For inputString = "abacabadabacaba" and width = 8, the output should be
losslessDataCompression(inputString, width) = "ab(0,1)c(0,3)d(0,7)".

In both of the above examples the resulting "compressed" string becomes even longer than the initial one.
In fact, sliding window compression proves to be efficient for longer inputs.

For inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa" and width = 12, the output should be
losslessDataCompression(inputString, width) = "a(0,1)(0,2)(0,4)(0,8)(4,12)".

In the last example the resulting string is one character shorter than the input one. 
It is the shortest possible example of the efficient work of sliding window compression. 
If the input contained even more letters 'a', 
then the effect of this approach would be even more considerable.
'''
def losslessDataCompression(s, w):
    res = s[0]
    i = 1
    while i < len(s):
        tmp = s[max(0,i-w):i]
        c = s[i]
        if c not in tmp:
            res += c
            i+=1
        else:
            for j in range(w+1, 0 , -1):
                for k in range(max(0,i-w),i):
                    if s[k:k+j] in tmp and s[i:i+j]==s[k:k+j]:
                        break
                if s[k:k+j] in tmp and s[i:i+j]==s[k:k+j]:
                        break
            res += "("+str(k)+","+str(j)+")"
            i += j
    
    return res
