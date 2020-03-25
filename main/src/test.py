import os,re
import math
import copy
import time

import numpy as np
from PIL import Image
import cv2
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, models
from torch.optim import lr_scheduler
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import logging

from PIL import Image

import pandas as pd
import numpy as np

# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

from tqdm import tqdm_notebook as tqdm
import glob

#scikit-image

from skimage import data
from skimage.transform import resize # float64　, float32のみ

import shape_commentator

%matplotlib inline

from statistics import mean

pd.set_option('display.max_rows', 100)
