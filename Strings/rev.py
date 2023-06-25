def rev(sent):
    ans = sent[::-1]
    return ans
        
if __name__ == '__main__':
    sent = input("Enter a string: ")
    print(rev(sent))