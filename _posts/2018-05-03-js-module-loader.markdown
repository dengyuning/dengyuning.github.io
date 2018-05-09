---
layout:     post
title:      "EVIDENCE AGGREGATION FOR ANSWER RE-RANKING IN OPEN-DOMAIN QUESTION ANSWERING"
subtitle:   ""
date:       2018-05-03
author:     "Dyn"
header-img: "img/post-bg-js-module.jpg"
catalog: true
---
## EVIDENCE AGGREGATION FOR ANSWER RE-RANKING IN OPEN-DOMAIN QUESTION ANSWERING
###### 2018 ICLR under review
###### 新加坡管理大学，IBM research

#### 任务描述
【模型输入与输出】: 输入是问题和N篇文档，输出是答案。  
【数据集】: Quasar-T, SearchQA,  TriviaQA


#### 模型架构
非端到端的模型

![image](https://note.youdao.com/yws/public/resource/3af6b1c0acb0ae3ddb9181197b595c69/xmlnote/D850326ED16F434FA4ADDAA2AE60B833/6415)

#### 创新点
* A strength-based re-ranker: 两个指标，一个是候选答案出现在多少个篇章中，一个是候选答案的概率（该候选答案在多个篇章的概率值相加）
* A coverage-basedre-ranker:
把所有包含答案的篇章串接到一起，作为新的context。计算新的context和question的attention，作为一个新的指标。  

【实现】   
对于输入的N篇文档，每个文档出一个答案。抽取答案的模型采用的是R3（Reinforced reader-ranker for open-domain question answering）,然后对N个答案进行进行重排序。重排序的过程是论文的核心。  
排序策略分为两类，一类是evidence strength,一类是evidence coverage.
1. EVIDENCE AGGREGATION FOR STRENGTH-BASED RE-RANKER
> Measuring Strength by Count 最简单的投票机制  
> Measuring Strength by Probability 每个答案的得分加起来

2. EVIDENCE AGGREGATION FOR COVERAGE-BASED RE-RANKER
> R3模型给出了K个答案，每个答案将获得一个新的context。新的context是将该答案出现过的所有篇章串接到一起。计算这个新的context表示和答案和问句串接到一起的新表示之间的attention，然后得到一个匹配表示。K个匹配表示线性变换为K个scaler,作为这个答案和篇章的匹配度（或得分，具体意义待研究）。

#### 模型性能
![image](https://note.youdao.com/yws/public/resource/e397545c713bc638ec9b8ddfad91e602/xmlnote/B2280DB1D0B84FDEA1BAA007146295D4/6393)

#### 论文摘要
> Specifically, we first collect the top-K candidate answers based on their probabil- ities computed by a standard RC/QA system, and then we use two proposed re-rankers to re-score the answer candidates by aggregating each candidate’s evidence in different ways.

> We first use a pre-trained R3 model (Wang et al., 2017), which gets the state-of-the-art performance on the three public datasets we consider, to generate the top 50 candidate spans for the training, development and test datasets, and we use them for further ranking. During training, if the ground- truth answer does not appear in the answer candidates, we will manually add it into the answer candidate list.

#### 参考资料

