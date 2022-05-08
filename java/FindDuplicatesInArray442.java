import java.util.ArrayList;
import java.util.List;

public class FindDuplicatesInArray442 {
    public List<Integer> findDuplicates(int[] nums) {
        ArrayList<Integer> results = new ArrayList<>();

        int i = 0;
        while (i < nums.length) {
            if (nums[i] != i+1 && nums[nums[i]-1] != nums[i]) {
                int x = nums[i];
                nums[i] = nums[x-1];
                nums[x-1] = x;
            } else {
                i++;
            }
        }

        for (i = 0; i < nums.length; i++) {
            if (nums[i] != i+1) {
                results.add(nums[i]);
            }
        }

        return results;
    }

    static public void main(String[] args) {
        int[] nums = new int[]{4, 3, 2, 7, 8, 2, 3, 1};
        FindDuplicatesInArray442 solution = new FindDuplicatesInArray442();
        System.out.println(solution.findDuplicates(nums));
    }
}
