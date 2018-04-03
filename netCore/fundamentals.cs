using System;

namespace firstNetCore
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 255; i++) {
                Console.WriteLine(i);
            }
            
            for (int i = 1; i <= 100; i++) {
                if (i % 5 == 0 && i % 3 == 0) {
                    Console.WriteLine(i)
                }
            }
            
            for (int i = 1; i <= 100; i++) {
                if (i % 15 == 0) {
                    Console.WriteLine("FizzBuzz");
                }
                else if (i % 5 == 0) {
                    Console.WriteLine("Buzz");
                }
                else if ( i % 3 == 0) {
                    Console.WriteLine("Fizz");
                }
                else {
                    Console.WriteLine(i);
                }
            }


            Console.WriteLine("Hihi World!");
            Console.WriteLine("I think I may be bored in this class too. Luckily I have the Udemy course.");
            Console.WriteLine("Never forget your semi-colons, and I purposefully fudged this line.");
        }
    }
}
