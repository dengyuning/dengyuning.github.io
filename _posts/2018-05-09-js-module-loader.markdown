---
layout:     post
title:      "R3 Reinforced Ranker-Reader for Open-Domain Question Answering"
subtitle:   ""
date:       2018-05-09
author:     "Dyn"
header-img: "img/post-bg-js-module.jpg"
catalog: true
---
## R3 Reinforced Ranker-Reader for Open-Domain Question Answering
###### 2017
###### IBM,JD,

#### 任务描述
【模型输入输出】: 输入是一个问题，输出是一个答案。提供IR系统。
> During training we are given only the (q, ag ) pairs, together with an IR model with index built on an open-domain corpus

【数据集】: Quasar-T, SQuADOPEN, WikiMovies, CuratedTREC, WebQuestions

#### 模型架构
* A Ranker and a Reader
![image](https://note.youdao.com/yws/public/resource/d71a693746f6c50168b46213931dd990/xmlnote/1BBDF1D8B8F74D9793E250312BDCB3E9/5770)

* 模型算法
![image](https://note.youdao.com/yws/public/resource/d71a693746f6c50168b46213931dd990/xmlnote/4E82AFE242C6430BB5E424276A496ED3/6373)

#### 创新点
* 用到了强化学习 
* 【实现】:
用match-LSTM(文献)来表示篇章和问句  
ranker: 对每个篇章得到一个固定长度的向量表示，降维为长度为1的向量，作为这个篇章包含答案与否的概率值。  
reader: 一般的抽取式的阅读理解模型


#### 模型性能
![image](https://note.youdao.com/yws/public/resource/e397545c713bc638ec9b8ddfad91e602/xmlnote/B2280DB1D0B84FDEA1BAA007146295D4/6393)

【对比实验】
* Single Reader (SR):  
没有ranker模型，在提供的N个篇章中随机挑选一个作为reader的输入
* Simple Ranker-Reader (SR2):  
结合ranker和reader的损失

#### 论文摘要
> The other four datasets we consider are: SQuAD, the Stanford QA dataset, from which we take only the question- answer pairs and discard the passages to form an open- domain QA setting (denoted as SQuADOPEN); WikiMovies which contains movie-related questions from the OMDb and MovieLens databases and where the questions can be answered using Wikipedia pages; CuratedTREC, based on TREC (Voorhees and Tice 2000) and designed for open-domain QA; and WebQuestion which is designed for knowledge-base QA with answers restricted to Freebase en- tities. For these four datasets under the open-domain QA set- ting, no candidate passages are provided so we build a simi- lar sentence-level Search Index based on English Wikipedia, following Chen et al. 2017a’s work.

> We use the 2016-12-21 dump of En- glish Wikipedia as our sole knowledge source, and build an inverted index with Lucene8. We then take each input ques- tion as a query to search for top-200 articles, rank them with BM25, and split them into sentences. The sentences are then ranked by TF-IDF and the top-200 sentences for each ques- tion retained.

#### 参考资料
[2017b] Wang, S., and Jiang, J. 2017b. Machine compre- hension using match-LSTM and answer pointer. In Proc. of ICLR.    
[github代码](https://github.com/shuohangwang/mprc)    
强化学习还要了解更多
