import os
from xml.dom import minicompat


PATH = os.path.dirname(os.path.realpath(__file__))

DATA_PATH = '/home/adripinto/oskarknagg-implementation/few-shot/data'

EPSILON = 1e-8

if DATA_PATH is None:
    raise Exception('Configure your data folder location in config.py before continuing!')
