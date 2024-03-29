class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        Arrays.sort(nums);
        
        for(int num : nums) {
            if(!set.contains(num)) set.add(num);
            else return true;
        }
        
        return false;
    }
}