import java.util.Arrays;
import java.util.Comparator;

public class MinArrowShots452 {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, Comparator.comparingInt(a -> a[1]));
        int count = 1;
        int end = points[0][1];
        for (int[] point: points) {
            if (point[0] > end) {
                count += 1;
                end = point[1];
            }
        }
        return count;
    }

    static public void main(String[] args) {
        MinArrowShots452 solution = new MinArrowShots452();
        int[][] points = {{-2147483646,-2147483645},{2147483646,2147483647}};
        System.out.println(solution.findMinArrowShots(points));
    }
}
