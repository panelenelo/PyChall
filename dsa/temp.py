from icecream import ic



def largest_container(nums: list[int]) -> int:
    i = 0
    j = len(nums)-1
    max_volume = min(nums[i], nums[j]) * (j-i)
    while(i<j):
        if(nums[i]<nums[j]):
            i+=1
        else:
            j-=1
        x =  min(nums[i], nums[j]) * (j-i)
        if (max_volume < x):
            max_volume = x
    return max_volume

def pair_sum_set(nums: list[int], sum: int) -> list[int]:
    ns = set()
    for i in nums:
        x = sum - i
        if(i in ns):
            continue
        else:
            ns.add(i)
        if(x in ns):
            if(nums.index(x) == nums.index(i)):
                continue
            ic(ns)
            return nums.index(x), nums.index(i)
        

def triplet_sum(nums: list[int], sum: int) -> list[int]:
    for i, val in enumerate(nums):
        ns = set()
        for j in nums[i+1:]:
            x = sum - val - j
            if(j in ns):
                continue
            else:
                ns.add(j)
            if(x in ns):
                if(nums.index(x) == nums.index(j)):
                    continue
                ic(nums)
                ic(ns)
                return [nums.index(val), nums.index(x), nums.index(j)]






def main():
    #nums = [2, 7, 8, 3, 7, 6]
    #nums = [0, -1, 2, -3, 1]
    nums = [-1, 2, -3, 1]
    result = triplet_sum(nums, 0)
    ic(result)




if __name__ == "__main__":
    main()
