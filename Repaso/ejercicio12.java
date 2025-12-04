import java.util.Scanner;
public class ejercicio12 {
    
    public static void main(String[]args){

        Scanner sc = new Scanner(System.in);


        System.out.println("Introduce el primer numero");
        int num1 = sc.nextInt();
        System.out.println("Introduce el segundo numero");
        int num2 = sc.nextInt();

        System.out.println("1.Suma");
        System.out.println("2.Resta");
        System.out.println("3.Multiplicacion");
        System.out.println("4.Division");
        int opcion = sc.nextInt();



            switch (opcion) {
                case 1:
                System.out.println("La suma es de: " + (num1+num2)); 
                break;

                case 2:
                System.out.println("La resta es de: " + (num1-num2));
                break;

                case 3:
                System.out.println("La multiplicacion es de: " + (num1*num2));
                break;

                case 4:
                System.out.println("La division es de: " + (num1/num2));
                if(num2 ==0){
                    System.out.println("error");
                }
                break;
            
                default:
                    break;
            }


    }
}
