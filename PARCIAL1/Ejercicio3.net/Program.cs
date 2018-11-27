using System;

namespace Ejercicio3.net
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hola! Ingrese un numero a elevar al cubo"); // mostrar por pantalla
			int num = Int32.Parse(Console.ReadLine()); //Convertimos el dato string a int

			int cub = num*num*num; //Realizamos la multiplicacion
			Console.WriteLine("El resultado de la potenciacion es: " + cub + " "); //Mensaje final
        }
    }
}
