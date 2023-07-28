import sys
sys.stdin = open('input.txt')

char = input()

if char.isupper():
    result = char.lower()
else:
    result = char.upper()

    print(char, result)
    print(ord(char), ord(result))