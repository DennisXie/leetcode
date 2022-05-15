import java.util.Stack;

public class OneThreeTwoPattern456 {
    public boolean find132pattern(int[] nums) {
        if (nums.length < 3) {
            return false;
        }

        int min = 0;
        int max = 0;
        Stack<Integer> stack = new Stack<>();
        for (int num: nums) {
            if (stack.size() >= 2 && stack.peek() > num && stack.firstElement() < num) {
                return true;
            }

            while (stack.size() > 0 && stack.peek() >= num) {
                stack.pop();
            }

            stack.push(num);
        }
        return false;
    }

    static public void main(String[] args) {
        int[] nums = {4, 6, 8, 1, 3, 2};
        // int[] nums = {1, 2, 3, 4, 5};
        OneThreeTwoPattern456 solution = new OneThreeTwoPattern456();
        System.out.println(solution.find132pattern(nums));
    }
}
