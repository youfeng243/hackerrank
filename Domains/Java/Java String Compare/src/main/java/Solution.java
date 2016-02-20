import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {

        int k = 0;
        String text = "";
        String Max = "";
        String Min = "";

        Scanner sa = new Scanner(System.in);
        text = sa.nextLine();
        k = sa.nextInt();

        for( int i = 0; i < k; i++ ){
            Max += "A";
            Min += "z";
        }

        for( int i = 0; i <= text.length() - k; i++ ){
            String temp = text.substring(i, k + i );
            Max = Max.compareTo(temp) < 0 ? temp : Max;
            Min = Min.compareTo(temp) > 0 ? temp : Min;
        }

        System.out.println(Min);
        System.out.println(Max);
    }
}