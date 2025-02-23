package Hw1_21000712_TaQuangTung.TuringM3;

import java.util.Scanner;

public class TestTuringM3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a binary number: ");
        String binary = sc.nextLine();
        TuringM3 turingM3 = new TuringM3(binary);

        String finalString = "";
        for (int i = 0; i < turingM3.runAlgorithm().length - 1; i++) {
            finalString += turingM3.runAlgorithm()[i];
        }
        System.out.println(binary + " --> " + finalString);
    }
}
