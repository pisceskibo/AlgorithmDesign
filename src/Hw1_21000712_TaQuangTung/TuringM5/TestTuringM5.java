package Hw1_21000712_TaQuangTung.TuringM5;

import java.util.Scanner;

public class TestTuringM5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a binary number: ");
        String binary = sc.nextLine();
        TuringM5 turingM5 = new TuringM5(binary);
        System.out.println(binary + " có đối xứng? - " + turingM5.runAlgorithm());
    }
}
