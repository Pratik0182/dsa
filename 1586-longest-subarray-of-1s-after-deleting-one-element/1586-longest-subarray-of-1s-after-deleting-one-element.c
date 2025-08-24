int longestSubarray(int* nums, int numsSize) {
    int l = 0, r = 0, c = 1, max = 0;
    while(r < numsSize){
        if(nums[r] == 0)c--;
        while(c < 0){
            if(nums[l] == 0)c++;
            l++;
        }
        if((r - l + 1) > max)max = r - l + 1;
        r++;
    }
    return max - 1;
}