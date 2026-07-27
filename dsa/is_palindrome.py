from icecream import ic

def is_palindrome(words: str) -> bool:
    l = 0
    r = len(words)-1
    while(l<r):
        left = words[l]
        right = words[r]
        while not(ord(left)>96 and ord(left)<123):
            l+=1
            left = words[l]
        while not(ord(right)>96 and ord(right)<123):
            r-=1
            right = words[r]
        if (ord(left) != ord(right)):
            return False
        r-=1
        l+=1
    return True


def main():
    words = "a dog! a panic in a pagoda."
    # words = "aaccca.........a"
    result = is_palindrome(words)

    ic(result)


    
    

    







if __name__ == "__main__":
    main()