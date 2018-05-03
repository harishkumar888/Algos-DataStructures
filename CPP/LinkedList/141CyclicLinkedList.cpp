/* 141.Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
*/

#include <unordered_set>

class ListNode{
public:
  int val;
  ListNode *next;
  ListNode(int x): val(x), next(NULL) {}
};


// Using an unordered_set

bool hasCycleUsingSet(ListNode *head){
  std::unordered_set<ListNode *> ll_set;
  while(head != NULL){
    if(ll_set.find(head) != ll_set.end())
      ll_set.insert(head);
    head = head->next;
  }
  return false;
}

// Fast and slow pointer

bool hasCycleUsingPointer(ListNode *head){
  findcycle = false;
  if(head == NULL)
    return findcycle;
  ListNode *slow_p = head;
  ListNode *fast_p = head;
  while(slow_p && fast_p && fast_p->next){
    slow_p = slow_p->next;
    fast_p = fast_p->next->next;
    if(slow_p == fast_p){
      findcycle = true;
    }
  }
  return findcycle;
}

int main(){
  ListNode head(1);
  head.next = new ListNode(2);
  head.next->next = new ListNode(3);
  head.next->next->next = new ListNode(4);
  head.next->next->next->next = new ListNode(5);
  
  return 0;  
}

