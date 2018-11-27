import java.util.Scanner;

public class Ejercicio2bis {
	public static void main(String args[]) {
		Scanner teclado = new Scanner(System.in);

		System.out.print("Ingrese el numero del dia: " );
		Integer dia = Integer.parseInt(teclado.nextLine());
       String respuesta;
		switch(dia) {
			case 1:
				respuesta="lunes";
				break;
			case 2:
				respuesta="martes";
				break;
			case 3:
				respuesta="miercoles";
				break;
			case 4:
			    respuesta="jueves";
				break;
			case 5:
				respuesta="viernes";
				break;
			case 6:
				respuesta="sabado";
				break;
			case 7:
			 	respuesta="domingo";
				break;
			default:
					respuesta="error";
					break;
                    }
	        	System.out.println(respuesta);
	    	}
        }
		 
