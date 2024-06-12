class Solution {
    public void sortColors(int[] nums) {
        quicksort(nums, 0, nums.length-1);
    }

    public void quicksort(int[] nums, int low, int high) {
        if (low < high) {
            int m = low;
            for (int i = low; i <= high; i++) {
                if (nums[i] < nums[low]) {
                    m++;
                    int temp = nums[m];
                    nums[m] = nums[i];
                    nums[i] = temp;
                }
            }
            int temp = nums[m];
            nums[m] = nums[low];
            nums[low] = temp;
            
            quicksort(nums, low, m-1);
            quicksort(nums, m+1, high);
        }
    }
}
