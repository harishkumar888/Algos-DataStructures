#include <iostream>
#include <vector>

void insertionSortNaive(std::vector<int>& vec){
	for(int i=1; i<=vec.size(); ++i){  
	  for(int j=0; j != i && j<=vec.size(); ++j){
	    if(vec[i]<vec[j]){
	      int key = vec[j];
	      vec[j] = vec[i];
	      vec[i] = key;
	    }
	  }
  }
}

void insertionSortOptimized(std::vector<int>& vec){
	for(int i=0; i<vec.size(); ++i){
	  for(int j=vec.size()-1; j >= 0; j--){
	    if(vec[i]>vec[j]){
	      int key = vec[j];
	      vec[j] = vec[i];
	      vec[i] = key;
	    }
	  }
  }
}

int main() {
  std::vector<int> inp_vec = {6,5,8,2,7,9,1};

	std::cout << "Vector before sorting: " << std::endl;
	for(auto elem:inp_vec){
	  std::cout << elem << " ";
	}
	std::cout << std::endl;

  // insertionSortNaive(inp_vec);
  insertionSortOptimized(inp_vec);

	std::cout << "Vector after sorting: " << std::endl;
	for(auto elem:inp_vec){
	  std::cout << elem << " ";
	}
	std::cout << std::endl;

  return 0;
}
