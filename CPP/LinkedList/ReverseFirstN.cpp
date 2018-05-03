#include <iostream>

using namespace std;
/*Reverse the first N nodes of a linked list.*/
  
class Node{
  public:
  int data;
  Node* next = nullptr;
  Node(int init_data){
    data = init_data;
  }
};

class SinglyLinkedList{
  public:
  Node* head;
  SinglyLinkedList(Node* init_node){
    head = init_node;
  }
  
  friend ostream& operator<<(ostream& os, const SinglyLinkedList& ll){
    Node *head = ll.head;
    while(head){
      os << head->data << " ";
      head = head->next;
    }
    return os;
  }
  
  void printList(){
    Node* temp = head;
    while(temp != nullptr){
      std::cout<<temp->data<<" ";
      temp = temp->next;
    }
    std::cout<<"\n";
  }

  void ReverseFirstK(int K){
    Node* prev = nullptr;
    Node* next = nullptr;
    Node* old = nullptr; // Pointer to the remainder of the unmodified LL.
    Node* cur = head;
    int count = 0;
    while(cur != nullptr && count<K){
        next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
        count++;
    }
    head = prev;

    // Store the rest of the unmodified linked list.
    old = cur;
    cur = head;
    // Find the end of the reversed LL.
    while(cur->next != nullptr){
      cur = cur->next;
    }
    //Point the next of the end node to the remainder of the unmodified LL.
    cur->next = old;
  }
};

int main() {
  int K = 3;
  Node* head_node = new Node(10);
  head_node->next = new Node(5);
  head_node->next->next = new Node(2);
  head_node->next->next->next = new Node(50);
  head_node->next->next->next->next = new Node(2);
  head_node->next->next->next->next->next = new Node(8);
  SinglyLinkedList ll(head_node);
  std::cout << "Original List:\n";
  ll.printList();
  ll.ReverseFirstK(K);
  std::cout << "After reversing the first K nodes:\n";
  ll.printList();
  // cout << ll;
}
