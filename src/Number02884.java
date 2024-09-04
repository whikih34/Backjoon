import java.util.Scanner;

public class Number02884 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int hour1 = sc.nextInt();
    int min1 = sc.nextInt();

    // 시간의 범위를 벗어난 경우 -1을 출력하도록 함
    int hour2 = -1;
    int min2 = -1;

    if ((hour1 >= 0 && hour1 <= 23) && (min1 >= 0 && min1 <= 59)) {
      if (min1 >= 45) {
        hour2 = hour1;
        min2 = min1 - 45;
      } else {
        if (hour1 == 0) {
          hour2 = 23;
        } else {
          hour2 = hour1 - 1;
        }

        min2 = 60 - (45 - min1);
      }
    }

    System.out.println(hour2 + " " + min2);
  }
}