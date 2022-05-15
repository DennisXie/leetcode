import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Iterator;
import java.util.Stack;
import java.util.stream.IntStream;
import java.util.stream.StreamSupport;

public class MaxRectangle85 {
    /**
     * Similar to the 84. We enumerate each row as the rectangle's bottom edge,
     * we can calculate the height of each index depending on the last row's height.
     * The defines of the height is the continuous '1' on the vertical. Then this
     * question becomes find the answer of 84 on each row.
     * @param matrix
     * @return
     */
    public int maximalRectangle(char[][] matrix) {
        short rows = (short) matrix.length;
        short cols = (short) matrix[0].length;
        int[] heights = new int[cols];
        for (int j = 0; j < cols; j++) {
            heights[j] = 0;
        }

        int[] left = new int[cols];
        int[] right = new int[cols];
        Stack<Integer> stack = new Stack<>();

        int maxArea = 0;
        for (short i = 0; i < rows; i++) {
            for (short j = 0; j < cols; j++) {
                heights[j] = matrix[i][j] == '1' ? heights[j] + 1 : 0;
            }
            // System.out.println(Arrays.toString(heights));

            stack.clear();
            for (int j = cols - 1; j >= 0; j--) {
                while (stack.size() > 0 && heights[stack.peek()] >= heights[j]) {
                    stack.pop();
                }
                right[j] = stack.size() > 0 ? stack.peek() : cols;
                stack.push(j);
            }

            stack.clear();
            for (int j = 0; j < cols; j++) {
                while (stack.size() > 0 && heights[stack.peek()] >= heights[j]) {
                    stack.pop();
                }
                left[j] = stack.size() > 0 ? stack.peek() : -1;
                stack.push(j);
            }

            // calcEdge(heights, right, stack, IntStream.rangeClosed(cols-1, 0), cols);
            // calcEdge(heights, left, stack, IntStream.range(0, cols), -1);

            for (int j = 0; j < cols; j++) {
                int curArea = (right[j] - left[j] - 1) * heights[j];
                maxArea = Math.max(maxArea, curArea);
            }
        }

        return maxArea;
    }

    /**
     * The python-like coding style is not very easy in Java，To generate a stream like range(cols-1, -1, -1) in python,
     * we need use apache commons lang package.
     * @param heights
     * @param dst
     * @param stack
     * @param intStream
     * @param border
     */
    private void calcEdge(int[] heights, int[] dst, Stack<Integer> stack, IntStream intStream, int border) {
        stack.clear();
        intStream.forEach(j -> {
            while(stack.size() > 0 && heights[stack.size()] >= heights[j]) {
                stack.pop();
            }
            dst[j] = stack.size() > 0 ? stack.peek() : border;
            stack.push(j);
        });
    }

    static public void main(String args[]) {
        char[][] matrix = {
            {'1', '0', '1', '0', '0'},
            {'1', '0', '1', '1', '1'},
            {'1', '1', '1', '1', '1'},
            {'1', '0', '0', '1', '0'},
        };
        // char[][] matrix = {{'1'}};

        MaxRectangle85 solution = new MaxRectangle85();
        System.out.println(solution.maximalRectangle(matrix));
    }
}
