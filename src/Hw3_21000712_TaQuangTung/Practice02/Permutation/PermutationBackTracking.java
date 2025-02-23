package Hw3_21000712_TaQuangTung.Practice02.Permutation;

public class PermutationBackTracking {
    private int[] array;

    // Khởi tạo Constructor
    public PermutationBackTracking(int[] array) {
        this.array = array;
    }

    // Hàm để in mảng
    private static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    // Hàm để hoán đổi giữa arr[i] và arr[j]
    private static void swap(int[] arr, int i, int j) {
        if (arr[i] != arr[j]) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    // Hàm đệ quy để sinh hoán vị bằng backtracking
    private void generatePermutations(int[] arr, int currentIndex) {
        if (currentIndex == arr.length - 1) {
            printArray(arr);
        }

        for (int i = currentIndex; i < arr.length; i++) {
            swap(arr, currentIndex, i);
            generatePermutations(arr, currentIndex + 1);
            swap(arr, currentIndex, i);         // Quay lui
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3};
        PermutationBackTracking permutationBackTracking = new PermutationBackTracking(arr);
        permutationBackTracking.generatePermutations(arr, 0);
    }

}
