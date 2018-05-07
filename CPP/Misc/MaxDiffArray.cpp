/*
Maximum difference between two elements such that larger element appears after the smaller number.
Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element appears after the smaller number.

Examples :

Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8
Explanation : The maximum difference is between 10 and 2.

Input : arr = {7, 9, 5, 6, 3, 2}
Output : 2
Explanation : The maximum difference is between 9 and 7.
*/


#include <iostream>

int maxDifference(int arr[], int arr_size){
  int max_diff = arr[1] - arr[0];
  int min_element = arr[0];

  for(int i=0; i<arr_size; ++i){
    if(arr[i]-min_element > max_diff){
      max_diff = arr[i]-min_element;
    }
    if(arr[i]<min_element){
      min_element = arr[i];
    }
  }
  return max_diff;
}



int main(){
  int a[] = {7, 9, 5, 6, 3, 2, 2, 2, 1};
  std::cout<<"The max difference between any of elements of the array is:";
  std::cout<<maxDifference(a, sizeof(a)/sizeof(int))<<"\n";
  return 0;
}
