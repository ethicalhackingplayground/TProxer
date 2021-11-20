## TProxer
A Burp Suite extension made to automate the process of finding reverse proxy path based SSRF.

![Demo](https://github.com/ethicalhackingplayground/TProxer/blob/main/static/demo.png)

### Features

- Attempts to gain access to internal APIs or files through a path based SSRF attack.
  For instance `https://www.example.com/api/v1/users` we try the payload `/..;/..;/..;/..;/` hoping for a **400 Bad Request**:
- Then the Algorithm tries to find the potential internal API root with:
  `https://www.example.com/api/v1/users/..;/..;/..;/` hoping for a **404 Not Found**
- Then, we try to discover content, if anything is found it performs additional test to see if it's 100% internal and worth investigating.
- Supports manual activation through context menu.
- Payloads are supplied by the user under dedicated tab, default values are stored under `query payloads.txt`
- You also selct your own wordlist
- Issues are added under the Issue Activity tab.

### TODO

- [x] N/A
- [ ] N/A
