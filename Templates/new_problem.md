<%*
const title = await tp.system.prompt("Enter Problem Name");
if (!title) return;

const filename = title
  .replace(/[^a-zA-Z0-9]+/g, "_")
  .replace(/^_+|_+$/g, "");

// move the note into DSA/problems with underscore filename
await tp.file.move(`dsa-abhyaas/DSA/problems/${filename}`);

// ✅ run the python script to update DSA_MASTER_LIST.md
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

