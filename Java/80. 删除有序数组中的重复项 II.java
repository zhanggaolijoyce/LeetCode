class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        if (n <= 2){
            return n;
        }
        int k = 0;
        for (int i = 0; i < n-2; i ++) {
            if (nums[i] == nums[i+1] && nums[i] == nums[i+2]){
                continue;
            } else {
                nums[k] = nums[i];
                k ++;
            }
        }
        nums[k] = nums[n-2];
        nums[k+1] = nums[n-1];
        return k+2;
    }
}
