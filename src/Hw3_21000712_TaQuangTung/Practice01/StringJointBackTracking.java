package Hw3_21000712_TaQuangTung.Practice01;

public class StringJointBackTracking {
    public static void main(String[] args) {
        String text = "ababaaaa";
        String pattern = "ab";
        showIndexStringFounder(text, pattern, 0, 0);
    }


    public static void showIndexStringFounder(String text, String patternFound, int textIndex, int patternIndex) {
        // Điều kiện dừng: khi textIndex lớn hơn hoặc bằng độ dài của text
        if (textIndex >= text.length()) {
            return;
        }

        // Trường hợp khớp: Kiểm tra các kỹ tự trong patternFound đã khớp với text chưa
        if (patternIndex == patternFound.length()) {
            System.out.println("Xâu mẫu P xuất hiện ở vị trí " + (textIndex - patternIndex) + " trong văn bản T");

            // Duyệt tiếp cả văn bản T
            if (textIndex < text.length()) {
                showIndexStringFounder(text, patternFound, textIndex, 0);
            }
            return;
        }

        // Trường hợp không khớp: Nếu duyệt hết văn bản mà không có ký tự khớp
        if (textIndex == text.length() || text.charAt(textIndex) != patternFound.charAt(patternIndex)) {
            // Nếu có ít nhất một ký tự đã được so khớp, quay lui
            if (patternIndex > 0) {
                showIndexStringFounder(text, patternFound, textIndex - patternIndex + 1, 0);
            } else {
                // Nếu chưa có ký tự nào khớp, tiếp tục với vị trí tiếp theo trong văn bản
                showIndexStringFounder(text, patternFound, textIndex + 1, 0);
            }
            return;
        }


        // Nếu ký tự hiện tại của patternFound đang khớp thì tiếp tục thuật toán
        showIndexStringFounder(text, patternFound, textIndex + 1, patternIndex + 1);
    }
}

/*
ababaaaa
ab (2)
0 0
1 1
2 2
=> index = 2 - 2 = 0

2 0
3 1
4 2
=> tương tự


aaabaaaa
a
0 0
1 1
=> index = 0

1 0
2 1
=> index = 1


aaabaaaa
ab
0 0
1 1
1 0
2 1
3 2
2 0
...
=> tương tự

 */