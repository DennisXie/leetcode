import java.util.Arrays;

class RussianMaxEnvelopes354 {
    public int maxEnvelopes(int[][] envelopes) {
        Arrays.sort(
            envelopes,
            (a, b) -> {
                if (a[0] != b[0]) {
                    return a[0] - b[0];
                } else {
                    return b[1] - a[1];
                }
            });

        // longest increase sub array
        int[] top = new int[envelopes.length];
        int piles = 0;
        for (int i = 0; i < envelopes.length; i++) {
            int left = 0, right = piles;
            while (left < right) {
                int mid = (left + right) / 2;
                if (top[mid] < envelopes[i][1]) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            if (left == piles) {
                piles++;
            }
            top[left] = envelopes[i][1];
        }
        return piles;
    }

    static public void main(String[] args) {
        RussianMaxEnvelopes354 solution = new RussianMaxEnvelopes354();
        // int[][] envelopes = {{2, 1}, {4, 1}, {6, 2}, {7, 5}};
        // int[][] envelopes = {{2, 4}, {5, 4}, {6, 4}, {6, 7}};
        // int[][] envelopes = {{4, 4}, {4, 5}, {4, 6}, {6, 7}};
        int[][] envelopes = {{5, 4}, {6, 4}, {6, 7}, {2, 3}};
        System.out.println(solution.maxEnvelopes(envelopes));
    }
}