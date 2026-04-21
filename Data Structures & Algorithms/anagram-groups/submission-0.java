class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<String, List<String>>();
        int str_len = strs.length;

        for (int i = 0; i < str_len; i++) {
            char[] charArr = strs[i].toCharArray();
            Arrays.sort(charArr);
            String sortedString = new String(charArr);

            map.putIfAbsent(sortedString, new ArrayList<>());
            map.get(sortedString).add(strs[i]);
        }
        return new ArrayList<List<String>>(map.values());
    }
}
