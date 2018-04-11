---
layout:     post
title:      "FAST AND ACCURATE READING COMPREHENSION BY COMBINING SELF-ATTENTION AND CONVOLUTION"
subtitle:   ""
date:       2018-04-11
author:     "Dyn"
header-img: "img/post-bg-js-module.jpg"
catalog: true
---
## FAST AND ACCURATE READING COMPREHENSION BY COMBINING SELF-ATTENTION AND CONVOLUTION
###### ICLR2018
###### CMU,Google Brain

#### 任务描述
【任务类型】:  阅读理解  
【数据集】: SQUAD,triviQA


#### 创新点
* 没用RNN（所以速度快）
* 结合了transformer里面的multi-head attention
* CNN combined with self-attention
* data augmentation by backtranslation

#### 模型架构
![image](https://note.youdao.com/yws/public/resource/c941817d01a5a905cf4e7ece6b7ecebb/xmlnote/58F04FAC355449719DB757E72215F190/3008)
很多地方挺像BiDAF模型

#### 模型性能
![image](https://note.youdao.com/yws/public/resource/736f6e3a9df414177b61e87f43e29e9a/xmlnote/C59D0EE734134C65B709553C16292F00/3022)


#### trick
data augmented
![image](https://note.youdao.com/yws/public/resource/c941817d01a5a905cf4e7ece6b7ecebb/xmlnote/939D724BFE4840D5BAC8663E1F31A5B7/3017)

#### 论文摘要
> When paraphrasing, we keep the question q unchanged (to avoid accidentally changing its meaning) and generate new triples of (d0, q, a0) such that the new document d0 has the new answer a0 in it. The procedure happens in two steps: (i) document paraphrasing – paraphrase d into d0 and (b) answer extraction – extract a0 from d0 that closely matches a.

> Compared to SQuAD, TriviaQA is more chal- lenging in that: 1) its examples have much longer context (2895 tokens per context on average) and may contain several paragraphs, 2) it is much noisier than SQuAD due to the lack of human labeling, 3) it is possible that the context is not related to the answer at all, as it is crawled by key words.

> Due to the multi-paragraph nature of the context, researchers also find that simple hierarchical or multi-step reading tricks, such as first predicting which paragraph to read and then apply models like BiDAF to pinpoint the answer within that paragraph 

> Recently, attempts have been made to replace the recurrent networks by full convolution or full attention architectures (Kim, 2014; Gehring et al., 2017; Vaswani et al., 2017b; Shen et al., 2017a). Those models have been shown to be not only faster than the RNN architectures, but also effective in other tasks, such as text classification, machine translation or sentiment analysis.

#### 参考资料
* Simple and effective multi-paragraph reading comprehension
* Teaching machines to read and comprehend
* Wikireading: A novel large-scale language understanding task over wikipedia
* The goldilocks principle: Reading children’s books with explicit memory representation
* Learning recurrent span representations for extractive question answering
* Structural embedding of syntactic trees for machine comprehension
* MEMEN: multi-layer embedding with memory networks for machine comprehension
