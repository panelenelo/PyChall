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

    return nums

def zero_striping_inplace(nums: list[list[int]]) -> list[list[int]]:
    row_has_zero = False
    col_has_zero = False
    r = len(nums)
    c = len(nums[0])

    for i in range(r):
        if(nums[i][0] == 0):
            row_has_zero = True
            break

    for j in range(c):
        if(nums[0][j] == 0):
            col_has_zero = True
            break

    for i in range(r):
        for j in range(c):
            if(nums[i][j] == 0):
                nums[i][0] = 0
                nums[0][j] = 0

    for i in range(1, r):
        for j in range(1, c):
            if (nums[0][j] == 0 or nums[i][0] == 0):
                nums[i][j] = 0

    if(row_has_zero == True):
        for i in range(r):
            nums[i][0] = 0

    if(col_has_zero == True):
        for j in range(c):
            nums[0][j] = 0

    
    return nums




def main():
    nums = [
        [1 , 2 , 3 , 4 , 5 ],
        [6 , 0 , 8 , 9 , 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 0 ]        
    ]
    result = zero_striping_inplace(nums)
    ic(result)


    
    

    









if __name__ == "__main__":
    main()