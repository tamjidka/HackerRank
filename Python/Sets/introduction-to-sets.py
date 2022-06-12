#LINK: https://www.hackerrank.com/challenges/py-introduction-to-sets
#Language: Python
#Difficulty: Easy

def average(array):
    
    distinct_numbers = list(set((array))) #get distinct numbers in list
    sum = 0
    len_distinct_numbers = len(distinct_numbers) #get length of distinct_numbers list
    
    for i in range(len(distinct_numbers)):
        sum += distinct_numbers[i]       #sum 
    return round((sum/float(len_distinct_numbers)),3) #get float number and round it to 3 decimal places
  
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

