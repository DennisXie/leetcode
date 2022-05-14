import java.util.LinkedList;

public class RemoveKdigits402 {
    public String removeKdigits(String num, int k) {
        int ansLen = num.length() - k;
        int count = 0;

        LinkedList<Character> characters = new LinkedList<>();
        for (int i = 0; i < num.length(); i++) {
            while (characters.size() > 0 && num.charAt(i) < characters.getLast() && count < k) {
                characters.removeLast();
                count += 1;
            }

            if (characters.size() < ansLen) {
                characters.add(num.charAt(i));
            } else {
                count += 1;
            }
        }

        while (characters.size() > 0 && characters.getFirst() == '0') {
            characters.removeFirst();
        }

        StringBuilder stringBuilder = new StringBuilder();
        for (Character ch : characters) {
            stringBuilder.append(ch);
        }

        return characters.size() == 0 ? "0" : stringBuilder.toString();
    }

    static public void main(String[] args) {
        String num = "99991";
        RemoveKdigits402 solution = new RemoveKdigits402();
        System.out.println(solution.removeKdigits(num, 3));
    }
}
