package Hw1_21000712_TaQuangTung.TuringM6;

import java.util.Arrays;
import java.util.Scanner;

public class TestTuringM6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input a string: ");
        String input = sc.nextLine();
        TuringM6 turingM6 = new TuringM6(input);

        String finalString = "";
        for (String ele : turingM6.runAlgorithm()) {
            finalString += ele;
        }
        System.out.println(input + " khi thêm khoảng trắng sẽ thành: " + finalString);
    }
}
