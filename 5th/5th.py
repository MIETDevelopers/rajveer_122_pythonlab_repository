'''Purpose:Write a program to reverse every kth row in a matrix.
Author: Kavya Dhar
'''
# initializing list
test_list = [[5, 3, 2], [8, 6, 3], [3, 5, 2],
             [3, 6], [3, 7, 4], [2, 9]]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing K
K = 3
 
res = []
for idx, ele in enumerate(test_list):
 
    # checking for K multiple
    if (idx + 1) % K == 0:
 
        # reversing using reversed
        res.append(list(reversed(ele)))
    else:
        res.append(ele)
 
# printing result
print("After reversing every Kth row: " + str(res))
