# -*- coding: utf-8 -*-
# @Author  : Jerry Wenjie Wu
# @Time    : 07/10/2024 14:19
from envtest import pandas_df_to_markdown

import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(pandas_df_to_markdown(df))