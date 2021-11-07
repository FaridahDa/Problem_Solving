//Your task is to make two functions, max and min (maximum and minimum in PHP and Python, maxi and mini in Julia) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vect

import java.util.Arrays;
public class Kata {

  public int min(int[] list) {
    Arrays.sort(list);
    return list[0];
  }

  public int max(int[] list) {
    Arrays.sort(list);
    return list[list.length-1];
  }
}