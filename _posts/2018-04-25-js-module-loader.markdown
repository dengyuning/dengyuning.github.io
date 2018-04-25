---
layout:     post
title:      "A Question-Focused Multi-Factor Attention Network for Question Answering"
subtitle:   ""
date:       2018-04-25
author:     "Dyn"
header-img: "img/post-bg-js-module.jpg"
catalog: true
---
## A Question-Focused Multi-Factor Attention Network for Question Answering
###### 2018
###### National University of Singapore

#### 任务描述
* QA类阅读理解
* 数据集:TriviaQA,NewsQA,SearchQA

#### 创新点
* 概念
1. Multi-factor attentive encoding  
多角度的self-attention
2. Question-focused Attentional Pointing  
1. max-attentional question aggregation              通过问句和篇章的attention，找到问句中最关键的词  
2. question type representation
用疑问词(what, who, how, when, which, where, why)和紧跟着疑问词的一个词作为问句类型的表示
* 实现 
#### 模型架构
![image](https://note.youdao.com/yws/public/resource/bd2d33317394ec72bd3d8fd759ad1034/xmlnote/DCB9EF3325FE4F69A88189A0018C17FE/5710)
#### 模型性能

![image](https://note.youdao.com/yws/public/resource/9c77aa51a85ef6fc61376f336346fe35/xmlnote/C4D27B80305145B098E63FD7254E0EBE/5716)
![image](https://note.youdao.com/yws/public/resource/9c77aa51a85ef6fc61376f336346fe35/xmlnote/35B903CF041441ADBA01BDE8CE9747DC/5719)
![image](https://note.youdao.com/yws/public/resource/9c77aa51a85ef6fc61376f336346fe35/xmlnote/7B48F2C82D5C4452B1FA42BFC8C1B7EE/5721)

#### trick


#### 论文摘要
>which learns to aggregate evidence distributed across multiple sentences and identifies the important question words to help extract the answer.  

> Intuitively, AMANDA extracts the answer not only by synthe- sizing relevant facts from the passage but also by implicitly determining the suitable answer type during prediction.

> In practice, recurrent neural networks fail to remember information when the context is long.

> SearchQA (Dunn et al. 2017) is also constructed to more closely reflect IR-style QA. They first collected existing question-answer pairs from a Jeopardy archive and aug- mented them with text snippets retrieved by Google. One difference with TriviaQA is that the evidence passages in SearchQA are Google snippets instead of Wikipedia or Web search documents. This makes reasoning more challenging as the snippets are often very noisy. SearchQA consists of 140,461 question-answer pairs, where each pair has 49.6 snippets on average and each snippet has 37.3 tokens on av- erage.

#### 参考资料
