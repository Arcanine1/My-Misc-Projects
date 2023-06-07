#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

//returns number of appearences of target in int arr[] with size size
int count(bool arr[] ,int size, int target ){

    int count =0;

    //iterates through
    for (int i = 0; i < size; i++) {
        if(arr[i]== target){
            count++;
        }
    }   

    return count;

}

int main() {


    int size =  pow(10,9);
    bool* numbers = (bool*) malloc(size * sizeof(bool)); //defines array

    for (int i = 2; i < size; i++) {
    numbers[i] = true;
    }   

    numbers[0]= false;
    numbers[1]=false;

    int factor=1;  //current factor
    int root = sqrt(size);
    int num=3; //num evaluating currently
    int multiple =factor; //used to optimize the sieve
    float top = size/factor; //used to optimize the sieve

    while(factor<root){

        //finds new factor
        factor=factor+1;
        while(1){
            if(numbers[factor]==true){
                break;
            }   
            factor=factor+1;
        }

        multiple =factor;
        top = size/factor + 1;

        //sets all multiples of current factor to not prime
        while(multiple<top){
            numbers[factor*multiple] = false;
            multiple=multiple+1;
        }
    
    }

    
    printf("%d" , count(numbers,size,true));
    free(numbers);

}


