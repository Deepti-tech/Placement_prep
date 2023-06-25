def palindrome(string):
    string = [char.lower() for char in string if char.isalnum()]
    revStr = string[::-1]
    if revStr == string:
        return True
    return False

string = "abcdcba"
print(palindrome(string))