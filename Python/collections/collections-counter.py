
#LINK: https://www.hackerrank.com/challenges/collections-counter
#Language: Python
#Difficulty: Easy


from collections import Counter

n_of_shoes = int(input())
size = list(map(int, input().split(' ')))
size_availability = Counter(size)
n_of_customers = int(input())

income = 0

for i in range(n_of_customers):
    size, price = map(int, input().split(' '))
    if size_availability[size]:
        income += price
        size_availability[size] -=1
        
print(income)
