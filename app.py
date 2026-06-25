# fastmcp run app.py:app --transport http --port 8000
# 測試指令：fastmcp run (程式名稱):FastMCP物件變數名稱 --透過網路提供服務 --port
# 補充：如果以後遇到類似：command not found: xxx，但明明剛剛 pip install xxx 成功，可以先試：rehash

# MCP (Model Context Protocol) 開發、部署與調用
# 部署到 FastMCP Cloud 雲端服務
# 使用 Google Antigravity 測試
import matplotlib.pyplot as plt
import io # 處理內部資料轉換
from fastmcp import FastMCP
from fastmcp.utilities.types import Image
app=FastMCP("My MCP Server") # 透過FastMCP建立物件，包進變數app中

# 提供一個加法的工具
@app.tool # 裝飾器
def add(n1:int,n2:int)->int: # 明確定義輸入格式為整數，用箭頭符號定義回傳值也是整數
    """Add Two Numbers""" # FastMCP提供的：在工具函式中，用字串告訴AI Agent這個工具在做什麼。AI代理人會根據說明決定是否調用
    return n1+n2


# 開發圓餅圖工具
# 定義數字列表的輸入
# 使用Matplotlib套件繪製圓餅圖
# 使用image物件回傳圖片
@app.tool
def draw_pie_chart(numbers:list[int])->Image:
    """Draw Pie Chart"""
    plt.pie(numbers)
    buffer=io.BytesIO() # 內部緩衝：做資料轉換(位元組的輸入輸出)
    plt.savefig(buffer, format="png")
    return Image(data=buffer.getvalue(), format="png") #Image(data=位元組列表)，必須是byte-array, byte-list。buffer.getvalue()：取得buffer中的位元組列表



