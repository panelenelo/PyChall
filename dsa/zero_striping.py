from icecream import ic


def zero_striping(nums: list[list[int]]) -> list[list[int]]:
    rows = set()
    cols = set()

    for i,v in enumerate(nums):
        for j, c in enumerate(v):
            if(c == 0):
                rows.add(i)
                cols.add(j)

    for i, v in enumerate(nums):
        for j, c in enumerate(v):
            if((i in rows) or (j in cols)):
                nums[i][j] = 0

    ic(rows)
    ic(cols)
    ic(nums)


    




def main():
    nums = [
        [1 , 2 , 3 , 4 , 5 ],
        [6 , 0 , 8 , 9 , 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 0 ]        
    ]
    result = zero_striping(nums)
    ic(result)


    
    

    









if __name__ == "__main__":
    main()