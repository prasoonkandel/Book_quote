import os
from errno import EMEDIUMTYPE

import fastembed
import numpy as np
import pandas as pd

model = fastembed.TextEmbedding()
df = pd.read_csv("utils/quote.csv")

df["embedding"] = list(model.embed(df["Quote"]))
