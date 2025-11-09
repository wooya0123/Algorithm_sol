package boj.p1546;

import java.util.*;
import java.io.*;

public class Main {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        double[] scores = new double[N];
        for (int i = 0; i < N; i++) {
            scores[i] = Integer.parseInt(st.nextToken());
        }

        double maxScore = Arrays.stream(scores).max().getAsDouble();

        for (int i = 0; i < N; i++) {
            scores[i] = scores[i] / maxScore * 100;
        }

        double meanScore = Arrays.stream(scores).average().getAsDouble();

        System.out.println(meanScore);
    }
}
