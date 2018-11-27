import java.util.Scanner;

public class Ejercicio1 {
	public static void main(String args[]){
		Scanner keyboard = new Scanner(System.in);

		Integer num;
		System.out.print("Ingrese un numero: ");
		Integer num = Integer.parseInt(keyboard.nextLine());

		while(num <= 100){
			System.out.print("Ingrese un numero: ");
			Integer num = Integer.parseInt(keyboard.nextLine());
			}
		}
}
