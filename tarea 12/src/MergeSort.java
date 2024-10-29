import java.util.Arrays;

public class MergeSort {
    public static void main(String[] args) {
        int[] numeros = {100,20,25,43,21,14,12,7,6,3,2};
        ordenarPorMezcla(numeros);
        System.out.println("Array ordenado: " + Arrays.toString(numeros));
    }

    public static void ordenarPorMezcla(int[] numeros) {
        if (numeros.length <= 1) {
            return;  // No se necesita ordenar si el arreglo tiene 1 o menos elementos
        }

        int mitad = numeros.length / 2;
        int[] parteIzquierda = Arrays.copyOfRange(numeros, 0, mitad);
        int[] parteDerecha = Arrays.copyOfRange(numeros, mitad, numeros.length);

        ordenarPorMezcla(parteIzquierda);  // Ordenar la mitad izquierda
        ordenarPorMezcla(parteDerecha);    // Ordenar la mitad derecha

        combinar(numeros, parteIzquierda, parteDerecha);  // Combinar ambas mitades
    }

    private static void combinar(int[] resultado, int[] izquierda, int[] derecha) {
        int indiceIzq = 0, indiceDer = 0, indiceRes = 0;

        while (indiceIzq < izquierda.length && indiceDer < derecha.length) {
            if (izquierda[indiceIzq] < derecha[indiceDer]) {
                resultado[indiceRes++] = izquierda[indiceIzq++];
            } else {
                resultado[indiceRes++] = derecha[indiceDer++];
            }
        }

        // Añadir los elementos restantes de la izquierda, si los hay
        while (indiceIzq < izquierda.length) {
            resultado[indiceRes++] = izquierda[indiceIzq++];
        }

        // Añadir los elementos restantes de la derecha, si los hay
        while (indiceDer < derecha.length) {
            resultado[indiceRes++] = derecha[indiceDer++];
        }
    }
}