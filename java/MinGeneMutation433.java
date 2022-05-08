public class MinGeneMutation433 {

    public int minMutation(String start, String end, String[] bank) {
        int[][] distance = new int[bank.length + 1][bank.length + 1];
        int end_idx = -1;
        for (int i = 0; i < bank.length; i++) {
            distance[0][i+1] = unimpeded(start, bank[i]);
            distance[i+1][0] = distance[0][i+1];
            if (end.equals(bank[i])) {
                end_idx = i+1;
            }
        }
        for (int i = 0; i < bank.length; i++) {
            for (int j = 0; j < bank.length; j++) {
                distance[i+1][j+1] = unimpeded(bank[i], bank[j]);
                distance[j+1][i+1] = distance[i+1][j+1];
            }
        }

        for (int k = 0; k < distance.length; k++) {
            for (int i = 0; i < distance.length; i++) {
                for (int j = 0; j < distance.length; j++) {
                    if (distance[i][k] != -1 && distance[k][j] != -1) {
                        if (distance[i][j] == -1) {
                            distance[i][j] = distance[i][k] + distance[k][j];
                        } else {
                            distance[i][j] = Math.min(distance[i][j], distance[i][k] + distance[k][j]);
                        }
                    }
                }
            }
        }
        return end_idx >= 0 ? distance[0][end_idx] : -1;
    }

    private int unimpeded(String start, String end) {
        int count = 0;
        for (int i = 0; i < start.length(); i++) {
            if (start.charAt(i) != end.charAt(i)) {
                count += 1;
            }
        }
        return count > 1 ? -1 : count;
    }

    static public void main(String[] args) {
        String start = "AACCGGTT";
        String end = "AACCGGTA";
        String[] bank = {};
        MinGeneMutation433 solution = new MinGeneMutation433();
        System.out.println(solution.minMutation(start, end, bank));
        
    }
}
