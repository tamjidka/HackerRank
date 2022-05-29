
#LINK: https://www.hackerrank.com/challenges/the-minion-game/problem
#Language: Python
#Difficulty: Medium


def minion_game(string):
    string_len = len(string)
    const = vowel = 0
    
    for i in range(string_len):
        if s[i] in 'AEIOU':
            vowel = vowel + (string_len-i)
        else:
            const = const + (string_len-i)
            
    if const > vowel:
        print('Stuart', const)
    elif vowel > const:
        print ('Kevin', vowel)
    else:
        print('Draw')
            
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
