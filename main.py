import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '一列目': [1,2,3,4],
    '二列目': [10,20,30,40]  
})

#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0), height=200, width=200)

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c'] 
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)


df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69, 139.70],
    columns=['lat','lon'] 
)

st.map(df)

st.write('Display Image')

# if st.checkbox('Show Image'):
#     img = Image.open('test.PNG')
#     st.image(img, caption='LPSC conference', use_column_width=True)

st.write('プレグレスバー')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)