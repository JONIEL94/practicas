using System;

namespace Ejercicio1.net
{
    class Program
    {
        static void Main(string[] args)
        {
			int num1, num2, num3;

            Console.Write("Ingrese primer numero ");
			num1=int.Parse(Console.ReadLine());

			Console.Write("Ingrese 2do numero " );
			num2=int.Parse(Console.ReadLine());

			Console.Write("Ingrese 3er numero " );
			num3=int.Parse(Console.ReadLine());
		
			int suma = num1 + num2 + num3;
		  	
			Console.WriteLine("Esta esla suma : " + suma.ToString());
        }
    }
}
