import java.util.Arrays;

public class SingleNumber260 {
    public int[] singleNumber(int[] nums) {
        int a = 0;
        for (int num: nums) {
            a = a ^ num;
        }

        int b = (a == Integer.MAX_VALUE ? a : a & (-a));
        int c = 0, d = 0;
        for (int num: nums) {
            if ((num & b) != 0) {
                c ^= num;
            } else {
                d ^= num;
            }
        }
        return new int[]{c, d};
    }

    static public void main(String[] args) {
        int[] nums = {1, 2, 1, 3, 2, 5};
        SingleNumber260 solution = new SingleNumber260();
        System.out.println(Arrays.toString(solution.singleNumber(nums)));
    }
}
