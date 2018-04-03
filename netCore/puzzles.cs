using System;
using System.Collections.Generic;


namespace firstNetCore
{
    class Program
    {
        static void Main(string[] args)
        {
               RandomArr(); 
        // Coin Flip
        // Create a function called TossCoin() that returns a string
        // 
        // Have the function print "Tossing a Coin!"
        // Randomize a coin toss with a result signaling either side of the coin 
        // Have the function print either "Heads" or "Tails"
        // Finally, return the result
        // Create another function called TossMultipleCoins(int num) that returns a Double
        // 
        // Have the function call the tossCoin function multiple times based on num value
        // Have the function return a Double that reflects the ratio of head toss to total toss
        // Names
        // Build a function Names that returns an array of strings
        // 
        // Create an array with the values: Todd, Tiffany, Charlie, Geneva, Sydney
        // Shuffle the array and print the values in the new order
        // Return an array that only includes names longer than 5 characters
        
        }
        public static void RandomArr() {
            Random rand = new Random();
            int[] randomArr = new int[10];
            for (int i = 0; i < randomArr.Length; i++) {
                randomArr[i] = rand.Next(5, 25);
            }
            int sum = 0;
            int min = randomArr[0];
            int max = randomArr[0];
            foreach (int item in randomArr) {
                sum += item;
                if (item < min) {
                    min = item;
                }
                if (item > max) {
                    max = item;
                }
            }
            Console.WriteLine("This assignment is a study in c# syntax. As I will continue to explore syntax as I go on, I'm leaving this as is and will return to it another day.");
        }
        
    }
}

