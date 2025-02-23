package Hw1_21000712_TaQuangTung.TuringM2;

import java.util.*;

public class TuringM2 {
    private List<String> states;        // Tập hữu hạn các trạng thái
    private List<String> alphabet;      // Bảng chữ cái
    private HashMap<String, Map<String, String[]>> rules;   // Tập các quy tắc
    private String input;

    // Khởi tạo Constructor
    public TuringM2() {
        this.states = Arrays.asList("q0", "q1", "halt");
        this.alphabet = Arrays.asList("0", "1", "#");
        this.rules = createRules();
    }

    public TuringM2(String input) {
        this.input = input + "#";
        this.states = Arrays.asList("q0", "q1", "halt");
        this.alphabet = Arrays.asList("0", "1", "#");
        this.rules = createRules();
    }

    // Thiết kế tập luật các quy tắc
    public HashMap<String, Map<String, String[]>> createRules() {
        this.rules = new HashMap<>();
        Map<String, String[]> transitionsQ0 = new HashMap<>();
        transitionsQ0.put("0", new String[]{"q0", "0", "R"});
        transitionsQ0.put("1", new String[]{"q0", "1", "R"});
        transitionsQ0.put("#", new String[]{"q1", "#", "L"});
        this.rules.put("q0", transitionsQ0);

        Map<String, String[]> transitionsQ1 = new HashMap<>();
        transitionsQ1.put("0", new String[]{"q1", "1", "L"});
        transitionsQ1.put("1", new String[]{"halt", "0", "-"});
        this.rules.put("q1", transitionsQ1);

        return this.rules;
    }

    // Hiển thị ra các tập luật
    public void printRules() {
        List<Map.Entry<String, Map<String, String[]>>> entries = new ArrayList<>(this.rules.entrySet());
        Collections.reverse(entries);       // Đảo ngược thứ tự của các entries

        for (Map.Entry<String, Map<String, String[]>> stateEntry : entries) {
            String state = stateEntry.getKey();
            Map<String, String[]> transitions = stateEntry.getValue();

            for (Map.Entry<String, String[]> transitionEntry : transitions.entrySet()) {
                String readSymbol = transitionEntry.getKey();
                String[] transition = transitionEntry.getValue();
                System.out.println("\t" + state + " --> " + readSymbol + " => " + transition[0] + ", " + transition[1] + ", " + transition[2]);
            }
        }
    }

    // Thực hiện thuật toán
    public String[] runAlgorithm() {
        String[] result = new String[input.length()];   // Mảng kết quả
        String[] inputData = input.split("");       // Tách chuỗi thành mảng

        int currentPosition = 0;        // Con trỏ index tương ứng của trạng thái
        String currentState = "q0";

        while (!currentState.equals("halt")) {
            String[] nextResult = rules.get(currentState).get(inputData[currentPosition]);

            currentState = nextResult[0];
            result[currentPosition] = nextResult[1];

            // Dịch chuyển con trỏ currentPosition
            if (nextResult[2].equals("L")) {
                currentPosition--;
            } else if (nextResult[2].equals("R")) {
                currentPosition++;
            }
        }

        return result;
    }


    public static void main(String[] args) {
        TuringM2 turingM2 = new TuringM2();
        System.out.println("Máy Turing M2:");
        System.out.println("K = " + turingM2.states);
        System.out.println("Sigma = " + turingM2.alphabet);
        System.out.println("Tập luật:");
        turingM2.printRules();
    }
}
