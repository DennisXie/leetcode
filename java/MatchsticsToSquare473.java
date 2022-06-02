import java.util.Arrays;

public class MatchsticsToSquare473 {

    public boolean makesquare2(int[] matchsticks) {
        int[] f = new int[1 << matchsticks.length];
        int edge = 0;
        for (int len : matchsticks) {
            edge += len;
        }

        if (edge % 4 != 0) {
            return false;
        } else {
            edge = edge / 4;
        }

        for (int i = 0; i < matchsticks.length; i++) {
            f[1 << i] = matchsticks[i];
        }

        for (int i = 1; i < matchsticks.length; i++) {
            for (int j = 1; j < f.length; j++) {
                for (int k = 1; k < matchsticks.length; k++) {

                }
            }
        }
    }

    public boolean makesquare(int[] matchsticks) {
        int[][] f = new int[4][1 << matchsticks.length];
        Arrays.sort(matchsticks);
        int edge = 0;
        for (int len : matchsticks) {
            edge += len;
        }

        if (edge % 4 != 0) {
            return false;
        } else {
            edge = edge / 4;
        }

        int all = 0;
        for (int i = 0; i < matchsticks.length; i++) {
            f[0][1 << i] = matchsticks[i];
            all = all + (1 << i);
        }

        int ret = findSolution(3, all, 4 * edge, edge, f, matchsticks);
        return ret > 0;
    }

    private int findSolution(int i, int j, int length, int edge, int[][] f, int[] sticks) {
        if (f[i][j] > 0) {
            return f[i][j];
        }

        f[i][j] = 0;
        for (int k = 0; k < sticks.length; k++) {
            int idx = 1 << k;
            if ((j & idx) != 0) {
                int left = length - sticks[k];
                if (left == i * edge) {
                    int ret = findSolution(i-1, j - idx, left, edge, f, sticks);
                    if (ret > 0) {
                        f[i][j] = length;
                        break;
                    }
                } else if (left > i * edge) {
                    int ret = findSolution(i, j - idx, left, edge, f, sticks);
                    if (ret > 0) {
                        f[i][j] = length;
                        break;
                    }
                }
            }
        }
        return f[i][j];
    }

    public static void main(String[] args) {
        int[] sticks = {8, 8, 1, 2, 3, 1, 2, 7};
        MatchsticsToSquare473 solution = new MatchsticsToSquare473();
        System.out.println(solution.makesquare(sticks));
    }
}
