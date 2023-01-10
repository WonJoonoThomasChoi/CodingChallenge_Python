# https://leetcode.com/problems/palindrome-linked-list/
'''
1. 아이디어 :
    1) 배열을 하나 만들고, 노드를 순회하며 값을 넣은 후, 배열을 뒤집어서 비교한다.
2. 시간복잡도 :
    1) O(n)
    - while 문
3. 자료구조 :
    1) 배열
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        alist=[]
        curr=head
        while curr:
            alist.append(curr.val)
            curr=curr.next

        return alist==alist[::-1]