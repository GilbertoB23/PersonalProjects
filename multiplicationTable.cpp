// Project 1 - Multiplication Table Generator
#include <iostream>

void GenerateMultiplicationTable(int num, int range)
{
  std::cout << "Generating multiplcation table...\n";
  std::cout << "Multpiplication Table for " << num << ":\n";
  for (int i = 1; i <= range; i++)
  {
    int res = num * i;
    std::cout << num << " x " << i << " = " << res << '\n';
  }
}

int main()
{
  int number, range;
  std::cout << "Enter a number to generate the multiplication table for: ";
  std::cin >> number;
  while (number < 0)
  {
    std::cout << "Enter a positive number: ";
    std::cin >> number;
  }
  std::cout << "Enter the range: ";
  std::cin >> range;
  while (range < 0)
  {
    std::cout << "Enter a positive number: ";
    std::cin >> range;
  }
  GenerateMultiplicationTable(number, range);
  return 0;
}