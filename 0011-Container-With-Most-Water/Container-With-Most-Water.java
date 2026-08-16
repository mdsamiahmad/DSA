class Solution {
    public int maxArea(int[] height) {
        int l=0;
        int r=height.length-1;
        int ans = Integer.MIN_VALUE;
        while(l<r){
            int area=(r-l)*Math.min(height[r],height[l]);
            ans=Math.max(ans,area);
            if(height[r]>height[l]) l++;
            else r--;
        }
        return ans;
    }
}