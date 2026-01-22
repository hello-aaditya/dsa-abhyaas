```markdown
<%*
const title = await tp.system.prompt("Enter Problem Name");
const filename = title.replace(/[^a-zA-Z0-9]+/g, "_").replace(/^_+|_+$/g, "");
await tp.file.rename(filename);
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
```
```