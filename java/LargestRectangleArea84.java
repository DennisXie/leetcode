import java.util.Arrays;
import java.util.Stack;

public class LargestRectangleArea84 {
    /**
     * We enum the heights[i] to be the lowest post(or the rectangle's height).
     * So we need to know the index of the nearest miner heights[j] on the both
     * side. The nearest miner or bigger thing can remind us of monotonic stack.
     * @param heights
     * @return
     */
    public int largestRectangleArea(int [] heights) {
        int[] left = new int[heights.length];
        int[] right = new int[heights.length];
        Stack<Integer> stack = new Stack<>();

        for (int i = heights.length-1; i >= 0; i--) {

            while (stack.size() > 0 && heights[stack.peek()] >= heights[i]) {
                stack.pop();
            }

            if (stack.size() > 0 ) {
                right[i] = stack.peek();
            } else {
                right[i] = heights.length;
            }
            stack.push(i);
        }


        stack.clear();
        for (int i = 0; i < heights.length; i++) {
            while (stack.size() > 0 && heights[stack.peek()] >= heights[i]) {
                stack.pop();
            }

            if (stack.size() > 0) {
                left[i] = stack.peek();
            } else {
                left[i] = -1;
            }
            stack.push(i);
        }

        int maxArea = 0;
        for (int i = 0; i < heights.length; i++) {
            int length = right[i] - left[i] - 1;
            maxArea = Math.max(maxArea, heights[i] * length);
        }
        System.out.println(Arrays.toString(left));
        System.out.println(Arrays.toString(right));

        return maxArea;
    }

    static public void main(String[] args) {
        LargestRectangleArea84 solution = new LargestRectangleArea84();
        int[] heights = {1, 1, 1};
        System.out.println(solution.largestRectangleArea(heights));
    }
}
