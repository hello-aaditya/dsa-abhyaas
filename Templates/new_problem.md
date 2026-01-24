<%*
const title = await tp.system.prompt("Enter Problem Name");
if (!title) return;

const filename = title
  .replace(/[^a-zA-Z0-9]+/g, "_")
  .replace(/^_+|_+$/g, "");

// ✅ Dropdowns
const statusOptions = ["PENDING", "DONE"];
const levelOptions = ["EASY", "MODERATE", "HARD"];
const approachOptions = [
  "Binary Search",
  "Cyclic Sort",
  "Two Pointer",
  "Sliding Window",
  "Kadane's Algorithm",
  "Prefix Sum",
  "Hashing",
  "Sorting",
  "Recursion",
  "Backtracking",
  "Greedy",
  "Dynamic Programming",
  "Graph",
  "Tree",
  "Stack",
  "Queue"
];

const status = await tp.system.suggester(statusOptions, statusOptions);
const level = await tp.system.suggester(levelOptions, levelOptions);

// ✅ Multi-approach support
const primaryApproach = await tp.system.suggester(approachOptions, approachOptions);
const extraApproach = await tp.system.prompt("Extra Approach (optional, comma separated)") || "";

const approach = extraApproach.trim()
  ? `${primaryApproach}, ${extraApproach.trim()}`
  : primaryApproach;

const link = await tp.system.prompt("Enter Platform Link (LeetCode/GFG URL)") || "";
const prerequisite = await tp.system.prompt("Enter Pre-requisite link (optional)") || "";
const video = await tp.system.prompt("Enter Video Solution link (optional)") || "";

// ✅ Move/rename into problems folder
await tp.file.move(`dsa-abhyaas/DSA/problems/${filename}`);
-%>
---
problem: <% title %>
link: <% link %>
status: <% status %>
approach: <% approach %>
level: <% level %>
prerequisite: <% prerequisite %>
video: <% video %>
---

# Solution
```java

