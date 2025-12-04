import java.util.Scanner;
public class ejercicio11 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Introduce el primer numero");
        int numero1 = sc.nextInt();

        System.out.println("Introduce el segundo numero");
        int numero2 = sc.nextInt();

        double mcd = numero1*numero2;

        double mcm = numero1/numero2;


        for(int i =0; i<8; i++){

        System.out.println(mcm*i/mcd);
         

        }
        
sc.close();
    }
    
}
