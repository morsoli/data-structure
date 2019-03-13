# include<iostream>
using namespace std;

template <class T>
int length(T& arr){
    return sizeof(arr)/sizeof(arr[0]);
}
//O(n^3)
int MaxSunseqSum1(int n[]){
    int MaxSum=0,ThisSum=0;
    for(int i=0;i<length(n);i++){
        for(int j=i;j<length(n);j++){
            for(int k=i;k<=j;k++){
                ThisSum+=n[k];
            }
            if(MaxSum<ThisSum){
                MaxSum=ThisSum;
            }
        }
    }
    return MaxSum;
}
int main(){
    int n[]={-2, 11, -4, 13, -5, -2};
    cout<<MaxSunseqSum1(n);
}
