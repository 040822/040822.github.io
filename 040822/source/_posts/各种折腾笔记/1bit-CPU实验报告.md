---
title: 1bit-CPU实验报告
date: 2024-05-27 19:18:55
tags: 
categories: 开发笔记
---
## 实验资料
[比人类计算还慢的处理器——“世界级超低性能”1bit 1HZ 处理器 (qq.com)](https://mp.weixin.qq.com/s/NeROesBzsaLLNQtm5BNXIQ)
[1bit CPU 組み立てキット | 1bit-CPU (naoto64.github.io)](https://naoto64.github.io/1bit-CPU/)
### 电路图
![[IMG-20240527203855851.png]]
### PCB设计图与实物图
![[IMG-20240527203957553.png]]
![[IMG-20240527204007731.png]]

## 仿真电路图
![[IMG-20240527203301685.png]]
其中原电路图的USB部分是供电用的,这里用仿真电压源代替；原电路图的c3~c7是与主要部分分离的，但在pcb板设计时是连起来的，因此这里将c3~c7连了起来；原电路图还有个游离于主要部分以外的U1G、U2C、U3E（74HC14、74HC74、74HC00），但实物图中是没有这三个元件的，不懂这部分是干什么用的，推测这里可能代表主要部分的这三个元件共源共地。