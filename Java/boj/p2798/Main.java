package boj.p2798;

import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[] cards;
    static int[] result = new int[3];
    static int maxSum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        cards = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }

        combination(0, 0);

        System.out.println(maxSum);
    }

    // 조합 찾기
    public static void combination(int start, int depth) {
        if (depth == 3) {
            int sum = 0;
            for (int val : result) {
                sum += val;
            }

            if (sum <= M && sum > maxSum) {
                maxSum = sum;
            }
            return;
        }

        for (int i = start; i < N; i++) {
            result[depth] = cards[i];
            combination(i + 1, depth + 1);
        }
    }
}
