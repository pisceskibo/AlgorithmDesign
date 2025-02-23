package Hw1_21000712_TaQuangTung.TuringM1;

import java.util.*;

public class TuringM1 {
    private List<String> states;           // Tập trạng thái
    private List<String> alphabet;         // Bảng chữ cái
    private HashMap<String, Map<String, String[]>> rules;        // Tập quy tắc sinh
    private String input;           // String đầu vào

    // Khởi tạo Constructor
    public TuringM1() {
        this.states = Arrays.asList("q0", "q1", "halt");
        this.alphabet = Arrays.asList("0", "1", "#");
        this.rules = createRules();
    }

    public TuringM1(String input) {
        this.input = "0" + input + "#";
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
        transitionsQ1.put("0", new String[]{"halt", "1", "-"});
        transitionsQ1.put("1", new String[]{"q1", "0", "L"});
        this.rules.put("q1", transitionsQ1);

        return this.rules;
    }

    // Hiển thị ra các luật
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

    // Thực hiện chương trình
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
        TuringM1 turingM1 = new TuringM1();
        System.out.println("Máy Turing M1:");
        System.out.println("K = " + turingM1.states);
        System.out.println("Sigma = " + turingM1.alphabet);
        System.out.println("Tập luật:");
        turingM1.printRules();
    }
}
