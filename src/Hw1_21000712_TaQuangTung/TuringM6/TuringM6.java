package Hw1_21000712_TaQuangTung.TuringM6;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TuringM6 {
    private List<String> states;        // Tập hữu hạn các trạng thái
    private List<String> alphabet;      // Bảng chữ cái
    private HashMap<String, Map<String, String[]>> rules;   // Tập các quy tắc
    private String input;

    // Khởi tạo Constructor
    public TuringM6() {
        this.states = Arrays.asList("q0", "q1", "halt");
        this.alphabet = Arrays.asList("i", "#");
        this.rules = createRules();
    }

    public TuringM6(String input) {
        this.input = input + "#";
        this.states = Arrays.asList("q0", "q1", "halt");
        this.alphabet = Arrays.asList("i", "#");
        this.rules = createRules();
    }

    // Thiết kế tập luật các quy tắc
    public HashMap<String, Map<String, String[]>> createRules() {
        this.rules = new HashMap<>();
        Map<String, String[]> transitionsQ0 = new HashMap<>();
        transitionsQ0.put("i", new String[]{"q0", "i", "R"});
        transitionsQ0.put("#", new String[]{"q1", "#", "L"});
        this.rules.put("q0", transitionsQ0);

        Map<String, String[]> transitionsQ1 = new HashMap<>();
        transitionsQ1.put("i", new String[]{"q1", "i", "L"});
        transitionsQ1.put("#", new String[]{"halt", "_", "-"});
        this.rules.put("q1", transitionsQ1);

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
        String[] newData = new String[input.length() + 1];

        String[] inputData = input.split("");       // Tách chuỗi thành mảng

        int currentPosition = 0;        // Con trỏ index tương ứng của trạng thái
        int indexNewData = 1;
        String currentState = "q0";

        while (!currentState.equals("halt")) {
            String[] nextResult;
            if (!inputData[currentPosition].equals("#")) {
                nextResult = rules.get(currentState).get("i");
            } else {
                nextResult = rules.get(currentState).get("#");
            }

            currentState = nextResult[0];
            newData[indexNewData] = inputData[currentPosition];
            if (nextResult[2].equals("R")) {
                currentPosition++;
                indexNewData++;
            }

            // Dịch chuyển con trỏ currentPosition
            else if (nextResult[2].equals("L")) {
                currentPosition--;
                indexNewData--;

                if (currentPosition == -1) {
                    newData[indexNewData] = "_";
                    break;
                }
            }
        }

        return Arrays.copyOfRange(newData, 0, newData.length - 1);
    }

    public static void main(String[] args) {
        TuringM6 turingM6 = new TuringM6("XinChao");
        System.out.println("Máy Turing M6:");
        System.out.println("K = " + turingM6.states);
        System.out.println("Sigma = " + turingM6.alphabet);
        System.out.println("Tập luật:");
        turingM6.printRules();
    }
}
