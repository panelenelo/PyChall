from icecream import ic


def zero_striping(nums: list[list[int]]) -> list[list[int]]:
    maps = []

    for i, v in enumerate(nums):
        maps.append(dict())
        for j, c in enumerate(v):
            maps[i][j] = c

    for i, m in maps:
        if(0 in m):
            col = m[]
    




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