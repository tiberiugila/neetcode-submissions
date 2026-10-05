class Solution {
    public boolean hasDuplicate(int[] nums) {

        Map<Integer, List<Integer>> positions = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            positions.computeIfAbsent(nums[i], k-> new ArrayList<>()).add(i);
        }

        for (List<Integer> list: positions.values()){
            if (list.size() > 1) {
                return true;
            }
        }
        return false;
    }
}