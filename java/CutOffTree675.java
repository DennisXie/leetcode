import java.util.*;

public class CutOffTree675 {

    private static class Point {
        public int height;
        public int x;
        public int y;

        public Point(int height, int x, int y) {
            this.height = height;
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            Point point = (Point) o;

            if (height != point.height) return false;
            if (x != point.x) return false;
            return y == point.y;
        }

        @Override
        public int hashCode() {
            int result = height;
            result = 31 * result + x;
            result = 31 * result + y;
            return result;
        }
    }

    private List<List<Integer>> forest;

    private Deque<Point> queue = new LinkedList<>();

    private Map<Point, Integer> visited = new HashMap<>();

    private Set<Point> inQueue = new HashSet<>();

    private int[][] direction = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

    public int cutOffTree(List<List<Integer>> forest) {
        this.forest = forest;
        List<Point> trees = new ArrayList<>();
        for (int i = 0; i < forest.size(); i++) {
            for (int j = 0; j < forest.get(0).size(); j++) {
                if (forest.get(i).get(j) > 1) {
                    trees.add(new Point(forest.get(i).get(j), i, j));
                }
            }
        }
        trees.sort(Comparator.comparingInt(p -> p.height));
        Point pre = new Point(forest.get(0).get(0), 0, 0);
        int total = 0;
        for (Point cur : trees) {
            if (!cur.equals(pre)) {
                int dis = findShortestWay(pre, cur);
                if (dis < 0) {
                    return -1;
                } else {
                    total += dis;
                }
                pre = cur;
            }
        }
        return total;
    }

    /**
     * SPFA find the shortest way;
     * @param start
     * @param end
     * @return
     */
    private int findShortestWay(Point start, Point end) {
        queue.clear();
        visited.clear();
        inQueue.clear();

        queue.add(start);
        inQueue.add(start);
        visited.put(start, 0);
        while (!queue.isEmpty()) {
            Point cur = queue.pollFirst();
            for (int[] dir : direction) {
                int nX = cur.x + dir[0];
                int nY = cur.y + dir[1];
                if (nX < 0 || nX >= forest.size() || nY < 0 || nY >= forest.get(0).size()) {
                    continue;
                }
                int height = forest.get(nX).get(nY);
                if (height != 0) {
                    shorterAndSet(cur, new Point(height, cur.x+dir[0], cur.y+dir[1]));
                }
            }
        }
        return visited.getOrDefault(end, -1);
    }

    private void shorterAndSet(Point cur, Point next) {
        if (!visited.containsKey(next) || visited.get(next) > visited.get(cur) + 1) {
            visited.put(next, visited.get(cur) + 1);
            if (!inQueue.contains(next)) {
                inQueue.add(next);
                queue.addLast(next);
            }
        }
    }

    static public void main(String[] args) {
        List<List<Integer>> forest = Arrays.asList(
                Arrays.asList(1, 2, 3),
                Arrays.asList(0, 0, 0),
                Arrays.asList(7, 6, 5)
        );

        CutOffTree675 solution = new CutOffTree675();
        System.out.println(solution.cutOffTree(forest));
    }
}
