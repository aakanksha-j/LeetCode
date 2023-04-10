import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> hashmap = new HashMap<Character, Character>() {{
            put('{', '}');
            put('(', ')');
            put('[', ']');
        }};
        Stack<Character> st = new Stack<>();
        for (char bracket: s.toCharArray()) {
            if (hashmap.containsKey(bracket)){
                st.push(bracket);
            } else {
                if (st.empty() || hashmap.get(st.pop()) != bracket) {
                    return false;
                }
            }
        }
        return st.empty();
    }
}