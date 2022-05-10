public class DeleteDuplicates82 {
    static public class ListNode {
        int val;
        ListNode next;
        ListNode(int val) {this.val = val;}
        ListNode(int val, ListNode next) {this.val = val; this.next = next;}
    }

    public ListNode deleteDuplicates(ListNode head) {
        ListNode cur = head;
        ListNode pre = null;
        while (cur != null) {
            boolean deleteCur = false;
            while (cur.next != null && cur.next.val == cur.val) {
                cur.next = cur.next.next;
                deleteCur = true;
            }
            if (deleteCur) {
                if (pre != null) {
                    pre.next = cur.next;
                } else {
                    head = cur.next;
                }
            } else {
                pre = cur;
            }
            cur = cur.next;
        }

        return head;
    }

    static public void main(String[] args) {
        int[] values = {1, 1, 1, 2, 3, 3, 4, 4, 5};
        ListNode cur = null;
        for (int i = values.length - 1; i >= 0; i--) {
            cur = new ListNode(values[i], cur);
        }

        DeleteDuplicates82 solution = new DeleteDuplicates82();
        cur = solution.deleteDuplicates(cur);
        while (cur != null) {
            System.out.println(cur.val);
            cur = cur.next;
        }
    }
}
