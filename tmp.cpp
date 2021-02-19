// Example program
#include <iostream>
#include <string>

using std::string;
using std::cout;


string input(string name)
{
    using std::cin;
    cout << name;
    getline (cin, name);
    return name;
}


void hi(void)
{
  string name = input("What is your name? \n-");
  cout << "Hello, " << name << "!\n";
}


int main(void)
{
    hi();
    return 0;
}
