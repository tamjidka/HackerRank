#LINK: https://www.hackerrank.com/challenges/no-idea
#Language: Python
#Difficulty: Medium

n, m = map(int, input().split())

arr = list(map(int, input().split()))

listA = set(map(int, input().split()))
listB = set(map(int, input().split()))

count = 0

for i in range(len(arr)):
    if arr[i] in listA:
        count += 1
    if arr[i] in listB:
        count -=1
        
print(count)
