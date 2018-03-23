# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret,p1,p2 = ListNode(0),l1,l2
        cur = ret
        num1,num2=0,0
        i,j=1,1
        while(p1!=None):
            num1+=p1.val*i
            i*=10
            p1=p1.next
        while(p2!=None):
            num2+=p2.val*j
            j*=10
            p2=p2.next
        num = num1+num2
        num3=1
        if num==0:
            cur.next=ListNode(num)
        else:
            while(num):
                num3=num%10
                num=num//10
                #cur.val=num3  如果给当前的结点赋予值，尾结点需要去掉，因为循环构造结点时多执行了一步。循环外加一步cur.next=None
                cur.next = ListNode(num3)
                print(num,cur.val,cur.next.val)
                cur=cur.next
        return ret.next
