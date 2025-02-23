package Hw3_21000712_TaQuangTung.Practice01;

import java.util.Scanner;

public class KnightsTourBackTracking {
    private int size;
    private int[][] solutionMatrix;     // Các đường đi thỏa mãn

    // Hướng di chuyển của quân mã
    private static final int[] xMove = {2, 1, -1, -2, -2, -1, 1, 2};
    private static final int[] yMove = {1, 2, 2, 1, -1, -2, -2, -1};

    // Khởi tạo Constructor
    public KnightsTourBackTracking(int size) {
        this.size = size;
        this.solutionMatrix = new int[size][size];
        solutionMatrix = initializeBoard();
    }

    private int[][] initializeBoard() {
        for (int x = 0; x < size; x++) {
            for (int y = 0; y < size; y++) {
                solutionMatrix[x][y] = -1;
            }
        }
        return solutionMatrix;
    }

    private boolean isSafe(int x, int y) {
        return (x >= 0 && x < size && y >= 0 && y < size && solutionMatrix[x][y] == -1);
    }

    private boolean solveKT(int x, int y, int movei) {
        if (movei == size * size) {
            return true;
        }

        for (int k = 0; k < 8; k++) {
            int nextX = x + xMove[k];
            int nextY = y + yMove[k];
            if (isSafe(nextX, nextY)) {
                solutionMatrix[nextX][nextY] = movei;
                if (solveKT(nextX, nextY, movei + 1)) {
                    return true;
                } else {
                    // Quay lui
                    solutionMatrix[nextX][nextY] = -1;
                }
            }
        }
        return false;
    }

    public boolean solveKnightsTour() {
        solutionMatrix[0][0] = 0; // Bắt đầu từ ô đầu tiên
        if (!solveKT(0, 0, 1)) {
            return false;
        } else {
            printSolution();
            return true;
        }
    }

    // In ra các trường hợp thỏa mãn
    private void printSolution() {
        for (int x = 0; x < size; x++) {
            for (int y = 0; y < size; y++) {
                System.out.print(solutionMatrix[x][y] + "\t");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhập kích cỡ bàn cờ: ");
        int size = sc.nextInt();
        KnightsTourBackTracking knight = new KnightsTourBackTracking(size);
        knight.solveKnightsTour();
    }
}
