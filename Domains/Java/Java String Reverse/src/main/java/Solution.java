import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();

        int length = A.length();
        for (int i = 0; i < A.length(); i++) {
            if (A.charAt(i) != A.charAt(length - i - 1)) {
                System.out.println("No");
                return;
            }
        }

        System.out.println("Yes");
    }
}
