package Hw1_21000712_TaQuangTung.TuringM1;

import java.util.Scanner;

public class TestTuringM1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a binary number: ");
        String binary = sc.nextLine();
        TuringM1 turingM1 = new TuringM1(binary);

        String finalString = "";
        for (int i = 0; i < turingM1.runAlgorithm().length - 1; i++) {
            finalString += turingM1.runAlgorithm()[i];
        }
        System.out.println(binary + " + 1 = " + finalString);
    }
}
