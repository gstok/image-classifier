

import collections;
import tensorflow as TF;

d = collections.OrderedDict();

a = TF.gfile.Walk(".");
print a;
print "hello world";