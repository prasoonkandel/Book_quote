import os
from errno import EMEDIUMTYPE

import numpy as np
import pandas as pd
import requests

df = pd.read_csv("utils/quote.csv")
