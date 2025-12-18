# Question-1:
## Question: Swap Two Variables Using a Temporary Variable (Cash Register Scenario)

Imagine you are working as a cashier, and you discover that the cash amounts in two registers have been mistakenly swapped. Your task is to correct this by swapping the values of the two registers using a **temporary variable**.

### Problem Statement

You are given the cash counts of two registers:
- Register A has `x = 5`
- Register B has `y = 10`

### Tasks to Perform

1. **Initialize Two Variables**
   - Store the cash count of Register A in variable `x`.
   - Store the cash count of Register B in variable `y`.

2. **Swap the Values**
   - Use a temporary variable to swap the values of `x` and `y` without losing any data.

3. **Display the Results**
   - Display the values of both registers **before** swapping.
   - Display the values of both registers **after** swapping to verify the correction.

### Expected Output

#### Sample Output
Before swap:  
Register A: 5  
Register B: 10

After swap:  
Register A: 10  
Register B: 5
## Solution
```java
import java.util.Scanner;
public class SwapTwoVariableUsingTemp {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int number1 = input.nextInt();
		int number2 = input.nextInt();
		
		System.out.println("Before Swap: ");
		System.out.println("Register A: " + number1);
		System.out.println("Regsiter B: " + number2);
		
		int temp = number2;
		number2 = number1;
		number1 = temp;
		
		System.out.println("After Swap: ");
		System.out.println("Register A: " + number1);
		System.out.println("Regsiter B: " + number2);
		input.close();
	}

}
```
# Question-2:
## Question: Swap Two Variables Without Using a Temporary Variable (Cash Register Scenario)

Imagine you are working as a cashier and you realize that the cash amounts recorded for two registers are reversed. To fix this issue **without using any extra memory**, you must swap the values of the two registers **without using a temporary variable**.

### Problem Statement

You are given the cash counts of two registers:
- Register A has `x = 5`
- Register B has `y = 10`

### Tasks to Perform

1. **Initialize Two Variables**
   - Variable `x` represents the cash count of Register A.
   - Variable `y` represents the cash count of Register B.

2. **Swap the Values Without a Temporary Variable**
   - Swap the values of `x` and `y` using **arithmetic operations (addition and subtraction)**.
   - Ensure that no extra variable is used during the swapping process.

3. **Display the Results**
   - Display the values of both registers **before** swapping.
   - Display the values of both registers **after** swapping to confirm that the values are corrected.

### Expected Output

#### Sample Output
Before swap:  
Register A: 5  
Register B: 10

After swap:  
Register A: 10  
Register B: 5
## Solution
```java
package basics;

import java.util.Scanner;
public class SwapTwoVariableWithoutUsingTemp {

	public static void main(String[] args) {
Scanner input = new Scanner(System.in);
		
		int number1 = input.nextInt();
		int number2 = input.nextInt();
		
		System.out.println("Before Swap: ");
		System.out.println("Register A: " + number1);
		System.out.println("Regsiter B: " + number2);
		
		number1 = number1+number2;
		number2 = number1-number2;
		number1 = number1-number2;
		
		System.out.println("After Swap: ");
		System.out.println("Register A: " + number1);
		System.out.println("Regsiter B: " + number2);
		
		input.close();
	}

}
```
# Question-3
## Question: Calculate the Area of a Circle (Park Design Scenario)

Imagine you are an urban planner designing a circular park. To estimate how much space the park’s central fountain will occupy, you need to calculate the **area of a circle** based on its radius.

### Problem Statement

You are given the radius of a circular fountain, and your task is to calculate its area using the mathematical formula for the area of a circle.

### Tasks to Perform

1. **Declare and Initialize the Radius**
   - Declare a variable named `radius`.
   - Initialize it with a hardcoded value (for example, `7.5`).

2. **Calculate the Area**
   - Use the formula:  
     \[
     \text{area} = \pi \times \text{radius}^2
     \]
	   
   - Use the built-in constant `Math.PI` to get an accurate value of π.

3. **Display the Result**
   - Print the calculated area with a clear and meaningful message indicating that it represents the **area of the circle**.

### Expected Output

#### Sample Output
