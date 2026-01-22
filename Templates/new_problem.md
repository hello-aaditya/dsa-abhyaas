<%*
const title = await tp.system.prompt("Enter Problem Name");
if (!title) return;

const filename = title
  .replace(/[^a-zA-Z0-9]+/g, "_")
  .replace(/^_+|_+$/g, "");

const targetPath = `DSA/problems/${filename}.md`;
await tp.file.move(targetPath);

// run script
await tp.system.exec("python /home/mcclusky/dsa-abhyaas/dsa-abhyaas/DSA_SCRIPTS/generate_master.py");
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

arh