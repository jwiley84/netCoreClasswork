using System;
using System.Collections.Generic;


namespace algoPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            Sigma_two(5);
        }

        public static int Sigma_two(int num) {
            int sum = 0;
            while(num > 0) {
                sum += num;
                num--;
            }
            
            Console.WriteLine(sum);
            return sum;
        }

        //array of ints, remove >0, change to false boolean
        //
        //
        // public static List<string> Swappy(int[] numArr) {
        //     List<string> changedList = new List<string>;

        //     foreach (var item in numArr){
        //         if (item >= 0) {
        //             // add item to changedList;
        //             string newItem = item.ToString();

        //             changedList.Add(newItem);
        //         }
        //         else {
        //             // add(false);
        //             string fakeBool = "false";
        //             changedList.Add(fakeBool);
        //         }
        //         }
        //     return changedList;
        // }
        public static object Testy(object[] numArr) {
                        
            foreach (var item in numArr){
                int test = (int)item;
                if (test < 0) {
                    numArr[test] = false;
                }
            }            
            return numArr;
        }
    }
}
