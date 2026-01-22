<%*
const title = await tp.system.prompt("Enter Problem Name");
if (!title) return;

const filename = title
  .replace(/[^a-zA-Z0-9]+/g, "_")
  .replace(/^_+|_+$/g, "");

const link = await tp.system.prompt("Enter Platform Link (LeetCode/GFG URL)");
const approach = await tp.system.prompt("Enter Approach (Binary Search / Two Pointer / Kadane / etc.)");
let level = await tp.system.prompt("Enter Level (EASY / MODERATE / HARD)");
let status = await tp.system.prompt("Enter Status (Done / Pending)");

level = (level || "").trim().toUpperCase();
status = (status || "Pending").trim();

if (!level) level = "EASY";
if (!status) status = "Pending";

const targetPath = `dsa-abhyaas/DSA/problems/${filename}`;
await tp.file.move(targetPath);

// ✅ Auto-run your master list generator (Linux)
await tp.system.exec(`python /home/mcclusky/dsa-abhyaas/dsa-abhyaas/DSA_SCRIPTS/generate_master.py`);
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

