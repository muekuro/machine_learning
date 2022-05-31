import tensorflow as tf

# Tensor作成
string = tf.Variable("this is a string", tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)

# 配列、リスト
rank1_tensor = tf.Variable(["Test", "Ok", "Tim"], tf.string)
rank2_tensor = tf.Variable((["test", "ok"], ["test", "yes"]), tf.string)

print(tf.rank(rank1_tensor))
print(rank2_tensor.shape)

# 形状変え
tensor1 = tf.ones([1, 2, 3])
tensor2 = tf.reshape(tensor1, [2, 3, 1])
tensor3 = tf.reshape(tensor2, [3, -1])

print(tensor1)
print(tensor2)
print(tensor3)

# テスト
t = tf.zeros([5, 5, 5, 5])
print(t)
t = tf.reshape(t, [125, 5])
print(t)