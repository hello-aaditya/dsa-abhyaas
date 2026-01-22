<%*
const title = await tp.system.prompt("Enter Problem Name");
if (!title) return;

const filename = title
  .replace(/[^a-zA-Z0-9]+/g, "_")
  .replace(/^_+|_+$/g, "");

const link = await tp.system.prompt("Enter Platform Link (LeetCode/GFG URL)") || "";
const approach = await tp.system.prompt("Enter Approach (Binary Search / Two Pointer / etc.)") || "";
let level = await tp.system.prompt("Enter Level (EASY / MODERATE / HARD)") || "EASY";
let status = await tp.system.prompt("Enter Status (Done / Pending)") || "Pending";

level = level.trim().toUpperCase();
status = status.trim();

await tp.file.move(`dsa-abhyaas/DSA/problems/${filename}`);

// ✅ wait so content gets saved properly, then update master list
await tp.system.sleep(2000);
-%>
---
problem: <% title %>
link: <% link %>
status: <% status %>
approach: <% approach %>
level: <% level %>
---

# Solution
```java

