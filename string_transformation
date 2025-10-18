#Exercise: String Transformation
#
#Problem:
#Write a that takes an array of strings and returns a new array with the following rules:
#
#If a string has even length, convert it to uppercase.
#
#If a string has odd length, reverse it.
#
#If a string starts and ends with the same letter (case-insensitive), append its length at the end after the previous transformation.
#
#Example:
#Input: ["apple", "banana", "kiwi", "level", "noon", "grape"]
#Output: ["elppa", "BANANA", "KIWI", "LEVEL5", "NOON4", "eparg"]

def solution(arr):
    result = []
    for s in arr:
        # Step 1: transform by length
        transformed = s.upper() if len(s) % 2 == 0 else s[::-1]
        
        # Step 2: append length if first and last char match (case-insensitive)
        if s[0].lower() == s[-1].lower():
            transformed += str(len(s))
        
        result.append(transformed)
    return result

# Test cases
print(solution(["apple", "banana", "kiwi", "lavel", "noon", "grape"]))
# Output: ['elppa', 'BANANA', 'KIWI', 'LEVEL5', 'NOON4', 'eparg']

print(solution(["rider", "moon", "sun", "chesc", "sky"]))
# Output: ['RADAR5', 'MOON4', 'nus', 'CIVIC5', 'yks']
