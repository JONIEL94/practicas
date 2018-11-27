import java.util.Scanner;

public class Ejercicio2 {
	public static void main(String args[]){
		Scanner keyboard = new Scanner(System.in);

		System.out.print("Hola! Ingrese numero de inicio : ");
		Integer numi = Integer.parseInt(keyboard.nextLine());

		System.out.print("Por favor ingrese numero de fin : ");
		Integer numf = Integer.parseInt(keyboard.nextLine());

		System.out.print("Ingrese Numero de referencia : ");
		Integer numr = Integer.parseInt(keyboard.nextLine());

		for(Integer i = numi; i<=numf; i++)
			System.out.println(i);
		}
}
