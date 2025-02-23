package Hw3_21000712_TaQuangTung.Practice01;

import java.util.Scanner;

public class ListBinaryBackTracking {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int size = sc.nextInt();
        int[] array = new int[size];
        binaryStrings(size, array, 0);
    }

    // Hàm đệ quy để in tất cả dãy nhị phân có độ dài n
    public static void binaryStrings(int n, int arr[], int i) {
        if (i == n) {
            // Khi đã điền đủ n phần tử, in dãy nhị phân
            printArray(arr, n);
            return;
        }

        // Đặt giá trị tại vị trí i là 0 và quay lui
        arr[i] = 0;
        binaryStrings(n, arr, i + 1);

        // Đặt giá trị tại vị trí i là 1 và quay lui
        arr[i] = 1;
        binaryStrings(n, arr, i + 1);
    }

    // Hàm để in mảng
    public static void printArray(int arr[], int n) {
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i]);
        }
        System.out.println();
    }
}
