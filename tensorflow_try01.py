Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
print (x)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print (x)
NameError: name 'x' is not defined
>>> print(1)
1
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, TensorFlow')
>>> sess = tf.Session()
>>> print(sess.run(hello))
b'Hello, TensorFlow'
>>> 
>>> node1 = tf.constant(3.0, tf.float32)
>>>  node1 = tf.constant(4.0) #also tf.float32 implicitly
 
SyntaxError: unexpected indent
>>> node2 = tf.constant(4.0) #also tf.float32 implicitly
>>> node3 = tf.add(node1, node2)
>>> print("node1:", node1, "node2", node2)
node1: Tensor("Const_1:0", shape=(), dtype=float32) node2 Tensor("Const_2:0", shape=(), dtype=float32)
>>> print(node3)
Tensor("Add:0", shape=(), dtype=float32)
>>> adder_node = a + b # + provides a shortcut for tf.add(a, b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    adder_node = a + b # + provides a shortcut for tf.add(a, b)
NameError: name 'a' is not defined
>>> adder_node = node1 + node2 # + provides a shortcut for tf.add(a, b)
>>> print(sess.run(adder_node, feed_dict={a: [1, 3], b: [2, 4]}))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(sess.run(adder_node, feed_dict={a: [1, 3], b: [2, 4]}))
NameError: name 'a' is not defined
>>> print(sess.run(adder_node, feed_dict={node1: [1, 3], node2: [2, 4]}))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(sess.run(adder_node, feed_dict={node1: [1, 3], node2: [2, 4]}))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 778, in run
    run_metadata_ptr)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 961, in _run
    % (np_val.shape, subfeed_t.name, str(subfeed_t.get_shape())))
ValueError: Cannot feed value of shape (2,) for Tensor 'Const_1:0', which has shape '()'
>>> a = tf.placeholder(tf.float32)
>>> b = tf.placeholder
>>> b = tf.pla
