import java.util.Scanner;

public class Number02739 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int dan = sc.nextInt();

    if (dan >= 1 && dan <= 9) {
      for (int i = 1; i <= 9; i++) {
        System.out.println(dan + " * " + i + " = " + dan*i);
      }
    } else {
      System.out.println("잘못된 숫자를 입력하셨습니다. (1~9 중의 숫자를 입력하세요)");
    }

  }
}