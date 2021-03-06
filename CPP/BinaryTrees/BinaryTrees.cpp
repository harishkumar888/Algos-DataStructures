// BinaryTrees.cpp : Defines the entry point for the console application.
//

#include<iostream>
using namespace std;

struct Node {
	int data;
	struct Node* left;
	struct Node* right;
};

class tree {
private:
	Node* root;
public:
	void print_data() {
		std::cout << root->data<< endl;
	}
	Node get_sample_tree() {
		Node my_node;
		my_node.data = 10;
		my_node.left = new Node();
		my_node.right = new Node();
		my_node.left->left = new Node();
		my_node.left->right = new Node();
		my_node.right->left = new Node();
		my_node.right->right = new Node();
		my_node.left->data = 5;
		my_node.left->left->data = 2;
		my_node.left->right->data = 7;
		my_node.right->data = 15;
		my_node.right->left->data = 12;
		my_node.right->right->data = 19;
		return my_node;
	}
	void traverse_preorder() {
		if  (root == NULL)
			return;
		cout<<root->data;
		traverse_preorder();
		traverse_preorder();
	}
};

int main()
{
	std::cout << "My Binary tree\n";
	//Node my_node;
	//my_node.data = 10;
	//my_node.left = new Node();
	//my_node.right = new Node();
	//my_node.left->left = new Node();
	//my_node.left->right = new Node();
	//my_node.right->left = new Node();
	//my_node.right->right = new Node();
	//my_node.left->data = 5;
	//my_node.left->left->data = 2;
	//my_node.left->right->data = 7;
	//my_node.right->data = 15;
	//my_node.right->left->data = 12;
	//my_node.right->right->data = 19;

	tree my_tree = tree();
	my_tree.print_data();
	Node sample_tree = my_tree.get_sample_tree();
    return 0;
}

