import tushare as ts
from config import TOKEN

ts.set_token('10b3efea157f9e882603569ff34375b9d710bff194a4b22932634d55')


# 获取tushare
def get_pro():
    ts.set_token(TOKEN)
    return ts.pro_api()