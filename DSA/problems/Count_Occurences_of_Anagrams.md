---
problem: Count Occurences of Anagrams
link: https://www.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1
status: DONE
approach: Sliding Window
level: MODERATE
prerequisite: 
video: https://www.youtube.com/watch?v=MW4lJ8Y0xXk&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=5
---

# Solution
```java
class Solution {

    int search(String pat, String txt) {
        // code here
        
        // CREATE A HASHMAP TO STORE ALL CHAR OF PAT
        HashMap<Character, Integer> map = new HashMap<>();
        
        for (char ch : pat.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        
        int size = txt.length();
        int k = pat.length(); // WINDOW-SIZE OF pat
        int start = 0;
        int distinctChar = map.size();
        int count = 0;
        
        for (int end=0; end<size; end++) {
            int windowSize = end - start + 1;
            char currentChar = txt.charAt(end);
            
            // IF currentChar FOUND INSIDE map THEN REDUCE ITS COUNT BY 1
            if (map.containsKey(currentChar)) {
                map.put(currentChar, map.get(currentChar) - 1);
                
                // IF THE VALUE OF currentChar INSIDE map GETS 0 -> distinctChar--
                if (map.get(currentChar) == 0) {
                    distinctChar--;
                }
                
                // IF distinctChar BECOMES ZERO THAT MEANS ALL CHARACTERS INSIDE pat
                // FOUND INSIDE txt -> count++;
                if (distinctChar == 0) {
                    count++;
                }
            }
            
            // IF WE HIT THE windowSize
            if (windowSize == k) {
                // CHECK CHARACTER AT start of txt IS PRESENT INSIDE THE map
                // THeN BEFORE SLIDE THE WINDOW WE MUST INCREASE ITS COUNT
                char startChar = txt.charAt(start);
                if (map.containsKey(startChar)) {
                    // CHECK IF THE VALUE startChar IS ZERO THEN
                    // WE MUST INCREASE distinctChar value
                    if (map.get(startChar) == 0) {
                        distinctChar++;
                    }
                    map.put(startChar, map.getOrDefault(startChar, 0) + 1);
                }
                start++;
            }
        }
        return count;
    }
}
```
![Count Occurences of AnagramsPic1.jpg](./images/Count_Occurences_of_AnagramsPic1.jpg)