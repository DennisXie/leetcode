import java.util.HashMap;

public class MaxWordProduct318 {
    public int maxProduct(String[] words) {

        HashMap<Character, Integer> charMap = new HashMap<>();
        String basics = "abcdefghijklmnopqrstuvwxyz";
        int count = 1;
        for (int i = 0; i < 26; i++) {
            charMap.put(basics.charAt(i), count);
            count = count << 1;
        }

        HashMap<Integer, Integer> wordEncodeDict = new HashMap<>();
        for (int j = 0; j < words.length; j++) {
            String word = words[j];
            int encoded = 0;
            for (int i = 0; i < word.length(); i++) {
                encoded = encoded | charMap.get(word.charAt(i));
            }
            wordEncodeDict.put(j, encoded);
        }

        int maxProduct = 0;
        for (int i = 0; i < words.length; i++) {
            for (int j = i+1; j < words.length; j++) {
                if ((wordEncodeDict.get(i) & wordEncodeDict.get(j)) == 0) {
                    maxProduct = Math.max(maxProduct, words[i].length() * words[j].length());
                }
            }
        }
        return maxProduct;
    }
}
