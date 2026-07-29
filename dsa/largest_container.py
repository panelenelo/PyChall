from icecream import ic


def largest_container(nums: list[int]) -> int:
    result = 0
    i=0
    j=len(nums)-1
    while i<j:
        water = min(nums[i], nums[j]) * (j-i)
        if(water>result):
            result = water
        if(nums[i]<nums[j]):
            i+=1
        else:
            j-=1
    return result





def main():
    nums = [2, 7, 8, 3, 7, 6]
    result = largest_container(nums)
    ic(result)


    
    

    









if __name__ == "__main__":
    main()
