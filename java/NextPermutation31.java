import java.util.Arrays;

public class NextPermutation31 {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 1;
        int idx = -1;
        int minIdx = -1;
        while (i > 0) {
            if (nums[i] > nums[i - 1]) {
                idx = i - 1;
                minIdx = i;
                break;
            }
            i--;
        }

        if (idx == -1) {
            Arrays.sort(nums);
            return;
        }

        for (i = idx + 1; i < nums.length; i++) {
            if (nums[i] > nums[idx] && nums[i] < nums[minIdx]) {
                minIdx = i;
            }
        }

        i = nums[idx];
        nums[idx] = nums[minIdx];
        nums[minIdx] = i;

        Arrays.sort(nums, idx+1, nums.length);
    }

    public void nextPermutation2(int[] nums) {
        int i = nums.length - 1;
        int idx = -1;
        while (i > 0) {
            if (nums[i] > nums[i - 1]) {
                idx = i - 1;
                break;
            }
            i--;
        }

        int j =  nums.length - 1;
        while (i < j) {
            nums[i] = nums[j] ^ nums[i];
            nums[j] = nums[j] ^ nums[i];
            nums[i] = nums[j] ^ nums[i];
            i++;
            j--;
        }

        if (idx != -1) {
            for (i = idx + 1; i < nums.length; i++) {
                if (nums[i] > nums[idx]) {
                    nums[i] = nums[idx] ^ nums[i];
                    nums[idx] = nums[idx] ^ nums[i];
                    nums[i] = nums[i] ^ nums[idx];
                    break;
                }
            }
        }
    }

    static public void main(String[] args) {
        int[] nums = {1, 7, 2, 9, 8, 2, 1};
        NextPermutation31 solution = new NextPermutation31();
        solution.nextPermutation(nums);
        System.out.println(Arrays.toString(nums));
    }
}
