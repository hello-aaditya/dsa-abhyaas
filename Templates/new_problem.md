<%*
const title = await tp.system.prompt("Enter Problem Name");
if (!title) return;

const filename = title
  .replace(/[^a-zA-Z0-9]+/g, "_")
  .replace(/^_+|_+$/g, "");

const targetPath = `DSA/problems/${filename}.md`;

// Move the current note to DSA/problems/ with the cleaned filename
await tp.file.move(targetPath);
%>
---
problem: <% title %>
link: 
status: Pending
approach: 
level: 
---

# Solution
```java

