---
layout:     post
title:      "有用的Python小代码"
subtitle:   ""
date:       2018-07-03
author:     "Dyn"
header-img: "img/post-bg-js-module.jpg"
catalog: true
---

##### 判断一个字符串中是否包含中文字符
```
def has_ch(word):
for ch in word:
if "\u4e00"< ch< "\u9fa5":
return True
return False
```
