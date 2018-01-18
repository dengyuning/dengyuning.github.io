### 计算余弦相似度
import tensorflow as tf
import numpy as np

def cosine(q,a):
    pooled_len_1 = tf.sqrt(tf.reduce_sum(q * q, 1))
    pooled_len_2 = tf.sqrt(tf.reduce_sum(a * a, 1))
    pooled_mul_12 = tf.reduce_sum(q * a, 1)
    score = tf.div(pooled_mul_12, pooled_len_1 * pooled_len_2 +1e-8, name="scores")
    return score

a = np.array([[1,2,3],[1,3,5]],dtype=np.float32)
b = np.array([[2,4,6],[1,5,9]],dtype=np.float32)
a = tf.convert_to_tensor(a)
b = tf.convert_to_tensor(b)
c = cosine(a,b)
sess = tf.Session()
print(sess.run(c))
