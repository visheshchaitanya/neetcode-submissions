class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        int a = -1, b = -1, c = -1;
        int n = triplets.length;

        for (int i = 0; i < n ; i++) {
            int curr_a = triplets[i][0];
            int curr_b = triplets[i][1];
            int curr_c = triplets[i][2];

            if (curr_a <= target[0] && curr_b <= target[1] && curr_c <= target[2]) {
                if (curr_a == target[0] && curr_b == target[1] && curr_c == target[2]) {
                    return true;
                } else {
                    a = Math.max(a, curr_a); 
                    b = Math.max(b, curr_b);
                    c = Math.max(c, curr_c);
                }
            }
        }

        return a == target[0] && b == target[1] && c == target[2];
    }
}
