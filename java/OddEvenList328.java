public class OddEvenList328 {
    static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) {this.val = val;}
        ListNode(int val, ListNode next) {this.val = val; this.next = next;}
    }

    public ListNode oddEvenList(ListNode head) {
        if (head == null) {
            return null;
        }
        int count = 0;
        ListNode cur = head;
        ListNode oddTail = head;
        ListNode evenHead = head.next;
        do {
            count += 1;
            ListNode next = cur.next;
            cur.next = next == null ? null : next.next;
            if ((count & 1) == 1) {
                oddTail = cur;
            }
            cur = next;
        } while (cur != null);

        oddTail.next = evenHead;
        return head;
    }

    static public void main(String[] args) {
        ListNode six = new ListNode(6);
        ListNode five = new ListNode(5, six);
        ListNode four = new ListNode(4, five);
        ListNode three = new ListNode(3, four);
        ListNode two = new ListNode(2, three);
        ListNode one = new ListNode(1, two);
        OddEvenList328 solution = new OddEvenList328();
        ListNode h = solution.oddEvenList(one);
        while (h != null) {
            System.out.println(h.val);
            h = h.next;
        }
    }
}
