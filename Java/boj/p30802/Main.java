package boj.p30802;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        int[] tSize = new int[6];
        for (int i = 0; i < 6; i++) {
            tSize[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int T =  Integer.parseInt(st.nextToken());
        int P =  Integer.parseInt(st.nextToken());

        int tBundle = 0;

        for (int t : tSize) {
            if (t % T > 0) {
                tBundle += t / T + 1;
            } else {
                tBundle += t / T;
            }
        }

        int pBundle = N / P;
        int p = N % P;

        sb.append(tBundle);
        sb.append('\n');
        sb.append(pBundle);
        sb.append(' ');
        sb.append(p);

        System.out.println(sb);
    }
}
