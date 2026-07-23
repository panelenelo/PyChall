from icecream import ic






def main():
    data = []
    with open('text2.txt', 'r') as f:
        data = f.read()

    for i in data:
        if (64 < ord(i) < 91 or 96 < ord(i) < 123):
            ic(i)

    
    

    









if __name__ == "__main__":
    main()