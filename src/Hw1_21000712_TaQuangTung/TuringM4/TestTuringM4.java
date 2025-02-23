package Hw1_21000712_TaQuangTung.TuringM4;

import java.util.Scanner;

public class TestTuringM4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a binary number: ");
        String binary = sc.nextLine();
        TuringM4 turingM4 = new TuringM4(binary);

        System.out.println(binary + " --> " + turingM4.runAlgorithm());
    }
}
