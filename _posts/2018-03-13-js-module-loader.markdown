---
layout:     post
title:      "遇到的问题"
subtitle:   ""
date:       2018-03-13
author:     "Dyn"
header-img: "img/post-bg-js-module.jpg"
catalog: true
---
1. focal loss : Nan  
> [不过需要注意的是，在TensorFlow中，tf.nn.sigmoid函数，在输出的参数非常大，或者非常小的情况下，会给出边界值1或者0的输出](http://blog.sina.com.cn/s/blog_6ca0f5eb0102wr4j.html)
> [学习率过大](https://www.zhihu.com/question/62441748)
> [github 何凯明 版 focal loss](https://github.com/ailias/Focal-Loss-implement-on-Tensorflow/blob/master/focal_loss.py)
2. [更新Tensor某一维度的值](https://www.google.com.hk/search?safe=strict&q=tensorflow+change+tensor+value&sa=X&ved=0ahUKEwiku6nl3cnYAhWBi5QKHZ7_BQkQ1QIIbigB&biw=1170&bih=803)  
**无法解决**
> theano 支持  
> [tensorflow中的tensor是只读的](https://stackoverflow.com/questions/41516058/tensorflow-theano-tensor-set-subtensor-equivalent)
3. [Python2 unicode 混杂 中文](http://kuanghy.github.io/2017/02/24/python-str-to-unicode-escape)
4. [TypeError: Expected int32, got list containing Tensors of type '_Message' instead.](https://stackoverflow.com/questions/41813665/tensorflow-slim-typeerror-expected-int32-got-list-containing-tensors-of-type)  
> tensorflow的版本问题  
> tf.concat(axis=0,values=[a,b])
5. loss = 0 
> **解决方案**:
> 1. https://stackoverflow.com/questions/43776661/tensorflow-model-gets-loss-0
7. ssh 协议登录不上，能ping通  
用户名写错，ip写错  
8. [Ubuntu新建用户并给其管理员权限](http://www.linuxidc.com/Linux/2016-06/132218.htm)
9. 训练语言模型时遇到NAN的问题
>   调小learning rate
10. 把gensim训练的词向量文件转成word2vec.txt格式
> w2v.wv.save_word2vec_format('wv2.txt',binary=False)
11. [tensorlayer的tl.iterate.minibatches只产生batch_size整除的样本，最后剩下的不足batch_size大小的样本没有用上 
     ](http://blog.csdn.net/rxm1989/article/details/73457858)
12. [TypeError: only integer scalar arrays can be converted to a scalar index](http://blog.csdn.net/accumulate_zhang/article/details/78808038)
13. [Ubuntu14.04 安装python3.6](https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get)
14. [using pip3: module “importlib._bootstrap” has no attribute “SourceFileLoader”](https://stackoverflow.com/questions/44761958/using-pip3-module-importlib-bootstrap-has-no-attribute-sourcefileloader)  

15.[源码安装python3.6和pip3](https://www.jianshu.com/p/325f16755680)  
16. [完全卸载python3.4](https://www.jianshu.com/p/325f16755680)
17. [futures requires Python '>=2.6, <3' but the running Python is 3.6.2](http://www.mamicode.com/info-detail-2176366.html)
18. ImportError: numpy.core.multiarray failed to import
> [方案一 不成功](http://blog.csdn.net/u013041398/article/details/52231969)  
> [方案二 不成功](http://blog.csdn.net/u012542955/article/details/78464049)  
> 原因:pypi.douban.com镜像上的numpy最新版本是1.13.3 所以upgrade显示numpy已经是最新版本  
> 方案三 成功: 从pypi.python.org上下载numpy1.14.0
19. pip3 install --upgrade numpy -vvv 
> -v 这个参数表示可以输出更多的错误信息
20. [bz2 module is not available， No module named '_bz2'](http://www.vuln.cn/8806?replytocom=1924)
21. [loss 为NAN](http://blog.csdn.net/u012436149/article/details/60322085)
22. Could not find any downloads that satisfy the requirement tensorflow 这一般是由于pip版本过低所致  
pip install -U pip  
pip install tensorflow-gpu==1.2
