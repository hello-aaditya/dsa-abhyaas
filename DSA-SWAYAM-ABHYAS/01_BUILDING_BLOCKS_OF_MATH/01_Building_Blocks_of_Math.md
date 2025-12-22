## 1. Leap Year Program

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

## 2. Vowel or Consonant

### Problem Statement
You need to develop a simple Java application to check if a given character is a vowel or a consonant.

---
### Explanation
Vowels in the English alphabet are:
- Lowercase: `a`, `e`, `i`, `o`, `u`
- Uppercase: `A`, `E`, `I`, `O`, `U`

All other alphabet characters are consonants.  
Any non-alphabet character is considered invalid.

---
### Task: Check if a Given Character is a Vowel or a Consonant
- Use `Scanner` to take user input for the character.
- Use conditional statements to check if the character is a vowel or a consonant.
    
- Print a message indicating whether the character is a vowel, a consonant, or not a valid alphabet character.
    

---

### Expected Output

**Input:**

```
a
```

**Output:**

```
a is a vowel.
```

**Input:**

```
B
```

**Output:**

```
B is a consonant.
```

**Input:**

```
1
```

**Output:**

```
1 is not a valid alphabet character.
```

---

### Sample Input

```
a
```

### Sample Output

```
a is a vowel.
```

---

### Solution
```java
package a01_Building_Blocks_of_Math;

import java.util.Scanner;

public class VowelConsonant {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		// Ask user to input a Character
		System.out.println("ENTER A CHARACTER: ");
		char userInput = input.next().charAt(0);

		if ((userInput >= 'a' && userInput <= 'z') || (userInput >= 'A' && userInput <= 'Z')) {
			if (isVowel(userInput) == true) {
				System.out.println(userInput + " is a vowel.");
			} else {
				System.out.println(userInput + " is a consonant.");
			}
		} else {
			System.out.println(userInput + " is not a valid alphabet character.");
		}

		input.close();
	}

	// Check if the Character is a vowel or a consonant
	public static boolean isVowel(char ch) {
		switch (ch) {
		case 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U':
			return true;
		default:
			return false;
		}
	}
}
```
## 3. N Even Numbers

### Problem Statement

You need to develop a simple Java application to print the first **n even numbers**.

---

### Task: Print the First N Even Numbers

- Use `Scanner` to take user input for the value of `n`.
    
- Use a `for` loop to iterate from `1` to `n`.
    
- In each iteration, calculate the even number by multiplying the loop counter by `2`.
    
- Print the calculated even number.
    

---

### Expected Output

**Input:**

```
n = 5
```

**Output:**

```
The first 5 even numbers are:
2
4
6
8
10
```

**Input:**

```
n = 3
```

**Output:**

```
The first 3 even numbers are:
2
4
6
```

---

### Sample Input

```
7
```

### Sample Output

```
The first 7 even numbers are:
2
4
6
8
10
12
14
```

---

### Solution
```java
```