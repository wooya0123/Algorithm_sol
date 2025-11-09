package boj.p1978;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int cnt = 0;

        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());

            if (num == 1) {
                continue;
            }

            boolean isPrime = true;
            for (int j = 2; j < num; j++) {
                if (num % j == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime) {
                cnt++;
            }
        }
        System.out.print(cnt);
    }
}
