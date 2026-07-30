from icecream import ic


def par_sum_sorted(nums: list[int], target:int) -> list[int]:
    l = 0
    r = len(nums)-1
    while l<r:
        sum = nums[l]+ nums[r]
        if(sum == target):
            return [l, r]
        if(sum < target):
            l+=1
        if(sum > target):
            r-=1

def par_sum(nums:list[int], target:int) -> list[int]:
    pass




def main():
    nums = [2, 2, 3]
    target = 5
    result = par_sum_sorted(nums, target)
    ic(result)


    
    

    









if __name__ == "__main__":
    main()