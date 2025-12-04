import java.util.Scanner;
public class ejercicio10 {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        System.out.println("Introduce el numero");
        int numero = sc.nextInt();

        for(int i=0; i<11; i++){
            System.out.println(i*numero);
        }
       sc.close(); 
    }
    
}
