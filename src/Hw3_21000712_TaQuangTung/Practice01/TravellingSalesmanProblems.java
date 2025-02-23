package Hw3_21000712_TaQuangTung.Practice01;

import java.util.Arrays;

public class TravellingSalesmanProblems {
    private int numberCity;
    private int[][] distanceMatrix; // Ma trận khoảng cách giữa các thành phố
    private boolean[] visited; // Các thành phố đã đi qua hay chưa
    private int bestCost = Integer.MAX_VALUE; // Lưu giá trị chi phí tối ưu
    private int[] currentPath; // Lưu đường đi hiện tại
    private char[] bestPath; // Lưu đường đi tối ưu

    public TravellingSalesmanProblems(int[][] distanceMatrix) {
        numberCity = distanceMatrix.length;
        this.distanceMatrix = distanceMatrix;
        visited = new boolean[numberCity];
        currentPath = new int[numberCity + 1];
        bestPath = new char[numberCity + 1];
    }

    /*
    level: số lượng thành phố đã thăm
    currCost: chi phí tổng cộng từ đầu đến 'indexCurrent'
     */
    public void tsp(int indexCurrent, int currCost, int level) {
        // Nếu duyệt hết các thành phố và về lại thành phố ban đầu
        if (level == numberCity && distanceMatrix[indexCurrent][0] > 0) {
            int cmin = distanceMatrix[indexCurrent][0];
            for (int j = 0; j < level; j++) {
                if (cmin > distanceMatrix[indexCurrent][j]) {
                    cmin = distanceMatrix[indexCurrent][j];
                }
            }

            int totalCost = currCost + (numberCity - indexCurrent + 1)*cmin;
            if (totalCost < bestCost) {
                bestCost = totalCost;
                for (int i = 0; i < numberCity; i++) {
                    bestPath[i] = (char) ('A' + currentPath[i]);
                }
                bestPath[numberCity] = 'A'; // Quay lại thành phố bắt đầu
            }
            return;
        }

        for (int i = 0; i < numberCity; i++) {
            if (!visited[i] && distanceMatrix[indexCurrent][i] > 0) {
                visited[i] = true;
                currentPath[level] = i;
                tsp(i, currCost + distanceMatrix[indexCurrent][i], level + 1);
                visited[i] = false;
            }
        }
    }

    public void solve() {
        Arrays.fill(visited, false);
        visited[0] = true;
        currentPath[0] = 0;
        tsp(0, 0, 1);
        System.out.println("Chi phí tối thiểu: " + bestCost);
        System.out.print("Đường đi: ");
        for (int i = 0; i <= numberCity; i++) {
            System.out.print(bestPath[i] + " ");
        }
    }

    public static void main(String[] args) {
        int[][] distanceMatrix = {
                {0, 10, 15, 20},
                {10, 0, 35, 25},
                {15, 35, 0, 30},
                {20, 25, 30, 0}
        };
        TravellingSalesmanProblems solver = new TravellingSalesmanProblems(distanceMatrix);
        solver.solve();
    }
}
