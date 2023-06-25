def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    freq1, freq2 = 0, 0
    for i in range(len(s)):
        freq1 += ord(s[i]) - ord('a')
        freq2 += ord(t[i]) - ord('a')
        
    if freq1 == freq2:
        return True
    return False

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))