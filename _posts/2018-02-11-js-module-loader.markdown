---
layout:     post
title:      "有用的资源"
subtitle:   ""
date:       2018-02-11
author:     "Dyn"
header-img: "img/post-bg-js-module.jpg"
catalog: true
---
## contextualized word representations for reading comprehension
###### arXiv 10 Dec 2017
###### Tel-Aviv University

#### 任务描述
* QA，答案是篇章字符串的一个子字符串
* 数据集: SQuAD 

#### 创新点
> Contextualized Word Representations

* 概念  
* non-contextual representation: 原始词向量
* contextual representation:  
* RNN-based token re-embedding (TR) : 原始token的词向量过RNN之后的hidden states作为token的embedding
* LM-augmented token re-embedding (TR + LM) : 原始token的词向量过RNN之后的hidden states串接上语言模型的embedding作为token的embedding   
* TR + LM (L1)  
* TR + LM (L2)  
* 实现  
contextual representation 和 non-contextual representation 一起过一个highway network 。

#### 模型架构
* embedding  
* Passage-independent question representation（问句对自己计算attention,找到问句中最重要的信息）  
* Passage-aligned question representations(文档和问句计算attention，fuse问句的信息)  
* Augmented passage token representations

* encoder  
* 双向LSTM
* answer layer  
* span a = (l,r)   
* 全连接层预测答案得分
* 损失函数  
* 最大似然概率

#### 模型性能

#### 相关结论
1. Importance of context  
篇章上下文的信息对找到正确答案来说很重要
2. Context complements rare words  
词频较低的词语相对于词向量，会倾向于选择利用上下文的信息来作为自己的表示  
3. Extent of context utilization  
相对于上下文的信息，词向量是一个主要的信息来源（好的词向量很重要）

#### 小trick


#### 论文摘要
> In this work, we hypothesize that the still-relatively-small size of current RC datasets, combined with the fact that a large part of examples can be solved with local question-document matching heuristics ([Jia and Liang, 2017](https://arxiv.org/abs/1707.07328); [Weissenborn et al.,2017](http://www.aclweb.org/anthology/K17-1028)), 
results in models that make limited use of context.

> When encoding the representation of a word token in its encompassing sequence (either the question or the passage),
we are interested in allowing extra computation to be carried out over the sequence and evaluating the extent to which context is utilized in the resultant representation.

#### 参考资料

