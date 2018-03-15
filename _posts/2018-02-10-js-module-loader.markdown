---
layout:     post
title:      "contextualized word representations for reading comprehension"
subtitle:   ""
date:       2018-02-10
author:     "Dyn"
header-img: "img/post-bg-js-module.jpg"
catalog: true
---
## Attention-over-Attention Neural Networks for Reading Comprehension
###### ACL 2017
###### 哈工大和科大讯飞联合实验室

#### 任务描述
* 任务类型：完形填空  
* 数据类型:<D,Q,A>三元组，其中Q缺失了一个词（词的类型有很多种），缺失的那个词被视为Q的答案A。
* 数据: CNN 和 Children's Book Test.对于CNN来说，D是新闻的正文，Q则是正文的摘要。对于CBT来说，一篇文档没有对应的摘要，数据组织者把文章的前20句话作为D，第21句话作为Q，缺失的那个词作为答案，答案类型按词性分为命名实体、普通名词、动词和介词这四种。但是介词和动词这两类问题，在大多数情况下可以仅仅根据Q的上下文来给出答案。研究者们主要研究命名实体和普通名词这两类问题。

#### 创新点
* 概念
1. attened attention
2. N-best re-ranking strategy
* 实现 
#### 模型架构
1. Contextual Embedding
> * 词向量过双向GRU
2. Pair-wise Matching Score
> * 计算D和Q的相关性矩阵M
3. Individual Attentions （document-level attention）
> a(t) = softmax(M(1,t),...,M(|D|,t))  
> a = [a(1),a(2),...,a(Q)]
4. Attention-over-Attention
> query-level attention
>> beta(t) = softmax(M(t,1),...,M(t,|Q|))
5. 
#### 模型性能

#### trick


#### 论文摘要

#### 参考资料
