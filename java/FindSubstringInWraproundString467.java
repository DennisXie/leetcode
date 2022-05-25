import java.util.*;

public class FindSubstringInWraproundString467 {
    Set<Integer> subSet = new HashSet<Integer>();

    public int findSubstringInWraproundString2(String p) {
        // dp[c] 以c为结尾的最长子串
        int[] dp = new int[26];
        int k = 0;
        for (int i = 0; i < p.length(); ++i) {
            if (i > 0 && (p.charAt(i) - p.charAt(i - 1) + 26) % 26 == 1) {
                ++k;
            } else {
                k = 1;
            }
            dp[p.charAt(i) - 'a'] = Math.max(dp[p.charAt(i) - 'a'], k);
        }
        return Arrays.stream(dp).sum();
    }

    public int findSubstringInWraproundString(String p) {
        subSet.clear();
        int cur = 0;
        int start = 0;
        while (cur < p.length()) {
            if (cur + 1 == p.length()) {
                addToSubset(p.charAt(start) - 'a', cur - start + 1);
                break;
            }
            int curIdx = p.charAt(cur) - 'a';
            int nextIdx = p.charAt(cur + 1) - 'a';
            if (nextIdx - curIdx == 1 || nextIdx - curIdx == -25) {
                cur += 1;
            } else {
                addToSubset(p.charAt(start) - 'a', cur - start + 1);
                cur += 1;
                start = cur;
            }
        }
        return subSet.size();
    }

    private void addToSubset(int begin, int length) {
        for (int i = 1; i <= length; i++) {
            for (int j = begin; j < begin + 26; j++) {
                if (j + i <= begin + length) {
                    int start = j % 26;
                    subSet.add(i * 100 + start);
                } else {
                    break;
                }
            }
        }
    }

    static public void main(String[] args) {
        String p = "cdefghefghijklmnopqrstuvwxmnijklmnopqrstuvbcdefghijklmnopqrstuvwabcddefghijklfghijklmabcdefghijklmnopqrstuvwxymnopqrstuvwxyz";
        // String p = "abcd";
        FindSubstringInWraproundString467 solution = new FindSubstringInWraproundString467();
        System.out.println(solution.findSubstringInWraproundString(p));
    }
}
