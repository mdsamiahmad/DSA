/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        if (head == null)
            return null;
        int length = 0;
        ListNode temp = head;
        while (temp != null) {
            length++;
            temp = temp.next;
        }
        int cnt = 0;
        while (head != null) {
            if (cnt < (length / 2) ) {
                cnt++;
                head = head.next;
            } else {
                break;
            }
        }

        return head;
        // By TortioseHare Method
        /*
        class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow=head;
        ListNode fast=head;
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        return slow;
    }
}
        */
    }
}
