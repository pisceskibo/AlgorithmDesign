package Hw3_21000712_TaQuangTung.Practice02.Combination;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CombinationBacktracking {
    public static void generateCombinations(int n, int k) {
        backtrack(new ArrayList<>(), 1, n, k);
    }

    private static void backtrack(List<Integer> current, int start, int n, int k) {
        if (current.size() == k) {
            System.out.println(current);
            return;
        }

        for (int i = start; i <= n; i++) {
            current.add(i);
            backtrack(current, i + 1, n, k);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("n = ");
        int n = sc.nextInt();
        System.out.print("k = ");
        int k = sc.nextInt();
        generateCombinations(n, k);
    }
}
