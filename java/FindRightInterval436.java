import java.util.Arrays;
import java.util.Comparator;

public class FindRightInterval436 {
    private static class Pair {
        public int start;
        public int index;

        public Pair(int start, int index) {
            this.start = start;
            this.index = index;
        }

    }
    public int[] findRightInterval(int[][] intervals) {
        Pair[] starts = new Pair[intervals.length];
        for (int i = 0; i < intervals.length; i++) {
            starts[i] = new Pair(intervals[i][0], i);
        }
        Arrays.sort(starts, Comparator.comparingInt(o -> o.start));

        int[] ans = new int[intervals.length];
        for (int k = 0; k < intervals.length; k++) {
            int i = 0;
            int j = intervals.length - 1;
            ans[k] = -1;
            while (i <= j) {
                int mid = (i + j) >> 1;
                if (starts[mid].start >= intervals[k][1]) {
                    ans[k] = starts[mid].index;
                    j = mid - 1;
                } else {
                    i = mid + 1;
                }
            }
        }
        return ans;
    }

    static public void main(String[] args) {
        int[][] intervals = {{1, 4}, {2, 3}, {1, 2}};
        FindRightInterval436 solution = new FindRightInterval436();
        System.out.println(Arrays.toString(solution.findRightInterval(intervals)));
    }
}
