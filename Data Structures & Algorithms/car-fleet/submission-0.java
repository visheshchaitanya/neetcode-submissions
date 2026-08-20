class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;

        int[][] cars = new int[n][2];

        for (int i = 0 ; i < n ; i++) {
            cars[i][0] = position[i];
            cars[i][1] = speed[i];
        }

        Arrays.sort(cars, (a, b) -> a[0] - b[0]);
        Stack<Double> st = new Stack<>();

        for (int i = 0 ; i < n ; i++) {
            double arr_time = (target - cars[i][0]) / (double) cars[i][1] ; 
            while (!st.isEmpty() && st.peek() <= arr_time) {
                st.pop() ; 
            }

            st.push(arr_time);
        }

        return st.size();
    }
}
