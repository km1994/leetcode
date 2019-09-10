#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/23
@url：https:#leetcode-cn.com/classic/problems/lru-cache/description/
@desc:
    146. LRU缓存机制
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

    获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
    写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

    进阶:

    你是否可以在 O(1) 时间复杂度内完成这两种操作？

    示例:

    LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       # 返回  1
    cache.put(3, 3);    # 该操作会使得密钥 2 作废
    cache.get(2);       # 返回 -1 (未找到)
    cache.put(4, 4);    # 该操作会使得密钥 1 作废
    cache.get(1);       # 返回 -1 (未找到)
    cache.get(3);       # 返回  3
    cache.get(4);       # 返回  4
'''

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_capacity = capacity
        self.cache_key_sort_list = []
        self.cache_dict = {}

    def get(self, key):
        if key in self.cache_key_sort_list: 
            p = self.cache_key_sort_list.index(key)
            self.cache_key_sort_list.remove(key)
            self.cache_key_sort_list.append(key)
            return self.cache_dict[key]
        return -1

    def put(self, key, value):
        if key in self.cache_key_sort_list:
            p = self.cache_key_sort_list.index(key)
            self.cache_key_sort_list.remove(key)
            self.cache_key_sort_list.append(key)
            self.cache_dict[key] = value
        else:
            if self.last_capacity <= 0:
                self.cache_dict.pop(self.cache_key_sort_list[0])
                self.cache_key_sort_list.pop(0)
            else:
                self.last_capacity = self.last_capacity - 1
            
            self.cache_dict[key] = value
            self.cache_key_sort_list.append(key)
            

        print("self.cache_key_sort_list:{0}".format(self.cache_key_sort_list))
        print("self.cache_dict:{0}".format(self.cache_dict))



if __name__ == "__main__":

    print("--------1-------")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print("cache.get(1):{0}".format(cache.get(1)))       # 返回  1
    cache.put(3, 3)    # 该操作会使得密钥 2 作废
    print("cache.get(2):{0}".format(cache.get(2)))       # 返回 -1 (未找到)
    cache.put(4, 4)    # 该操作会使得密钥 1 作废
    print("cache.get(1):{0}".format(cache.get(1)))       # 返回 -1 (未找到)
    print("cache.get(3):{0}".format(cache.get(3)))       # 返回  3
    print("cache.get(4):{0}".format(cache.get(4)))       # 返回  4