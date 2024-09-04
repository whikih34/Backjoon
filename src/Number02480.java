import java.util.Scanner;

public class Number02480 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int[] dices = new int[3];
    int max = 0;
    int prize = 0;

    for (int i = 0; i < dices.length; i++) {
      int num = sc.nextInt();
      if (num >= 1 && num <= 6) {
        dices[i] = num;
      } else {
        System.out.println("잘못된 숫자 입력");
        return;  // 프로그램 종료 (return 0(exit code) 와 같은 표현)
      }

      if (dices[i] > max) {
        max = dices[i];
      }
    }

    if (dices[0] == dices[1]) {
      if (dices[1] == dices[2]) {
        prize = 10000 + dices[0] * 1000;
      } else {
        prize = 1000 + dices[0] * 100;
      }
    } else {
      if (dices[1] == dices[2]) {
        prize = 1000 + dices[1] * 100;
      } else {
        if (dices[2] == dices[0]) {
          prize = 1000 + dices[2] * 100;
        } else {
          prize = max * 100;
        }
      }
    }

    System.out.println(prize);

  }
}