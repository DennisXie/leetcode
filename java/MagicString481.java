public class MagicString481 {

    public int magicalString(int n) {
        if (n <= 3) {
            return 1;
        }
        byte[] chs = new byte[n];
        chs[0] = 1;
        chs[1] = 2;
        chs[2] = 2;
        int i = 2;
        int j = 3;
        int count = 1;
        while (j < n) {
            byte cur = (byte) (((i+1) & 1) == 1 ? 1: 2);
            chs[j] =  cur;
            j += 1;
            count = cur == 1 ? count + 1 : count;
            if (j == n) {
                break;
            }

            if (chs[i] == 2) {
                chs[j] = cur;
                j += 1;
                count = cur == 1 ? count + 1 : count;
            }
            i += 1;
        }
        return count;
    }

    static public void main(String[] args) {
        MagicString481 solution = new MagicString481();
        System.out.println(solution.magicalString(4));
    }
}
