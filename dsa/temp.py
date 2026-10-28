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










def main():
    nums = [2, 7, 8, 3, 7, 6]
    result = largest_container(nums)
    ic(result)




if __name__ == "__main__":
    main()
