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

await tp.file.move(`DSA/problems/${filename}.md`);

// ✅ Update master list
await tp.user.update_dsa_master();
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

