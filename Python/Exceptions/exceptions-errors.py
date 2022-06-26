#LINK: https://www.hackerrank.com/challenges/exceptions/problem
#Language: Python
#Difficulty: Easy



n = int(input())

for i in range(n):
    try:
        a, b = map(int, input().split())
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
        
