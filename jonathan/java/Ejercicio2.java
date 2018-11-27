import java.util.Scanner;

public class Ejercicio2{
		public static void main (String args[]){
			Scanner teclado= new Scanner(System.in);

			System.out.print("Ingrese su edad: ");
			int edad=teclado.nextInt();

			if(edad>=18)
				System.out.println("Usted es mayor de edad");
		}
}
