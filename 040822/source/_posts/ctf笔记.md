---
title: ctf笔记
date: 2024-07-25 22:13:23
tags:
---

## 资料
[简介 - CTF Wiki (ctf-wiki.org)](https://ctf-wiki.org/)
[BUUCTF在线评测 (buuoj.cn)](https://buuoj.cn/challenges)

## BUUCTF 部分习题思路

### MISC

#### 金三胖
把gif的各帧取出来即可。
碎碎念：组合各部分flag的时候，我组合了好几遍才得到正确的flag，QAQ。
#### rar
穷举密码就可以了。一开始试图自己写一个py代码，结果出现了bug，后来才知道archpr这款神器。
[一篇文章带你搞定ARCHPR的下载和使用-CSDN博客](https://blog.csdn.net/csjjjd/article/details/135098907)

#### ZIP伪加密
wiki上有对伪加密的介绍。
[zip格式伪加密_504b0304-CSDN博客](https://blog.csdn.net/specter11235/article/details/70306436
![[Pasted image 20240725222432.png]]
PS:按照wiki对zip目录结构的介绍，08 00是通用位标记，但实际上它前边两位09 00才是通用位标记，有点坑QAQ。问题可能在于此文件没有那个“解压所需 pkware 的最低版本”占位。

#### 文件中的秘密
图片属性

#### 你竟然赶我走
16进制查看器，启动！
vscode插件：Hex Editor

#### 乌镇峰会种图
同上

#### 大白
在网上搜资料，被剧透了一脸QAQ
[＜总结＞CTF·图片隐写_图片隐写 ctf-CSDN博客](https://blog.csdn.net/qq_57061511/article/details/117999226)
题目中的“看不见”意思是这样：windows默认图片查看器能打开，但只能看到图片的上端（679x256）部分，有些图片查看器则直接打不开图片（比如kail、vscode）。这题的问题是，图片头数据块记录的宽高与实际宽高不匹配，因此我们需要修改头数据块。
图片的尺寸679x256，对应的十六进制数如下，修改后边部分即可。
![[Pasted image 20240725231553.png]]
实际上，wiki-png页面上有提这类题目，如果修改的是宽而不是高的话那么情况更为复杂，详情请看wiki。

#### 二维码
hex查看器可以发现图片里藏了个txt文件，将图片后缀名改为rar后能用压缩软件打开。
![[Pasted image 20240725232105.png]]

但是！问题在于，这个rar文件ARCHPR解析不了！可能情况如下：1.它就不是个rar文件 2.它是高版本rar文件，ARCHPR不支持，需要换一个密码破解器。
TODO

#### 小明的保险箱
文件前部分是一大堆诸如
`html
</rdf:li></rdf:Bag>
</dc:subject><dc:title><rdf:Alt xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:li xml:lang="x-default">3dnew.com 高清图片</rdf:li></rdf:Alt>
</dc:title><dc:description><rdf:Alt xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:li xml:lang="x-default">3dnew.com 高清图片</rdf:li></rdf:Alt>
`
之类的奇奇怪怪的xml代码，推测为图片的版权信息什么的，用exif查看器解析，并没有得到什么有用的信息。

文件最后藏了个2.txt，但是将文件更改为rar和zip格式都无法打开QAQ，于是就卡在了这里。
TODO

#### N种方法解决
所给的exe文件无法打开，用文本查看器查看exe文件，发现内容为“data:image/jpg;base64,iVBORw...”，显然是用base64加密的jpg文件，于是让copilot写了个代码

```python
import base64

# Base64 编码的图像数据
base64_data = "iVBORw0KGgoAAAANSUhEUgAAAIUAAACFCAY"

# 解码 Base64 数据

image_data = base64.b64decode(base64_data)

# 将解码后的数据写入 JPEG 文件
with open("output.jpg", "wb") as file:
    file.write(image_data)

print("图像已成功保存为 output.jpg")
```
解出来张二维码，微信扫一下即可得到答案。
ps：我记得KEY要换成flag。

#### 基础破解
4位数字而已，吃我ARCHPR大法！
解出来一段奇奇怪怪的字符串，加上flag之后居然过不了？！这说明flag被加密了，猜测格式为base64，解一下即可。

以下为copilot的帮助：

你提供的字符串 `ZmxhZ...0=` 看起来像是一个 Base64 编码的字符串。我们可以先解码它，看看解码后的内容是什么。

以下是一个使用 Python 解码 Base64 字符串的示例代码：

```python
import base64

# Base64 编码的字符串
encoded_str = "114514"

# 解码 Base64 字符串
decoded_bytes = base64.b64decode(encoded_str)
decoded_str = decoded_bytes.decode('utf-8')

print("解码后的字符串:", decoded_str)
```

运行这段代码后，你会得到解码后的字符串。根据解码后的内容，你可以进一步判断它是否使用了其他加密方法。

如果你需要进一步的帮助，请告诉我。

为什么你觉得他是个base64编码的字符串，有什么特征吗？

我认为它是一个 Base64 编码的字符串，主要基于以下几个特征：

1. **字符集**：Base64 编码使用的字符集包括大写字母（A-Z）、小写字母（a-z）、数字（0-9）、加号（+）和斜杠（/），以及等号（=）作为填充字符。你提供的字符串符合这个字符集。

2. **长度**：Base64 编码的字符串长度通常是 4 的倍数，因为每 3 个字节的数据会被编码为 4 个字符。如果长度不是 4 的倍数，字符串末尾会使用等号（=）进行填充。你提供的字符串长度为 48 个字符，符合这一特征。

3. **常见用途**：Base64 编码常用于在文本环境中传输二进制数据，例如嵌入图像数据、加密数据或其他二进制文件。你提供的字符串看起来像是这种用途。

基于这些特征，我推测它是一个 Base64 编码的字符串。通过解码它，我们可以验证这一点。

如果你有其他问题或需要进一步的帮助，请告诉我。

#### LSB
新的神器。
[Giotino/stegsolve (github.com)](https://github.com/Giotino/stegsolve)
但是，用这玩意分析图片分析了半天都没分析出来，先摆了QAQ
TODO


### Crypto

#### 一眼就解密
base64

#### MD5
[MD5 - CTF Wiki (ctf-wiki.org)](https://ctf-wiki.org/crypto/hash/md5/)
记得加上flag

#### Url编码
[URL 编码/解码 - 锤子在线工具 (toolhelper.cn)](https://www.toolhelper.cn/EncodeDecode/Url)

#### 看我回旋踢
[ROT5、ROT13、ROT18、ROT47位移编码 (qqxiuzi.cn)](https://www.qqxiuzi.cn/bianma/ROT5-13-18-47.php)
PS：rot13和rot18都能恢复成flag，但结果不一样。

#### 摩丝
[在线摩斯密码翻译器 (lddgo.net)](https://www.lddgo.net/encrypt/morse)

#### password
题目意思：让你猜张三可能设置的密码。记得将key换成flag

#### Quoted-printable
[Quoted-printable - 维基百科，自由的百科全书 (wikipedia.org)](https://zh.wikipedia.org/wiki/Quoted-printable)
[Quoted-printable - 在线工具 (try8.cn)](https://try8.cn/tool/code/qp)
flag居然是中文

#### 篱笆墙的影子
题意有点不明，但猜测意思可能是：字符串的字母本身不变，也就是说要实现felhaagv=》flag
一开始我还以为只是单纯的删减字母以实现这个变换，后来才发现（被剧透了）删去的字母居然有规律，为隔一个删一个：传说中的栅式加密。恢复后的flag有两段，合起来就可以了。

#### Rabbit
[在线Rabbit加密 | Rabbit解密- 在线工具 (sojson.com)](https://www.sojson.com/encrypt_rabbit.html)
[深入了解Rabbit加密技术：原理、实现与应用-CSDN博客](https://blog.csdn.net/qq_42210428/article/details/134628813)

#### RSA
要计算RSA的私钥`d`，我们需要使用以下公式：

\[ d \equiv e^{-1} \mod \phi(n) \]

其中：
- \( n = p \times q \)
- \( \phi(n) = (p - 1) \times (q - 1) \)
- \( e \) 是公钥的指数
- \( d \) 是私钥的指数

我们需要计算出 \( \phi(n) \)，然后找到 \( e \) 的模 \( \phi(n) \) 的逆元。

以下是Python代码来计算私钥`d`：

```python
from sympy import mod_inverse

# 给定的值
p = 114514
q = 114514
e = 114514

# 计算 n 和 φ(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# 计算 d
d = mod_inverse(e, phi_n)

# 打印结果
print(f"flag{{{d}}}")
```

运行这段代码，你将得到私钥`d`，并将其格式化为`flag{}`的形式。

#### Alice与Bob
暴力分解即可
[免费在线MD5加密解密工具 - 32位和16位大小写 | 极客工具你的在线免费工具库 (geekstool.com)](https://www.geekstool.com/tool/md5)

#### rsarsa

要使用 RSA 算法解码密文 [`c`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fwx%2Foffice%2Fahaic%2F040822.github.io%2Fc%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\wx\office\ahaic\040822.github.io\c")，需要执行以下步骤：

1. 计算模数 [`n = p * q`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2Fwx%2Foffice%2Fahaic%2F040822.github.io%2Fpython%2F0.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A2%2C%22character%22%3A13%7D%5D "python/0.py")。
2. 计算欧拉函数 `φ(n) = (p - 1) * (q - 1)`。
3. 计算私钥指数 `d`，使得 `d * e ≡ 1 (mod φ(n))`。
4. 使用私钥指数 `d` 解码密文 [`c`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fwx%2Foffice%2Fahaic%2F040822.github.io%2Fc%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\wx\office\ahaic\040822.github.io\c")，得到明文 `m`，即 `m = c^d % n`。

以下是详细步骤和代码：

步骤
1. 计算 [`n`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2Fwx%2Foffice%2Fahaic%2F040822.github.io%2Fpython%2F0.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A2%2C%22character%22%3A13%7D%5D "python/0.py") 和 `φ(n)`。
2. 使用扩展欧几里得算法计算 `d`。
3. 使用 `d` 解码密文 [`c`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fwx%2Foffice%2Fahaic%2F040822.github.io%2Fc%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\wx\office\ahaic\040822.github.io\c")。

```python
from sympy import mod_inverse

# 给定的参数
p =
q = 
e = 65537
c = 

# 计算 n 和 φ(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# 计算私钥指数 d
d = mod_inverse(e, phi_n)

# 解码密文 c
m = pow(c, d, n)



print("解码后的消息是:", m)
```

#### 大帝的密码武器
附件是个没密码的zip文件，显然是凯撒。

#### 萌萌哒的八戒
显然，附件不是个zip文件，用hex查看器查看一下就知道了。
zip文件头：50 4B 03 04
rar文件头：52 61 72 21 1A 07 00

解压后得到一张图片，但是题目却说需要获得代码？？？直接懵逼。如果是misc题的话，首先会考虑图片隐写，但这是crypto题。
观察图片发现，题目下方有一些奇奇怪怪的符号，丢给谷歌图片，我们获得了一个奇奇怪怪的幻灯片：[Security Intro 資安入門 - Latest version - HackMD](https://hackmd.io/@Sean64/sec?print-pdf#/)
竹北高中某前辈制作的ctf入门pdf，在这个pdf中就能找到类似的题目：猪圈密码
[猪圈密码 - 维基百科，自由的百科全书 (wikipedia.org)](https://zh.wikipedia.org/wiki/%E8%B1%AC%E5%9C%88%E5%AF%86%E7%A2%BC)
对着密码表解密即可得到结果。结果是小写，没有空格。

#### RSA1
```
from sympy import mod_inverse

  

# 给定的参数

p =

q = 

dp = 

dq = 

c = 

  

# 计算模数 n

n = p * q

  

# 使用 CRT 解码密文 c

m1 = pow(c, dp, p)

m2 = pow(c, dq, q)

  

# 计算 q_inv

q_inv = mod_inverse(q, p)

  

# 使用 CRT 组合结果

h = (q_inv * (m1 - m2)) % p

m = m2 + h * q

  

# 将明文转换为字符串

message = bytes.fromhex(hex(m)[2:]).decode('utf-8')

  

print("解码后的消息是:", m)
```
中国剩余定理，解码后用
```python
message = bytes.fromhex(hex(m)[2:]).decode('utf-8')
```
转换成字符串，再把noxCTF改成flag

#### Unencode
[Uuencode编码（加密）；Uuencode解码（解密）｜文字加密和解密工具 (qqxiuzi.cn)](https://www.qqxiuzi.cn/bianma/uuencode.php)

#### 还原大师
暴力即可。

#### [AFCTF2018]Morse
每个符号用“\”分隔，解码后可得到十六进制字符串（因为都是数字和A~F的字母，所以说首先猜测为hex），转换之后即可，需要把afctf变成flag。

#### 密码学的心声
111114157166145123145143165162151164171126145162171115165143150