package Hw3_21000712_TaQuangTung.Practice01;

import java.util.Scanner;

public class BagBranch {
    private int numberItems; // Số lượng đồ vật
    private int[] arrayItems; // Mảng chứa khối lượng của đồ vật loại i
    private int[] arrayMoney; // Mảng chứa số tiền tương ứng của đồ vật i
    private int maxWeight; // Trọng lượng tối đa của túi

    // Khởi tạo Constructor
    public BagBranch(int numberItems, int[] arrayItems, int[] arrayMoney, int maxWeight) {
        this.numberItems = numberItems;
        this.arrayItems = arrayItems;
        this.arrayMoney = arrayMoney;
        this.maxWeight = maxWeight;
    }

    // Hàm giải quyết bài toán cái túi bằng phương pháp nhánh cận
    public int bagSolve() {
        return solveRecursively(0, maxWeight, 0);
    }

    // Hàm đệ quy để giải bài toán
    private int solveRecursively(int index, int remainingWeight, int currentMoney) {
        // Kiểm tra điều kiện dừng
        if (index == numberItems || remainingWeight == 0) {
            return currentMoney;
        }

        // Chọn đồ vật hiện tại nếu có thể
        int withItem = 0;
        if (arrayItems[index] <= remainingWeight) {
            withItem = solveRecursively(index, remainingWeight - arrayItems[index], currentMoney + arrayMoney[index]);
        } else {
            withItem = solveRecursively(index + 1, remainingWeight, currentMoney);
        }

        return withItem;
    }

    public static void main(String[] args) {
        int numberItems = 4;
        int[] arrayItems = {5, 3, 2, 4};
        int[] arrayMoney = {10, 5, 3, 6};
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the maximum of the bag: ");
        int maxWeight = sc.nextInt();
        // int maxWeight = 27;

        BagBranch bag = new BagBranch(numberItems, arrayItems, arrayMoney, maxWeight);
        System.out.println("Maximum value in the bag: " + bag.bagSolve());
    }
}
