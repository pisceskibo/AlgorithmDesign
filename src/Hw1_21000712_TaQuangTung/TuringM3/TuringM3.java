package Hw1_21000712_TaQuangTung.TuringM3;

import java.util.*;

public class TuringM3 {
    private List<String> states;        // Tập hữu hạn các trạng thái
    private List<String> alphabet;      // Bảng chữ cái
    private HashMap<String, Map<String, String[]>> rules;   // Tập các quy tắc
    private String input;

    // Khởi tạo Constructor
    public TuringM3() {
        this.states = Arrays.asList("S", "halt");
        this.alphabet = Arrays.asList("0", "1", "#");
        this.rules = createRules();
    }

    public TuringM3(String input) {
        this.input = input + "#";
        this.states = Arrays.asList("S", "halt");
        this.alphabet = Arrays.asList("0", "1", "#");
        this.rules = createRules();
    }

    // Thiết kế tập luật các quy tắc
    public HashMap<String, Map<String, String[]>> createRules() {
        this.rules = new HashMap<>();
        Map<String, String[]> transitionsQ0 = new HashMap<>();
        transitionsQ0.put("0", new String[]{"S", "1", "R"});
        transitionsQ0.put("1", new String[]{"S", "0", "R"});
        transitionsQ0.put("#", new String[]{"halt", "#", "-"});
        this.rules.put("S", transitionsQ0);

        return this.rules;
    }

    public void printRules() {
        for (Map.Entry<String, Map<String, String[]>> stateEntry : this.rules.entrySet()) {
            String state = stateEntry.getKey();
            Map<String, String[]> transitions = stateEntry.getValue();

            for (Map.Entry<String, String[]> transitionEntry : transitions.entrySet()) {
                String readSymbol = transitionEntry.getKey();
                String[] transition = transitionEntry.getValue();
                System.out.println("\t" + state + " --> " + readSymbol + " => " + transition[0] + ", " + transition[1] + ", " + transition[2]);
            }
        }
    }

    // Thiết kế thuật toán
    public String[] runAlgorithm() {
        String[] result = new String[input.length()];   // Mảng kết quả
        String[] inputData = input.split("");       // Tách chuỗi thành mảng

        int currentPosition = 0;        // Con trỏ index tương ứng của trạng thái
        String currentState = "S";

        while (!currentState.equals("halt")) {
            String[] nextResult = rules.get(currentState).get(inputData[currentPosition]);

            currentState = nextResult[0];
            result[currentPosition] = nextResult[1];

            // Dịch chuyển con trỏ currentPosition
            if (nextResult[2].equals("R")) {
                currentPosition++;
            }
        }

        return result;

    }

    public static void main(String[] args) {
        TuringM3 turingM3 = new TuringM3();
        System.out.println("Máy Turing M3:");
        System.out.println("K = " + turingM3.states);
        System.out.println("Sigma = " + turingM3.alphabet);
        System.out.println("Tập luật:");
        turingM3.printRules();
    }
}
