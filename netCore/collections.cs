using System;
using System.Collections.Generic;


namespace firstNetCore
{
    class Program
    {
        static void Main(string[] args)
        {
            // int[] practiceArray = {0,1,2,3,4,5,6,7,8,9};

            string[] stringArray = {"Tim", "Joe", "Bob"};

            // bool[] truthyArray = new bool[10] {true,false,true,false,true,false,true,false,true,false,};


            // access modifier returnType Name(paramType paramName) {content}

            //accesses =>public, private, protected 
            //modifiers =>static, new, override
            //returnTypes => voice, int, string, bool...etc

            int length = 10;
            object[,] needsRefactoring = new object[length, length];

            for (int i = 0; i < length; i++) {
                for (int j = 0; j < length; j ++) {
                needsRefactoring[i,j] = ((j + 1)*(i+1));     
                }                
            }
            // foreach (var i in needsRefactoring) {
                // Console.WriteLine(i);
            // }
            List<string> flavors = new List<string>();
            flavors.Add("chocolate");
            flavors.Add("vanilla");
            flavors.Add("strawberry");
            flavors.Add("thin-mint");
            flavors.Add("cherry");
            // Console.WriteLine(flavors.Count);
            flavors.RemoveAt(2);
            // Console.WriteLine(flavors.Count);
            Random rand = new Random();
            SortedList<string, string> peeps = new SortedList<string, string>();
            foreach (var item in stringArray) {
                peeps.Add(item, flavors[rand.Next(0, flavors.Count -1)]);
            }
            foreach(var thing in peeps) {
                Console.WriteLine(thing);
            }
            // Console.WriteLine(peeps["Tim"]);
        }
    }
}

