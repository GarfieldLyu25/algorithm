
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}


class Solution {
    public Node copyRandomList(Node head) {
        if(head == null){
            return null;
        }
        for(Node node = head;node != null;node = node.next.next){
            Node newnode = new Node(node.val);
            newnode.next = node.next;
            node.next = newnode;
        }
        for(Node node = head;node != null;node = node.next.next){
            Node newnode = node.next;
            if(node.random != null){
                newnode.random = node.random.next;
            }
        }
        Node newhead = head.next;
        for(Node node = head;node != null;node = node.next){
            Node newnode = node.next;
            node.next = node.next.next;
            newnode.next = (newnode.next != null) ? newnode.next.next : null;
        }
        return newhead;
    }
}