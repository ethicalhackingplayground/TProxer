<h1 align="center">TProxer
  <br>
    <img src="https://media.istockphoto.com/vectors/spy-agent-detective-vector-id911660874?k=20&m=911660874&s=612x612&w=0&h=1zkZPaYJ1o8948xDc5ikQ2bKbyuPzsZQrZaKBnO55_4=" width="200px" alt="Erebus">
</h1>

<h4 align="center">A Burp Suite extension made to automate the process of finding reverse proxy path based SSRF.</h4>

<p align="center">
  <a href="/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg"/></a>
  <a href="https://docs.python.org/3/index.html"><img src="https://img.shields.io/badge/python-3.6-blue.svg"/></a>
  <a href="https://github.com/ethicalhackingplayground/TProxer/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
  <a href="https://twitter.com/z0idsec"><img src="https://img.shields.io/twitter/follow/z0idsec.svg?logo=twitter"></a>
  <a href="https://discord.gg/MQWCem5b"><img src="https://img.shields.io/discord/862900124740616192.svg?logo=discord"></a>
</p>

<p align="center">
  <a href="#how-it-works">How</a> •
  <a href="#install">Install</a> •
  <a href="#todo">Todo</a> •
  <a href="https://discord.gg/MQWCem5b">Join Discord</a> 
</p>

---

<h1 align="center">
  <br>
    <img src="https://github.com/ethicalhackingplayground/TProxer/blob/main/static/demo.png" width="500px" alt="TProxer">
</h1>

### How it works

- Attempts to gain access to internal APIs or files through a path based SSRF attack.
  For instance `https://www.example.com/api/v1/users` we try the payload `/..;/..;/..;/..;/` hoping for a **400 Bad Request**:
- Then the Algorithm tries to find the potential internal API root with:
  `https://www.example.com/api/v1/users/..;/..;/..;/` hoping for a **404 Not Found**
- Then, we try to discover content, if anything is found it performs additional test to see if it's 100% internal and worth investigating.
- Supports manual activation through context menu.
- Payloads are supplied by the user under dedicated tab, default values are stored under `query payloads.txt`
- You can also select your own wordlist
- Issues are added under the Issue Activity tab.

---

### Install

```bash
$ git clone https://github.com/ethicalhackingplayground/TProxer
```

- Download Jython from:

[https://www.jython.org/download.html](https://www.jython.org/download.html)

- Load burp, Extender -> Options
- Go to Python Environment -> Select file -> Select jython.jar
- Go to Extensions -> Add -> TProx.py

---

### Todo

- [ ] Make a better design
- [ ] Add more customization.

---

### License

TProxer is distributed under [MIT License](https://github.com/ethicalhackingplayground/TProxer/blob/main/LICENSE)

<h1 align="left">
  <a href="https://discord.gg/MQWCem5b"><img src="static/Join-Discord.png" width="380" alt="Join Discord"></a>
</h1>
