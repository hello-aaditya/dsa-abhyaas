---
problem: First negative in every window of size k
link: https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
status: DONE
approach: Sliding Window
level: MODERATE
prerequisite: https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
video: https://www.youtube.com/watch?v=uUXXEgK2Jh8&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=4
---

# Solution
```java
class Solution {
    static List<Integer> firstNegInt(int arr[], int k) {
        // write code here
        int size = arr.length;
        ArrayList<Integer> negativeList = new ArrayList<>();
        ArrayList<Integer> firstNegative = new ArrayList<>();
        
        int start = 0;
        int end = 0;
        
        while (end < size) {
            // IF arr[end] IS A NEGATIVE NUMBER THEN ADD IT INSIDE negativeList
            if (arr[end] < 0) {
                negativeList.add(arr[end]);
            }
            // CALCULATE windowSize
            int windowSize = (end - start) + 1;
            
            // IF windowSize < k THEN WE HAVE TO INCREASE THE WINDOW FROM THE END
            if (windowSize < k) {
                end++;
            } else if (windowSize == k) { // CONDITION: windowSize == k
                // CHECK negativeList IS EMPTY, IF YES THEN ADD 0 to firstNegative
                if (negativeList.isEmpty()) {
                    firstNegative.add(0);
                }
                // CHECK negativeList IS NOT EMPTY, THEN ADD negativeList[0] to firstNegative
                else {
                    firstNegative.add(negativeList.get(0));
                }
                
                // SLIDE THE WINDOW
                // BEFORE REMOVING arr[start] FROM THE WINDOW, CHECK WHETHER arr[start] PRESENT IN negativeList[0]
                // IF YES THEN, DELETE IT FROM THE BOTH PLACES
                if ((!negativeList.isEmpty()) && (arr[start] == negativeList.get(0))) {
                    negativeList.remove(0);
                }
                // AND FINALLY SLIDE THE WINDOW
                start++;
                end++;
                
            }
            
        }
        return firstNegative;
    }
}
```
