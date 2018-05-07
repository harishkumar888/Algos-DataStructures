#include <iostream>

/*Given a ‘key’, delete the first occurrence of this key in linked list.*/
  
class Node{
  public:
  int data;
  Node* next = NULL;
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
  void printList(){
    Node* temp = head;
    while(temp != NULL){
      std::cout<<temp->data<<" ";
      temp = temp->next;
    }
    std::cout<<"\n";
  }

  void DeleteFirstOccurance(int thisValue){
    if(head->data == thisValue){
      head = head->next;
      return;
    }
    Node* temp = head->next;
    Node* prev = temp;
    while(temp != NULL){
      if(temp->data == thisValue){
        prev->next = temp->next;
        return;
      }
      temp = temp->next;
    }
  }
};

int main() {
  Node* head_node = new Node(10);
  head_node->next = new Node(5);
  head_node->next->next = new Node(2);
  head_node->next->next->next = new Node(50);
  head_node->next->next->next->next = new Node(2);
  head_node->next->next->next->next->next = new Node(8);
  SinglyLinkedList ll(head_node);
  std::cout << "Original List:\n";
  ll.printList();
  ll.DeleteFirstOccurance(2);
  std::cout << "After removing the first occurance of 2:\n";
  ll.printList();
}
