nums = [1,2,2,3]
i=1; ls1 = [];

while(i<len(nums)):
    if(nums[i]==nums[i-1]):
        nums.pop(i-1)
        i+=1
    else:
        i+=1
print nums
