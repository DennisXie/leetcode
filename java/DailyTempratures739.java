import java.util.Stack;

public class DailyTempratures739 {
    public int[] dailyTempratures(int[] temperatures) {
        int[] next = new int[temperatures.length];
        Stack<Integer> highest = new Stack<>();
        for (int i = temperatures.length - 1; i >= 0; i--) {
            int currentTemperature = temperatures[i];
            // If current temprature is higher than the top tempature, then pop the top, because
            // the top of stack won't be seen for ever.
            while (highest.size() != 0 && temperatures[highest.peek()] <= currentTemperature) {
                highest.pop();
            }
            if (highest.size() != 0) {
                next[i] = highest.peek() - i;
            } else {
                next[i] = 0;
            }
            highest.push(i);
        }
        return next;
    }

    public static void main(String[] args) {

        DailyTempratures739 solution = new DailyTempratures739();
        int[] temperatures = {73, 74, 75, 71, 69, 72, 76, 73};
        for (int index: solution.dailyTempratures(temperatures)) {
            System.out.println(index);
        }
    }
}
