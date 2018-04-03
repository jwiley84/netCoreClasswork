using System;
using System.Collections.Generic;


namespace firstNetCore
{
    class Program
    {
        static void Main(string[] args)
        {
            // PrintNums(255); // 1
            // PrintOdd(255); // 2
            // PrintSum(10); // 3
            int[] numArr = {-7,2,3,4, -11, 1};
            object[] numArr2 = {1, 0, -2, 14, .11, 9};
            // IterArr(numArr); // 4
            // FindMax(numArr); // 5
            // GetAverage(numArr); // 6
            // OddArr(10); // 7
            // GTY(numArr, 2); // 8
            // sqArr(numArr); // 9
            // ElemNeg(numArr); // 10
            // MinMaxAvg(numArr); // 11
            // ShiftVals(numArr); // 12
            Testy(numArr2);// 13
        }


        public static void PrintNums(int num) {
            for (int i = 1; i <=num; i++) {
                Console.WriteLine(i);
            }
        }
        public static void PrintOdd(int num) {
            for (int i = 1; i <= num; i++) {
                if (i % 2 == 1) {
                    Console.WriteLine(i);
                }
            }
        }
        public static void PrintSum(int num) {
            int sum = 0;
            for (int i = 0; i <= num; i++) {
                sum += i;
                Console.WriteLine("New Number: " + i + "; Sum: " + sum);
            }        }public static void IterArr(int[] arr) {
            foreach (var item in arr) {
                Console.WriteLine(item);
            }
        }
        public static int FindMax(int[] arr) {
            int max = arr[0];
            foreach (int number in arr) {
                if (number >= max) {
                    max = number;
                }
            }
            Console.WriteLine(max);
            return max;
        }
        public static int GetAverage(int[] arr) {
            int sum = 0;
            foreach (int item in arr) {
                sum += item;
            }
            int avg = sum/arr.Length;
            Console.WriteLine(avg);
            return avg;
        }
        public static int[] OddArr(int num) {
            List<int> holderList = new List<int>();
            int[] oddArray = new int[(int)num/2];

            for (int i = 0; i <= num; i++) {
                if (i % 2 == 1) {
                    holderList.Add(i);
                }

            }
            oddArray = holderList.ToArray();
            // foreach (var item in oddArray){
            //     Console.WriteLine(item);
            // }
            return oddArray;

        }
        public static int GTY(int[] arr, int num) {
            int total = 0;
            foreach (int val in arr) {
                if (val > num) {
                    total++;
                }
            }
            // Console.WriteLine(total);
            return total;
        }

        public static void sqArr(int[] arr) {
            for(int i = 0; i < arr.Length; i++) {
                arr[i] = arr[i] * arr[i];
                Console.WriteLine(arr[i]);
            }
        }

        public static void ElemNeg(int[] arr) {
            for (int i = 0; i< arr.Length; i++) {
                if (arr[i] < 0) {
                    arr[i] = 0;
                }
                Console.WriteLine(arr[i]);
            }
        }

        public static void MinMaxAvg(int[] arr) {
            int max = arr[0];
            int min = arr[0];
            int sum = 0;
            foreach (int number in arr) {
                sum += number;
                if (number >= max) {
                    max = number;
                }
                if (number <= min) {
                    min = number;
                }
            }
            Console.WriteLine("Max: " + max);
            Console.WriteLine("Min: " + min);
            int avg = sum/arr.Length;
            Console.WriteLine("Avg: " + avg);
        }

        public static void ShiftVals(int[] arr) {
            // int temp = 
            for(int i = 0; i < arr.Length-1; i++) {
                arr[i] = arr[i+1];
            }
            arr[arr.Length -1] = 0;
            for(int i = 0; i < arr.Length; i++) {
                Console.WriteLine(arr[i]);
            }
        }

         public static object Testy(object[] numArr) {
                        
            for(int i = 0; i < numArr.Length-1; i++){
                int test = (int)i;
                if (test < 0) {
                    numArr[i] = false;
                }
            }            
            return numArr;
        }
    }
}

