---
title: 大创list
date: 2024-06-15 00:25:48
tags:
---
## 经费
TODO：
书籍部分：
深度学习-花书
机器学习-西瓜书+南瓜书
深度强化学习-王树森
深度强化学习-劳拉

服务器：
autodl 500~1000的服务器（

硬件：
硬盘是渠道版，报不了QAQ
耳机（bushi）

## 资料
[《动手学深度学习》 — 动手学深度学习 2.0.0 documentation (d2l.ai)](https://zh-v2.d2l.ai/index.html)
[audiocraft.models.musicgen API 文档 --- audiocraft.models.musicgen API documentation (facebookresearch.github.io)](https://facebookresearch.github.io/audiocraft/api_docs/audiocraft/models/musicgen.html#audiocraft.models.musicgen.MusicGen)
[「心迹成曲」项目管理 (kdocs.cn)](https://www.kdocs.cn/l/cvvVO4QKXdRF)
[facebookresearch/audiocraft：Audiocraft 是一个用于深度学习音频处理和生成的库。它具有最先进的 EnCodec 音频压缩器/分词器，以及 MusicGen，一种简单且可控的音乐生成 LM，具有文本和旋律条件。 --- facebookresearch/audiocraft: Audiocraft is a library for audio processing and generation with deep learning. It features the state-of-the-art EnCodec audio compressor / tokenizer, along with MusicGen, a simple and controllable music generation LM with textual and melodic conditioning. (github.com)](https://github.com/facebookresearch/audiocraft)
[[2306.05284] 简单可控的音乐生成 --- [2306.05284] Simple and Controllable Music Generation (arxiv.org)](https://arxiv.org/abs/2306.05284)


## 完成情况
目前打算从audiocraft-main\\demos\\musicgen_app.py入手，app文件已经使用gradio建立了一个简易网站，后续可以在此基础上进行进一步开发。
开发思路：
- 把app文件跑起来√
- 美化页面
- 尝试微调musicgen模型，musicgen已给出一大堆训练代码


## 碎碎语
摆了n个月，快到中期测评了才急急忙忙赶ddl，QAQ
配置环境ing，结果python版本下错了，很多包下不了，QAQ
conda remove启动！啊remove是删除包不是删除环境的啊。
conda remove -n musicLLM --all，启动！
conda create -n musicLLM python=3.9，启动！
![[Pasted image 20240615011113.png]]
运行成功，下边看看怎么微调。
2024.06.14

稍微翻译了一下页面。
2024.06.17