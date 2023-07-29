#### 实验内容：
比较Firefox和谷歌的记住密码插件的实现区别
#### 理论基础：
Firefox：

Mozilla开发了名为"Network Security Services"（NSS）的开源库，目的是满足开发者创建符合各种安全标准的应用程序。Firefox使用其中一个叫做"Security Decoder Ring"（SDR）的API来帮助实现账号证书的加密和解密功能。

当Firefox配置文件首次创建时，会生成一个随机的SDR密钥和盐（Salt），并将它们存储在名为"key3.db"的文件中。使用这个密钥和盐，Firefox使用3DES加密算法对用户名和密码进行加密。加密后的密文以Base64编码方式存储在名为"signons.sqlite"的SQLite数据库中。"signons.sqlite"和"key3.db"文件都存放在路径"%APPDATA%\Mozilla\Firefox\Profiles\[随机配置文件]"下。

如果想要获取SDR密钥，根据描述，该密钥被保存在一个被称为PKCS#11的软件令牌中。这个令牌被放入PKCS#11槽位中。因此，需要访问该槽位来获取账户证书的解密密钥。

另外，SDR使用的是3DES（DES-EDE-CBC）算法进行加密。解密密钥由Mozilla称为"主密码"的哈希值和存储在"key3.db"文件中的"全局盐"值共同生成。

Firefox用户可以在浏览器设置中设置主密码，但是很多用户对这个功能并不了解。正如前面所述，用户的整个账户证书完整性链条是依赖于所选择的密码的安全性的，而这个密码是攻击者所不知道的。如果用户设置了一个强密码，那么攻击者想要恢复存储的证书将变得非常困难。

然而，如果用户没有设置主密码，系统将使用空密码。这意味着攻击者可以提取全局盐，并使用该盐与空密码进行哈希运算，然后使用得到的结果来破解SDR密钥，从而危害用户的证书。


chrome：

简单的讲，chrome就是用户系统密码将用户保存在浏览器的密码加密保存在一个SQLite数据库里，保存在电脑里\Chrome\User Data\Default\Login Data 文件中。对这个文件执行一下win32crypt.CryptUnprotectData函数，调用系统解密就可以直接解密出里面保存的密码。换言之，任何程序里面只要使用解密命令就能用当前系统密码去解密chrome的密码文件，就可以查看到把chrome保存的密码。

当用户访问网站时，Chrome会首先判断此次登陆是否是一次成功的登录，如果成功登录，并且使用的是一套新的证书，这个证书是浏览器之前没有生成过的，Chrome就会生成一个提示条，询问用户是否需要记住密码，当点击“保存密码”时，就会调用Chrome密码管理器的“保存”函数来响应操作。在这函数被调用之后，执行AddLoginImpl()函数的任务被调用，该函数会调用登陆数据库对象的AddLogin()函数，以检查其操作是否成功。最终，我们看到密码是调用Windows API函数CryptProtectData来加密的。这意味着，只有用加密时使用的登陆证书，密码才能被恢复。而这根本不是问题，恶意软件通常就是在用户登陆环境下执行的。

根据参考链接中的内容我们了解到：破解密码，只需要调用Windows API中的CryptUnprotectData函数。幸运地是，Python为调用Windows API准备了一个完美的叫做pywin32的库。这使得破解密码变得非常容易。

总结：综上所述我们可以发现，在安全方面Firefox远高于chrome。

#### 参考链接
浏览器是如何存储密码的：https://www.cnblogs.com/shoubianxingchen/p/5073077.html

浏览器记住密码的机制：https://www.cnblogs.com/lcl101/p/13305273.html

再来谈谈浏览器存密码这件事：https://zhuanlan.zhihu.com/p/72016575#
