<%*
const title = await tp.system.prompt("Enter Problem Name");
if (!title) return;

const filename = title
  .replace(/[^a-zA-Z0-9]+/g, "_")
  .replace(/^_+|_+$/g, "");

const targetPath = `dsa-abhyaas/DSA/problems/${filename}`;
await tp.file.move(targetPath);

// ✅ Run your python script via user function
await tp.user.update_dsa_master();
-%>
---
problem: <% title %>
link:
status: Pending
approach:
level:
---

# Solution
```java

