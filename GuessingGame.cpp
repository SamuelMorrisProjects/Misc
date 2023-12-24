#include <random>
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int guess;
    random_device dev;
    mt19937 rng(dev());
    uniform_int_distribution<std::mt19937::result_type> dist6(1,10); 
    cout<<"Guess a number between one and ten: ";
    cin>>guess; 
    int rand_num;
    rand_num = dist6(rng);
    while (guess!=rand_num){
        cout<<"You got it wrong Guess again!\nGuess a number between one and ten: "; cin>>guess;
    }
    cout<<"You got it!!";
    return 0;
}