#include <iostream>
#include <vector>

using namespace std;

int numFriendRequestsNaive(vector<int>& ages) {
  int tot_requests=0;
  for(int i=0;i<ages.size();++i){
    for(int j=0;j<ages.size();++j){
      if(i!=j){
        if(ages[i]<ages[j] || (ages[j]>100 && ages[i]<100) || (ages[j] <= 0.5*ages[i]+7)){
          continue;
        }
        else{
          tot_requests++;
        }
      }
    }
  }
  return tot_requests;
}




int main() {
  vector<int> ages = {20,30,100,110,120};
  
  cout << numFriendRequestsNaive(ages);
}