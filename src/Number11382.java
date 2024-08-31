import java.util.Scanner;

public class Number11382 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    // 최댓값이 10의 12승이므로 long타입으로 입력을 받는다
    long num1 = sc.nextLong();
    long num2 = sc.nextLong();
    long num3 = sc.nextLong();

    System.out.println(num1 + num2 + num3);
  }
}