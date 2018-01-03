## contextualized word representations for reading comprehension
#### arXiv 10 Dec 2017
#### Tel-Aviv University

### 任务描述
* QA，答案是篇章字符串的一个子字符串
* 数据集: SQuAD 

### 创新点
1. Contextualized Word Representations
概念: contextual representation, non-contextual representation
non-contextual representation: 原始词向量
contextual representation: 
* RNN-based token re-embedding (TR）
    原始token的词向量过RNN之后的hidden states作为token的embedding
* LM-augmented token re-embedding (TR + LM)
    原始token的词向量过RNN之后的hidden states串接上语言模型的embedding作为token的embedding 
   * TR + LM (L1)
   * TR + LM (L2)
contextual representation 和 non-contextual representation 一起过一个highway network 作为这一层的输出。

### 模型架构
* embedding
    > Passage-independent question representation,Passage-aligned question representations,Augmented passage token representations
    三者串接
    
* encoder
    双向LSTM
* answer layer
    span a = (l,r)
    全连接层预测答案得分
    损失函数：最大似然概率

### 模型性能


### 有用结论


### 论文摘要
> In this work, we hypothesize that the still-relatively-small size of current RC datasets, combined with the fact that a
large part of examples can be solved with local question-document matching heuristics ([Jia and Liang, 2017](https://arxiv.org/abs/1707.07328); [Weissenborn et al.,2017](http://www.aclweb.org/anthology/K17-1028)), 
results in models that make limited use of context.

> When encoding the representation of a word token in its encompassing sequence (either the question or the passage), 
we are interested in allowing extra computation to be carried out over the sequence and evaluating the extent to which context
is utilized in the resultant representation.

### 参考资料

