import java.util.*;

public class FallingSquares699 {
    private Map<Integer, Integer> heights = new HashMap<>();

    public List<Integer> fallingSquares(int[][] positions) {
        heights.clear();
        List<Integer> ans = new LinkedList<>();

        int maxHeight = 0;
        for (int squareIdx = 0; squareIdx < positions.length; squareIdx++) {
            int[] square = positions[squareIdx];
            int height = square[1];
            int pos = square[0];
            for (int idx : heights.keySet()) {
                if (across(pos, pos+square[1]-1, positions[idx][0], positions[idx][0] + positions[idx][1] - 1)) {
                    int baseHeight = heights.get(idx);
                    height = Math.max(height, baseHeight + square[1]);
                }
            }
            heights.put(squareIdx, height);
            maxHeight = Math.max(maxHeight, height);
            ans.add(maxHeight);
        }

        return ans;
    }

    private boolean across(int aLeft, int aRight, int bLeft, int bRight) {
        if (bLeft <= aRight && bLeft >= aLeft) {
            return true;
        }

        if (aLeft <= bRight && aLeft >= bLeft) {
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        int[][] positions = {
            {5, 2},
            {6, 3},
            {11, 1},
            {2, 4}
        };

        FallingSquares699 solution = new FallingSquares699();
        System.out.println(solution.fallingSquares(positions));
    }
}
