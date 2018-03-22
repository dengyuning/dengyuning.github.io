---
layout:     post
title:      "Stochastic Answer Networks for Machine Reading Comprehension"
subtitle:   ""
date:       2018-02-08
author:     "Dyn"
header-img: "img/post-bg-js-module.jpg"
catalog: true
---
## Stochastic Answer Networks for Machine Reading Comprehension
###### arXiv 10 Dec 2017
###### Microsoft Research

#### 任务描述
* QA
* 数据集

#### 创新点
* 概念 stochastic answer network
* 实现 ： 详见 _模型架构_

#### 模型架构
* lexicon encoding layer
1. 9维POS embedding
2. 8维NER embedding
3. 3维exact match feature (original,lowercase,lemma)
4. aligned question embeddings
* contextual encoding layer
1. 问句和篇章使用同一个LSTM,hidden_size 设为128  
2. LSTM输入为 lexicon encoding layer 的输出串接上600 维的contextualized embedding  
* memory generation layer  
1. 通过attention机制实现
2. 双向attention 和 self—attention
3. 得到的新的篇章的表示，过一个双向LSTM

* final answer module
1. multi-step reasoning : T
2. 每次用一个GRU来预测答案，GRU的输入是x_t, x_t是用GRU的上一个cell的hidden_states 和memory计算得到的。用GRU的最后一个hidden states来计算答案的开始和结束位置的概率。
3. 对T个step的预测结果做一个平均。在训练阶段，做平均前会对T个step的预测结果进行dropout

#### 模型性能
![image](http://note.youdao.com/favicon.ico)
* 对比实验
* 模型性能
* 
#### trick
* Maxout layer : reduce parameter size
* Layer normalization
* contextualized representation

#### 论文摘要
> To avoiding over-fitting, we concatenate the output of a pre-trained 600-dimensional contextualized embedding1 ([McCann et al.,2017](https://arxiv.org/pdf/1708.00107.pdf)), which is trained on English-German machine translation dataset.  

> Dropout at the final layer level, where randomness
is introduced to the averaging of predictions,
prevents our model from relying exclusively
on a particular step to generate correct output.

> Pioneered by (Hill et al., 2016; Dhingra et al.,
2016; Sordoni et al., 2016; Kumar et al., 2015),
who used a predetermined fixed number of reasoning
steps, Shen et al (2016; 2017) showed
that multi-step reasoning outperforms single-step
ones and dynamic multi-step reasoning further
outperformed the fixed multi-step ones on two distinct
MRC datasets (SQuAD and MS MARCO).
But these models have to be trained using reinforcement
learning methods, e.g., policy gradient,
which are tricky to implement due to the instability
issue. Our model is different in that we fix the
number of reasoning steps, but perform stochastic
dropout to prevent step bias. Further, our model
can also be trained by using the back-propagation
algorithm, which is simple and yet efficient as single
step reasoning.

#### 参考资料


