import java.util.Scanner;

public class Number02525 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int startHour = sc.nextInt();
    int startMin = sc.nextInt();
    int cookTime = sc.nextInt();

    int endHour = -1;
    int endMin = -1;

    if ((startHour >= 0 && startHour <= 23) && (startMin >= 0 && startMin <= 59)) {
      if (startMin + cookTime < 60) {
        endMin = startMin + cookTime;
        endHour = startHour;
      } else {
        endHour = ((startMin + cookTime) / 60) + startHour;
        endMin = (startMin + cookTime) % 60;

        if (endHour > 23) {
          endHour %= 24;
        }
      }
      System.out.println(endHour + " " + endMin);
    } else {
      System.out.println("잘못된 시간을 입력하셨습니다");
    }

  }
}