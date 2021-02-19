// Example program
#include <iostream>
#include <string>


using std::string;

string input(string name="What is your name? -")
{
    std::cout << name;
    getline (std::cin, name);
    return name;
};


void hi(void)
{
  string name = input();
  std::cout << "Hello, " << name << "!\n";
};


int main(void)
{
    hi();
    
    return 0;
};
