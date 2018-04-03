using System;
using System.Collections.Generic;


namespace firstNetCore
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> things = new List<object>();
            things.Add(7);
            things.Add(28);
            things.Add(-1);
            things.Add(true);
            things.Add("puppy");
            things.Add("Admiral");
            int sum = 0;
            foreach (var item in things){
                Console.WriteLine(item);

                if(item is int) {
                    sum += (int)item;
                }
            }
            Console.WriteLine(sum);
        }
    }
}
