// Example program
#include <iostream>
#include <string>

using std::string;
using std::cout;
using std::cin;


string input(string name="What is your name? -")
{
    cout << name;
    getline (cin, name);
    return name;
}


void hi(void)
{
  string name = input();
  cout << "Hello, " << name << "!\n";
}


int main(void)
{
    hi();
    return 0;
}
