using System;

namespace pedro.net
{
    class Program
    {
        static void Main(string[] args)
        {
            string nombre;
			Console.Write("Ingrese su nombre: ");
			nombre = Console.ReadLine();
			
			if (nombre == "pedro") {
				Console.WriteLine("Hola Pedro");
				Console.ReadKey();
			}
		}
    }
}
