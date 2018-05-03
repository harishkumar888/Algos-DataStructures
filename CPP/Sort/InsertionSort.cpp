#include <iostream>
#include <vector>

using namespace std;

void insertionSort(){
  vector<int> vec = {6,5,8,2,7,9,1};
	for(int i=1; i<=vec.size(); ++i){
	  for(auto elem:vec){
	    cout << elem << " ";
	  }
	  cout << endl;
	  
	  for(int j=0; j != i && j<=vec.size(); ++j){
	    int key = 0;
	    if(vec[i]<vec[j]){
	      key = vec[j];
	      vec[j] = vec[i];
	      vec[i] = key;
	    }
	  }
  }
}

int main() {
  insertionSort();
  return 0;
}
