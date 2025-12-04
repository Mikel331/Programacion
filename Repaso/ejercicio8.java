public class ejercicio8 {
    
    public static void main(String[] args) {
        
        String[] array_letras = {"a","e","i","o","u"};
        String palabra = "Ornitorrinco";
        int contador=0;
        int contadorVocales=0;

        for(int i=0; i<palabra.length(); i++){
             char letra = palabra.charAt(i);
           contador++;
         
           for(String vocal: array_letras){
            if(String.valueOf(letra).equals(vocal))
            contadorVocales++;
           }
           
        }

        System.out.println("Tiene "+ " " + palabra + " " + contador +" " + "letras en total y " + " " + contadorVocales + " " + "vocales");
    }
}
