package boj.p4153;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        while (true) {
            String line = br.readLine();
            if (line == null) break;

            st = new StringTokenizer(line);

            int[] arr = new int[3];
            for (int i = 0; i < 3; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            if (arr[0] == 0 && arr[1] == 0 && arr[2] == 0) {
                break;
            }

            Arrays.sort(arr);
            if (Math.pow(arr[0], 2) +  Math.pow(arr[1], 2) == Math.pow(arr[2], 2)) {
                sb.append("right");
                sb.append("\n");
            } else {
                sb.append("wrong");
                sb.append("\n");
            }
        }

        System.out.println(sb);

    }
}
