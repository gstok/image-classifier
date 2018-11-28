#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections;
import tensorflow as tf;
import os;
import re;
import argparse;
import sys;

# TF.logging.info("你好，世界");

# print(os.path.basename("/usr/lib/bin/hhss.txt"))
# print(re.sub(r'[^a-z0-9]+', ' ', '鸟，世界s12'));

FLAGS = None;


def main(_):
    print("你好，世界");
    print(FLAGS.image_dir);
    k = tf.compat.as_bytes("1234");
    print(k);


if __name__ == '__main__':
    parser = argparse.ArgumentParser();
    parser.add_argument(
        "--image_dir",
        type = str,
        default = "",
        help = "图片文件夹路径"
    )
    FLAGS, unparsed = parser.parse_known_args();
    tf.app.run(main = main, argv = [sys.argv[0]] + unparsed);





# d = collections.OrderedDict();

# result = TF.gfile.Walk("./dirtest");
# for item in result:
#     print(item);

# list = sorted(set(os.path.normcase(ext) for ext in ['JPEG', 'JPG', 'jpeg', 'jpg']))

# inList = ["1", "3", "55", "54", "2", "2"];
# kkk = (jj + "jjj" for jj in inList);
# ssss = sorted(kkk);
# print(ssss);

# print(os.path.basename("/usr/local"))

# mySet = set(inList);
# outList = sorted(mySet)

# print(outList);

# print(list);
# print(list2);

# print(a);
# print("你好，世界");
# list = ["1", "12", "34"];
# print(list);
# for name in list:
#     print(name);
# flag = False;
# if flag:
#     print("真");
# else:
#     print("假的");
# num = 21;
# if num < 10:
#     print("第一个");
# elif num < 20:
#     print("第二个");
# elif num < 30:
#     print("第三个");
# else:
#     print("其他的");