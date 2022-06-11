#LINK: https://www.hackerrank.com/challenges/itertools-permutations
#Language: Python
#Difficulty: Easy



from itertools import permutations

s, k = (input().split())

list_perm = (list(permutations(s,int(k))))

list_perm.sort()

for i in list_perm:
    print("".join(i))
