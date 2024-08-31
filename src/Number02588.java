import java.util.Scanner;

public class Number02588 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int num1 = sc.nextInt();
    int num2 = sc.nextInt();

    int num2Unit = num2 % 10;  // num2의 일의 자리
    int num2Tens = (num2 % 100) / 10;  // num2의 십의 자리
    int num2Hund = num2 / 100;  // num2의 백의 자리

    System.out.println(num1 * num2Unit);
    System.out.println(num1 * num2Tens);
    System.out.println(num1 * num2Hund);
    System.out.println(num1 * num2);
  }
}