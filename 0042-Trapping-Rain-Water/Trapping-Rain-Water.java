class Solution {
    public int trap(int[] height) {
        int l = 0;
        int r = height.length - 1;
        int lMax = 0;
        int rMax = 0;
        int ans = 0;
        while (l < r) {
            int water = 0;
            if (height[r] > height[l]) {
                lMax = Math.max(lMax, height[l]);
                water = lMax - height[l];
                l++;
            } else {
                rMax = Math.max(rMax, height[r]);
                water = rMax - height[r];
                r--;
            }
            ans += water;
        }
        return ans;
    }
}