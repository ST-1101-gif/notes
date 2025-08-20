# <center> CSRF -- Cross Site Request Forgery
---
## Cookie and Session Management

### Cookie Attributes
Every cookie is a name-value pair
```php
Set-Cookie: sessionid=abc123; Domain=example.com
```
These additional cookie attributes help the browser determine which cookies should be attached to each request.
- The Domain and Path attributes tell the browser which URLs to send the cookie to. See the next section for more details.
- The Secure attribute tells the browser to only send the cookie over a secure HTTPS connection.
- The HttpOnly attribute prevents JavaScript from accessing and modifying the cookie.
- The expires field tells the browser when to stop remembering the cookie.

## Session
服务器端​​维护的用户状态信息

## Session Management
Cookies are often used to keep users logged in to a website over many requests and responses. When a user sends a login request with a valid username and password, the server will generate a new session token and send it to the user as a cookie. In future requests, the browser will attach the session token cookie and send it to the server. The server maintains a mapping of session tokens to users, so when it receives a request with a session token cookie, it can look up the corresponding user and customize its response accordingly.

- Session tokens are the values that the browser sends to the server to associate the request with a logged-in user. 
- Cookies are how the browser stores and sends session tokens to the server. Cookies can also be used to save other state (attributes). 


## CSRF

### HTML CSRF
利用 html 元素发送 GET 请求
```html
<link href="">
<img src="">
<img lowsrc="">
<img dynsrc="">
<meta http-equiv="refresh" content="0; url=">
<iframe src="">
<frame src="">
<script src=""></script>
<bgsound src=""></bgsound>
<embed src=""></bgsound>
<video src=""></video>
<audio src=""></audio>
<a href=""></a>
<table background=""></table>
......
```
CSS 
```css
@import ""
background:url("")
......
```
表单
```html
<form action="http://www.a.com/register" id="register" method="post">
  <input type=text name="username" value="" />
  <input type=password name="password" value="" />
</form>
<script>
  var f = document.getElementById("register");
  f.inputs[0].value = "test";
  f.inputs[1].value = "passwd";
  f.submit();
</script>
```

### 防御
验证码
验证码强制用户必须与应用进行交互，才能完成最终请求。

Referer Check
检查请求是否来自合法的源。但服务器并非什么时候都能取得 Referer。

Token 

- 随机性
- 生命周期短
- 保密性，如果 Token 出现在 URL 中，则可能会通过 Referer 泄露，应尽量把 Token 放在表单中，把敏感操作由 GET 改为 POST，以表单或 AJAX 的形式提交，避免 Token 泄露。