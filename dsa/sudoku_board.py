from icecream import ic


def sudoku_board(nums: list[list[int]]) -> bool:
    #for i, v in enumerate(nums):
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    grid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(0,9):
        for j in range(0,9):
            num = nums[i][j]
            if(num == 0):
                continue
            if((num in row_sets[i]) or (num in col_sets[j]) or (num in grid_sets[i//3][j//3])):
                return False
            else:
                row_sets[i].add(num)
                col_sets[j].add(num)
                grid_sets[i//3][j//3].add(num)
            
    return True


    




def main():
    # nums = [
        # [3, 0, 0, 0, 3, 2, 0, 0, 6],
        # [4, 7, 0, 1, 0, 2, 0, 0, 8],
        # [0, 0, 0, 4, 0, 1, 0, 4, 0],
        # [0, 0, 0, 0, 5, 0, 0, 7, 0],
        # [0, 7, 0, 0, 3, 0, 0, 0, 0],
        # [8, 0, 7, 0, 0, 0, 0, 0, 0],
        # [8, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 4, 0, 5, 0, 0],
        # [0, 0, 0, 2, 8, 0, 4, 5, 0]
    # ]
    nums = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    result = sudoku_board(nums)
    ic(result)


    
    

    









if __name__ == "__main__":
    main()