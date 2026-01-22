<%*
const title = await tp.system.prompt("Enter Problem Name");
if (!title) return;

const filename = title
  .replace(/[^a-zA-Z0-9]+/g, "_")
  .replace(/^_+|_+$/g, "");

const link = await tp.system.prompt("Enter Platform Link (LeetCode/GFG URL)") || "";
const approach = await tp.system.prompt("Enter Approach (Binary Search / Two Pointer / etc.)") || "";

let level = await tp.system.prompt("Enter Level (EASY / MODERATE / HARD)") || "EASY";
level = level.trim().toUpperCase();

let status = await tp.system.prompt("Enter Status (Done / Pending)") || "Pending";
status = status.trim();

const targetPath = `DSA/problems/${filename}.md`;
await tp.file.move(targetPath);

// ✅ Auto-update master list
await tp.system.exec("python /home/mcclusky/dsa-abhyaas/dsa-abhyaas/DSA_SCRIPTS/generate_master.py");
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

