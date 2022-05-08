import java.util.Arrays;

public class ArrangePostBox1478 {
    public int minDistance(int[] houses, int k) {
        int[][] minDistance = new int[k+1][houses.length+1];
        int[][] distance = new int[houses.length+1][houses.length+1];
        int maxValue = 0;
        Arrays.sort(houses);

        // We place the postbox at the middle of the house, then we can get the min distance.
        for (int i = 0; i < houses.length; i++) {
            for (int j =  i; j < houses.length; j++) {
                int mid = (i + j) / 2;
                distance[i+1][j+1] = 0;
                for (int h = i; h <= j; h++) {
                    distance[i+1][j+1] += Math.abs(houses[h]-houses[mid]);
                }
                maxValue = Math.max(maxValue, distance[i+1][j+1]);
            }
        }

        // If we use Integer.MAX_VALUE, the minDistance will overflow.
        minDistance[0][0] = 0;
        for (int j = 1; j <= houses.length; j++) {
            minDistance[0][j] = maxValue;
        }

        // We can use 1d or rolling array to use less memory usage.
        for (int i = 1; i <= k; i++) {
            for (int j = i-1; j <= houses.length; j++) {
                minDistance[i][j] = maxValue;
                for (int h = i-1; h < j; h++) {
                    minDistance[i][j] = Math.min(minDistance[i][j], minDistance[i-1][h] + distance[h+1][j]);
                }
            }
        }
        return minDistance[k][houses.length];
    }

    static public void main(String[] args) {
        int[] houses = {1, 4, 8, 20, 10};
        ArrangePostBox1478 solution = new ArrangePostBox1478();
        System.out.println(solution.minDistance(houses, 3));
    }
}
