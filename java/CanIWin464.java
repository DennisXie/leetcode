import java.util.HashMap;
import java.util.Map;

public class CanIWin464 {
    private int maxChoosable = 0;

    private int desiredTotal = 0;

    private Map<Integer, Boolean> memo;

    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        if ((1 + maxChoosableInteger) * (maxChoosableInteger) / 2 < desiredTotal) {
            return false;
        }
        this.maxChoosable = maxChoosableInteger;
        this.desiredTotal = desiredTotal;
        boolean win = true;
        memo = new HashMap<>();
        win = calcWin(0, 0);
        return win;
    }

    private boolean calcWin(int choosed, int current) {
        if (memo.get(choosed) != null) {
            return memo.get(choosed);
        }

        memo.put(choosed, false);
        for (int i = 1; i <= maxChoosable; i++) {
            int candidate = 1 << (i - 1);
            if ((choosed & candidate) == 0) {
                if (i + current >= desiredTotal) {
                    memo.put(choosed, true);
                    break;
                }
                // 这就表示两人最好的发挥，要找出另一个人不能赢的状态
                if (!calcWin(choosed | candidate, current + i)) {
                    memo.put(choosed, true);
                    break;
                }
            }
        }
        return memo.get(choosed);
    }

    static public void main(String[] args) {
        CanIWin464 solution = new CanIWin464();
        System.out.println(solution.canIWin(4, 8));
        System.out.println(solution.canIWin(3, 5));
        System.out.println(solution.canIWin(2, 3));
    }
}
