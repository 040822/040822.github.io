---
title: 更新日志
date: 2024-02-11 17:21:58
---
没事就写点东西吧。

2020.03.19  
用wordpress创建第一个博客。

2020.03.20  
创建各种页面

2020.03.21  
做题，被 普及组- 各种虐/(ㄒoㄒ)/~~

2020.04.20

本次更新如下：  
1.将服务器从腾讯云的改为阿里云的了  
2.由于现在服务器是香港的，因此可以使用备案的域名了

2021.03.20  
将服务器从阿里云改成了本地虚拟机了。

2021.03.21  
将虚拟机的网络连接模式改为仅主机模式，这样即使是没有网络的情况下也能上博客了。

2024.02.10  
在折腾一大圈之后决心使用白嫖的github pages和hexo框架重建博客。并开始将用wordpress搭建的旧博客迁移至新博客上。

2024.02.17  
更换了渲染器，现在博客可以支持数学公式了。  
教程：  
https://blog.homurax.com/2022/08/21/hexo-theme-latex/  
https://blog.windsky.tech/2021/01/30/Hexo-Katex/  
https://blog.chaos.run/dreams/hexo-enable-math-support/index.html  

2024.04.17
惨痛的经验教训告诉我们：1.不要将过大的图片上传至git库里，这样只会使你的git库变得炒鸡大。2.没事别更新包。这次更新keep主题（4.0.11）后我的相册直接炸掉，回退至4.0.6之后才解决问题。3.如果有地方出bug了而你又排查不出来的话，尝试看一下依赖包的版本是否变动吧。

又双叒叕出问题了。文章中用markdown格式引用的相对位置图片不渲染（开了post_asset_folder: true），哭唧唧。  
尝试了以下手段：

- npm install hexo-asset-image --save 得知这玩意n年前就停止维护了
- npm install hexo-asset-img --save 看样子是楼上的替代品，但是没有用
- hexo-renderer-marked中 postAsset=true 也没有用
- npm install hexo-image-link --save 终于有用了，虽然生成时会报错，比如：
  
``` 11
Markdown Image Path does not exists!
![alt text](image-43.png)
Label :alt text
image-43.png
```

更致命的是以html格式引用的图片反而会不加载了QAQ  

- npm i hexo-renderer-markdown-it-plus --save 成功解决，但是TOC又不渲染了QAQ
- [渲染器对比](https://bugwz.com/2019/09/17/hexo-markdown-renderer/#1-1%E3%80%81hexo-renderer-marked)

最终还是没能解决TOC问题，崩溃了。

2024.04.18

解决TOC问题了，在设置里把后边这个要关掉，true和toc有冲突。 “relative_link: false”  
