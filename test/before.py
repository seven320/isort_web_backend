# encoding:utf-8
import bisect  # bisect_left　これで二部探索の大小検索が行える
import collections
import copy
import fractions  # 最小公倍数などはこっち
import math
import random
import sys

import numpy as np

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))
