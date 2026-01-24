---
problem: 74. Search a 2D Matrix
link: https://leetcode.com/problems/search-a-2d-matrix/description/
status: DONE
approach: Binary Search
level: MODERATE
prerequisite: 
video: 
---

# Solution
```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rowSize = matrix.length;
        int colSize = matrix[0].length;

        int start = 0;
        int end = (rowSize * colSize) - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            int row = mid / colSize;
            int col = mid % colSize;

            if (matrix[row][col] == target)  {
                return true;
            } else if (matrix[row][col] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return false;
    }
}
```
![74_Search_a_2D_Matrix_pic1](./images/74_Search_a_2D_Matrix_pic1.jpg)

![74_Search_a_2D_Matrix_pic2](./images/74_Search_a_2D_Matrix_pic2.jpg)