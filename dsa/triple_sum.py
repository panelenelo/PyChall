from icecream import ic


def triple_sum_sorted(nums: list[int], target:int) -> list[int]:
    # Choose a x number and find a pair that summed to x is equal to target
    l = 1
    r = len(nums)-1
    fix = 0
    while(fix < len(nums)-2):
        while (l < r):
            sum = nums[l]+nums[r]+nums[fix]
            if (sum == target):
                return [l, r, fix]
            if (sum > target):
                r-=1
            if (sum < target):
                l+=1
        fix=+1
        l=fix+1
        r = len(nums)-1
    return [-1]

def triple_sum(nums:list[int], target:int) -> list[int]:
    pass




def main():
    nums = [0,0,0]
    target = 0
    result = triple_sum_sorted(nums, target)

    if (result[0] == -1):
        ic("not found in list")
        return

    ic(result)


    
    

    









if __name__ == "__main__":
    main()