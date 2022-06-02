#LINK: https://www.hackerrank.com/challenges/merge-the-tools/problem
#Language: Python
#Difficulty: Medium

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        uniq = ''
        for j in string[i:i+k]:
            if j not in uniq:
                uniq += j
        print(uniq)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
