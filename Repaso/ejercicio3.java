import java.util.Scanner;
public class ejercicio3 {

    public static void main(String[]args){

        Scanner sc = new Scanner(System.in);

        System.out.println("Introduce el numero");
        int numero = sc.nextInt();

        

        if(numero%2 ==0){
            System.out.println("El numero es par");
        }else{
            System.out.println("El numero es impar");
        }
        sc.close();
    }
    
    
}
