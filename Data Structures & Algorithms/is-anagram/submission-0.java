class Solution {
    public boolean isAnagram(String s, String t) {
        int l = s.length();
        if (l != t.length()) return false;
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0; i < l; i++) {
            char ch = s.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        for (int i = 0; i < l; i++) {
            char ch = t.charAt(i);
            if (!map.containsKey(ch) || map.get(ch) == 0) {
                return false;
            }
            map.put(ch, map.get(ch) - 1);
        }
        return true;
    }
}
