using System;

namespace Ejercicio2.net
{
    class Program
    {
        static void Main(string[] args)
        {
		string=respuesta;
            Console.WriteLine("ingrese el dia de la semana");
							int dia = int32.Parse(console.ReadLine());
		switch(dia){
			case 1:
				respuesta="Lunes";
				break;
		    case 2:
				respuesta="Martes";
				break;
	     	case 3:
				 respuesta="Miercoles";
				 break;

	    	case 4:
		 		 respuesta="Jueves";
				 break;
		    case 5:
				 respuesta="Viernes";
				 break;
			case 6:
				 respuesta="Sabado";
				 break;
			case 7:
				 respuesta="Domingo";
				 break;
			default:
					respuesta="Error";
					break;
		}
			Console.WriteLine(respuesta);

          	
        }
    }
