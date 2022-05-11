import java.util.Arrays;

public class RemoveDuplicates80 {
    public int removeDuplicates(int[] nums) {
        int i = 0, j = -1, sameCount = 0, comp = 10002;
        while (i < nums.length) {

            if (nums[i] == comp) {
                sameCount += 1;
            } else {
                sameCount = 0;
            }

            if (sameCount > 1 && j == -1) {
                j = i;
            }

            if (sameCount <= 1 && j != -1) {
                nums[j] = nums[i];
                j++;
            }
            comp = nums[i];
            i++;
        }
        return j == -1 ? nums.length : j;
    }

    static public void main(String[] args) {
        int[] nums = {1, 1, 1, 1, 1, 1};
        RemoveDuplicates80 solution = new RemoveDuplicates80();
        System.out.println(solution.removeDuplicates(nums));
        System.out.println(Arrays.toString(nums));
    }
}
