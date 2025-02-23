package Hw1_21000712_TaQuangTung.TuringM2;

import java.util.Scanner;

public class TestTuringM2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a binary number: ");
        String binary = sc.nextLine();
        TuringM2 turingM2 = new TuringM2(binary);

        String finalString = "";
        for (int i = 0; i < turingM2.runAlgorithm().length - 1; i++) {
            finalString += turingM2.runAlgorithm()[i];
        }
        System.out.println(binary + " - 1 = " + finalString);
    }
}
