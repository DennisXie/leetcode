public class FlattenBTtoList114 {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public void flatten(TreeNode root) {
        if (root != null) {
            traverse(root);
        }
    }

    private TreeNode traverse(TreeNode node) {
        TreeNode tail = node;

        if (node.left != null) {
            tail = traverse(node.left);
            tail.right = node.right;
            node.right = node.left;
            node.left = null;
        }

        if (tail.right != null) {
            tail = traverse(tail.right);
        }

        return tail;
    }

    static public void main(String[] args) {
        TreeNode two = new TreeNode(2);
        TreeNode root = new TreeNode(1, two, null);
        FlattenBTtoList114 solution = new FlattenBTtoList114();
        solution.flatten(root);
    }
}
