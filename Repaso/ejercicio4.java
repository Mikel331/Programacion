import java.util.Scanner;
public class ejercicio4 {

    public static void main(String[]args){

        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce el numero para factorizar");
        int numero = sc.nextInt();

        int factorial=1;

        for(int i=1; i<=numero; i++ ){
            factorial*=i;
        }  
        System.out.println("El numero:" + " " + numero+ " " + "numero factorial:"+ " " + factorial);
      
    }
    
}
