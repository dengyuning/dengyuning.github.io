---
layout:     post
title:      "Machine Reading Comprehension With Self-Matching Networks"
subtitle:   ""
date:       2018-02-09
author:     "Dyn"
header-img: "img/post-bg-js-module.jpg"
catalog: true
---
## Machine Reading Comprehension With Self-Matching Networks
###### 时间
###### 微软亚洲，自然语言处理组

#### 任务描述
* 任务类型:QA
* 数据集: SQUAD

#### 创新点
* gated self matching 
* 实现

#### 模型架构
* encoder
> 字、词向量串接在一起，过双向GRU

* interaction
> 1. Gated Attention-Based Recurrent Networks
> 2. Self-Matching Attention

* point layer
> RNN : time step=1时 输出start 的位置，time step=2时输出end的位置。RNN的初始状态为问句的信息。

#### 模型性能

#### details
* case-sentitive glove embeddings, fixed during training
* zero vectors to represent all out-of-vocab words
* use 1 layer of bi-directional GRU to compute character-level embeddings

#### trick


#### 论文摘要

#### 参考资料


