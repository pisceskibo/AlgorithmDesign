package Hw3_21000712_TaQuangTung.Practice01;

import java.util.Scanner;

public class QueenChessBackTracking {
    private int[] board;
    private int numberOfSolutions = 0;

    public QueenChessBackTracking(int n) {
        board = new int[n];
    }

    // Phương thức chính để giải bài toán
    public void solve() {
        placeQueen(0);
        System.out.println("Số cách đặt quân hậu: " + numberOfSolutions);
    }

    // Phương thức quay lui để đặt quân hậu
    private void placeQueen(int row) {
        int n = board.length;
        if (row == n) {
            // Tìm được một cách xếp, in ra kết quả
            printSolution();
            numberOfSolutions++;
        } else {
            for (int col = 0; col < n; col++) {
                if (canPlace(row, col)) {
                    board[row] = col;
                    placeQueen(row + 1);
                    // Không cần phục hồi trạng thái trước đó vì mỗi lần đệ quy là một mảng mới
                }
            }
        }
    }

    // Kiểm tra xem có thể đặt quân hậu vào ô này không
    private boolean canPlace(int row, int col) {
        for (int i = 0; i < row; i++) {
            if (board[i] == col || Math.abs(board[i] - col) == Math.abs(i - row)) {
                return false;
            }
        }
        return true;
    }

    // In ra một cách xếp hợp lệ
    private void printSolution() {
        int n = board.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(board[i] == j ? "Q " : ". ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhập kích cỡ bàn cờ: ");
        int size = sc.nextInt();
        QueenChessBackTracking nQueens = new QueenChessBackTracking(size);
        nQueens.solve();
    }
}
