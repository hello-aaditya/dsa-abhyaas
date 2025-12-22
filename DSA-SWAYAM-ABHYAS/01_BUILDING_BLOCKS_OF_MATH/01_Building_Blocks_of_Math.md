## Leap Year Program

### Problem Statement
You need to develop a simple Java application to check if a given year is a leap year.

---
### Leap Year Explanation
A leap year is a year that:
- Is evenly divisible by **4**,
- **Except** years that are evenly divisible by **100**.
- However, years that are evenly divisible by **400** are leap years.
**Examples:**
- Leap years: `2000`, `2400`
- Not leap years: `1800`, `1900`, `2100`, `2200`, `2300`, `2500`
---
### Task: Check if a Given Year is a Leap Year
- Use `Scanner` to take user input for the year.
- Use conditional statements to check if the year is a leap year.
- Print a message indicating whether the year is a leap year.
---
### Expected Output
**Input:**
```
2000
```
**Output:**
```
2000 is a leap year.
```
**Input:**
```
1900
```
**Output:**
```
1900 is not a leap year.
```
---
### Sample Input
```
2024
```
### Sample Output
```
2024 is a leap year.
```
## Solution
```java
package a01_Building_Blocks_of_Math;

import java.util.Scanner;

public class LeapYear {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		// Ask User to Enter a Year
		System.out.print("ENTER A YEAR: ");
		int year = input.nextInt();
		
		// Check if the Year is a Leap Year
		if(isLeapYear(year) == true) {
			System.out.println(year + " is a leap year.");
		} else {
			System.out.println(year + " is not a leap year.");
		}
		
		input.close();
	}
	public static boolean isLeapYear(int year) {
		
		// If Year is a Century Year
		if(year % 100 == 0) {
			// Check Year: Dividing by 400 
			if(year % 400 == 0) {
				return true;
			}
			return false;
		} else {
			if(year % 4 == 0) {
				return true;
			}
		}
		return false;
	}

}
```

