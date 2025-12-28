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
package a01_Building_Blocks_of_Math;

import java.util.Scanner;
public class PrintNEven {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		// Ask user for Input
		System.out.print("ENTER A NUMBER: ");
		int number = input.nextInt();
		
		int firstEven = 2;
		
		System.out.println("THE FIRST " + number + " EVEN NUMBER ARE: : ");
		for(int i=1; i<=number; i++) {
			System.out.println(firstEven);
			firstEven += 2;
		}
		input.close();
	}

}
```
## 4. Temperature Predictor

### Problem Statement

You need to develop a simple Java application to assign a category to a given temperature.

---

### Temperature Categories

- `< 0` : Freezing
    
- `0 – 15` : Cold
    
- `16 – 25` : Moderate
    
- `26 – 35` : Warm
    
- `> 35` : Hot
    

---

### Task: Assign a Category to a Given Temperature

- Use `Scanner` to take user input for the temperature.
    
- Use conditional statements to check the temperature range.
    
- Print the category corresponding to the temperature.
    

---

### Expected Output

**Input:**

```
-5
```

**Output:**

```
The temperature -5 is categorized as Freezing.
```

**Input:**

```
10
```

**Output:**

```
The temperature 10 is categorized as Cold.
```

---

### Sample Input

```
-5
```

### Sample Output

```
The temperature -5 is categorized as Freezing.
```

---

### Solution
```java
package a01_Building_Blocks_of_Math;

import java.util.Scanner;

public class TemperaturePredictor {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		// Ask user for Input 
		System.out.print("ENTER TEMPERATURE: ");
		int temp = input.nextInt();
		
		if(temp < 0) {
			System.out.println("THE TEMPERATURE " + temp + " IS CATEGORIZED AS FREEZING.");
		} else if(temp >= 0 && temp <= 15) {
			System.out.println("THE TEMPERATURE " + temp + " IS CATEGORIZED AS Cold.");
		}  else if(temp >= 16 && temp <= 25) {
			System.out.println("THE TEMPERATURE " + temp + " IS CATEGORIZED AS MODERATE.");
		} else if(temp >= 26 && temp <= 35) {
			System.out.println("THE TEMPERATURE " + temp + " IS CATEGORIZED AS WARM.");
		} else if(temp > 35){
			System.out.println("THE TEMPERATURE " + temp + " IS CATEGORIZED AS HOT.");
		}
		
		input.close();
	}

}
```
## 5. Senior Citizen Discount

### Problem Statement

You need to develop a simple Java application to check if a person is eligible for a senior citizen discount based on their age (assume **60 years** for eligibility).

---

### Task: Check Eligibility for a Senior Citizen Discount

- Use `Scanner` to take user input for the person's age.
    
- Use an `if-else` statement to check if the age is **60 or more**.
    
- Print a message indicating whether the person is eligible for a senior citizen discount.
    

---

### Expected Output

**Input:**

```
65
```

**Output:**

```
You are eligible for a senior citizen discount.
```

**Input:**

```
45
```

**Output:**

```
You are not eligible for a senior citizen discount.
```

---

### Sample Input

```
65
```

### Sample Output

```
You are eligible for a senior citizen discount.
```

---

### Solution
```java
package a01_Building_Blocks_of_Math;

import java.util.Scanner;
public class SeniorCitizenDiscount {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		// Ask user for Input
		System.out.println("ENTER YOUR AGE: ");
		int age = input.nextInt();
		
		System.out.println((age>=60) ? "You are eligible for a senior citizen discount." : "You are not eligible for a senior citizen discount.");
		
		
		input.close();
	}

}
```
## 6. Digit Counter

### Problem Statement

You need to develop a simple Java application to count the number of digits in a given number.

---

### Task: Count the Number of Digits in a Given Number

- Use `Scanner` to take user input for the number.
    
- Initialize a counter variable to `0`.
    
- Use a `while` loop to repeatedly divide the number by `10` until it becomes `0`.
    
- Increment the counter variable in each iteration of the loop.
    
- Print the counter variable, which represents the number of digits in the number.
    

---

### Expected Output

**Input:**

```
12345
```

**Output:**

```
The number 12345 has 5 digits.
```

**Input:**

```
6789
```

**Output:**

```
The number 6789 has 4 digits.
```

---

### Sample Input

```
11
```

### Sample Output

```
The number 11 has 2 digits.
```

---

### Solution
```java
package a01_Building_Blocks_of_Math;

import java.util.Scanner;

public class DigitCounter {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		// Ask user for Input
		System.out.println("ENTER A NUMBER: ");
		int number = input.nextInt();
		
		int temp = number;

		int digitCount = 0;
		while(temp > 0) {
			temp /= 10;
			digitCount++;
		}
		
		System.out.println("THE NUMBER " + number + " has " + digitCount + " digits.");
		

		input.close();
	}

}
```
## 7. Armstrong Number

### Problem Statement

You need to develop a simple Java application to check if a given number is an Armstrong number.

---

### Explanation

An **Armstrong number** (also known as a narcissistic number, pluperfect number, or pluperfect digital invariant) is a number that is equal to the sum of its own digits, each raised to the power of the number of digits.

**Example:**

- `153` is an Armstrong number because  
    `1³ + 5³ + 3³ = 153`
    

---

### Task: Check if a Given Number is an Armstrong Number

- Use `Scanner` to take user input for the number.
    
- Calculate the number of digits in the number.
    
- Extract each digit of the number and raise it to the power of the number of digits.
    
- Sum these values.
    
- If the sum is equal to the original number, print that it is an Armstrong number.
    
- Otherwise, print that it is not an Armstrong number.
    

---

### Expected Output

**Input:**

```
153
```

**Output:**

```
153 is an Armstrong number.
```

**Input:**

```
123
```

**Output:**

```
123 is not an Armstrong number.
```

---

### Sample Input

```
2222
```

### Sample Output

```
2222 is not an Armstrong number.
```

---

### Solution
```java
package a01_Building_Blocks_of_Math;

import java.util.Scanner;
public class ArmstrongNumber {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		// Ask user for Input
		System.out.print("ENTER A NUMBER: ");
		int number = input.nextInt();
		
		int totalDigits = digitCount(number); 
		
		int temp = number;
		int armstrong = 0;
		
		while(temp != 0) {
			int lastDigit = temp % 10;
			
			armstrong += (Math.pow(lastDigit, totalDigits));
			
			temp /= 10;
		}
		
		if(armstrong == number) {
			System.out.println(number + " IS AN ARMSTRONG NUMBER.");
		} else {
			System.out.println(number + " IS NOT AN ARMSTRONG NUMBER.");
		}
		
		input.close();
	}
	public static int digitCount(int number) {
		int totalDigits = 0;
		
		while(number != 0 ) {
			number /= 10;
			totalDigits++;
		}
		
		return totalDigits;
	}

}
```
## 8. Decimal to Binary

### Problem Statement

You need to develop a simple Java application to convert a decimal number to its binary equivalent.

---

### Explanation

A decimal number can be converted to binary by repeatedly dividing the number by `2` and recording the remainders.  
The binary equivalent is obtained by reading the sequence of remainders **from bottom to top**.

---

### Task: Convert a Given Decimal Number to Binary

- Use `Scanner` to take user input for the decimal number.
    
- Use a loop to repeatedly divide the number by `2` and store the remainders.
    
- Print the binary equivalent of the given decimal number.
    

---

### Expected Output

**Input:**

```
10
```

**Output:**

```
The binary equivalent of 10 is 1010.
```

**Input:**

```
15
```

**Output:**

```
The binary equivalent of 15 is 1111.
```

**Input:**

```
23
```

**Output:**

```
The binary equivalent of 23 is 10111.
```

---

### Sample Input

```
10
```

### Sample Output

```
The binary equivalent of 10 is 1010.
```

---

### Solution
```java
package a01_Building_Blocks_of_Math;

import java.util.Scanner;
public class DecimalToBinary {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		// Ask User for Input 
		System.out.print("ENTER A DECIMAL NUMBER: ");
		int decimalNumber = input.nextInt();
		
		String binaryNumber = binaryConversion(decimalNumber);
		
		System.out.println("THE BINARY EQUIVALENT OF " + decimalNumber + " is " + binaryNumber + ".");
	}
	
	public static String binaryConversion(int number) {
		String binaryNumber = "";
		
		while(number != 0) {
			int remainder = number % 2;
			binaryNumber =  remainder + binaryNumber;
			
			number = number / 2;
		}
		return binaryNumber;
		
	}

}
```
## 9. Fibonacci Series

### Problem Statement

You need to develop a simple Java application to print the Fibonacci series up to a given number.

---

### Fibonacci Series Explanation

The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with `0` and `1`.

**Example:**  
Fibonacci series up to `10`:

```
0, 1, 1, 2, 3, 5, 8
```

---

### Task: Print the Fibonacci Series Up to a Given Number

- Use `Scanner` to take user input for the maximum number.
    
- Use a loop to generate the Fibonacci series.
    
- Print each number in the series until the series reaches or exceeds the given number.
    

---

### Expected Output

**Input:**

```
10
```

**Output:**

```
Fibonacci series up to 10: 0 1 1 2 3 5 8
```

**Input:**

```
21
```

**Output:**

```
Fibonacci series up to 21: 0 1 1 2 3 5 8 13 21
```

---

### Sample Input

```
0
```

### Sample Output

```
Fibonacci series up to 0:
0
```

---

### Solution
```java
package array;



import java.util.Scanner;
public class FibonacciSeriesTillN {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("ENTER THE MAXIMUM NUMBER: ");
		int maxNumber = input.nextInt();
		
		// Print the Fibonacci Series up to the given Number
		System.out.print("FIBONACCI SERIES UP TO " + maxNumber + ": ");
		int firstNumber = 0;
		int secondNumber = 1;
		int nextNumber = firstNumber + secondNumber;
		
		System.out.print(firstNumber + " ");
		while(nextNumber <= maxNumber) {			
			System.out.print(nextNumber + " ");
			
			nextNumber = firstNumber + secondNumber;
			firstNumber = secondNumber;
			secondNumber = nextNumber;
		}
		input.close();
	}
}
```
## 10. Palindrome Checker

### Problem Statement

You need to develop a simple Java application to check if a given number is a palindrome.

---

### Explanation

A **palindrome** is a number that remains the same when its digits are reversed.

**Examples:**  
`121`, `1331`, `12321`

---

### Task: Check if a Given Number is a Palindrome

- Use `Scanner` to take user input for the number.
    
- Reverse the given number.
    
- Compare the reversed number with the original number.
    
- Print a message indicating whether the number is a palindrome.
    

---

### Expected Output

**Input:**

```
121
```

**Output:**

```
121 is a palindrome.
```

**Input:**

```
123
```

**Output:**

```
123 is not a palindrome.
```

---

### Sample Input

```
121
```

### Sample Output

```
121 is a palindrome.
```

---

### Solution
```java
package array;

// Check if a given Number is a Palindrome

import java.util.Scanner;
public class PalindromeChecker {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("ENTER A NUMBER: ");
		int number = input.nextInt();
		
		int reversedNumber = reverse(number); 
		
		if(reversedNumber == number) {
			System.out.println(number + " is a palindrome.");
		} else {
			System.out.println(number + " is not a palindrome.");
		}
		
		input.close();
	}
	public static int reverse(int number) {
		int reverseNumber = 0;
		
		while(number != 0) {
			int lastDigit = number % 10;
			
			reverseNumber = (reverseNumber * 10) + lastDigit;
			
			number /= 10;
		}
		
		return reverseNumber;
	}

}
```