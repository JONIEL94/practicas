import java.util.Scanner;

public class Ejercicio2 {
	public static void main(String args[]) {
		Scanner teclado = new Scanner(System.in);

		System.out.print("Ingrese el numero del dia: " );
		Integer dia = Integer.parseInt(teclado.nextLine());

		if(dia == 1) {
			System.out.println("Usted selecciono lunes " );
		} else if(dia == 2) {
			System.out.println("Usted selecciono martes " );
		} else if(dia == 3) {
			System.out.println("Usted selecciono miercoles " );
		} else if(dia == 4) {
			System.out.println("Ustdes selecciono jueves " );
		} else if(dia == 5) {
			System.out.println("Usted selecciono viernes" );
		} else if(dia == 6) {
			System.out.println("Usted selecciono sabado " );
		} else if(dia == 7) {
			System.out.println("Usted selecciono domingo " );
    	} else {
			System.out.println("Error");
		}
	}
}
		 
