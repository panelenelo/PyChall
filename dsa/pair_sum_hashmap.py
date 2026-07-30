from icecream import ic


def par_sum_hashmap(nums: list[int], target:int) -> list[int]:
    hashset = set()
    for i in nums:
        x = target - i
        if i in hashset:
            continue
        else:
            hashset.add(i)
        if (x in hashset):
            ic(hashset)
            return [nums.index(x), nums.index(i)]




def main():
    nums = [-1, 3, 4, 2]
    target = 3
    result = par_sum_hashmap(nums, target)
    ic(result)


    
    

    









if __name__ == "__main__":
    main()