import java.util.Comparator;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.SynchronousQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.ReentrantLock;

public class FooBar {

    static class Pair<T, B> {
        private T left;
        private B right;
        public Pair(T left, B right) {
            this.left = left;
            this.right = right;
        }

        public T getLeft() {
            return this.left;
        }

        public B getRight() {
            return this.right;
        }
    }

    synchronized public void tryEverything() {
        ReentrantLock lock = new ReentrantLock();
        AtomicInteger atomicInteger = new AtomicInteger();
        new HashSet<Integer>();
        PriorityQueue<Pair<Integer, Integer>> queue = new PriorityQueue<>(Comparator.comparingInt(Pair::getLeft));
        synchronized (lock) {
            tryEverything();
        }
    }

    synchronized public static void tryStatic() {
        synchronized (FooBar.class) {
            FooBar.tryStatic();
        }
    }
}
