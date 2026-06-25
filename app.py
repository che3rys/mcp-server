# fastmcp run app.py:app --transport http --port 8000
# 測試指令：fastmcp run (程式名稱):FastMCP物件變數名稱 --透過網路提供服務 --port
# 補充：如果以後遇到類似：command not found: xxx，但明明剛剛 pip install xxx 成功，可以先試：rehash

# MCP (Model Context Protocol) 開發、部署與調用

# 使用 FastMCP 開發伺服器程式
from fastmcp import FastMCP # 從 fastmcp 套件中，匯入 FastMCP 類別
app=FastMCP("My MCP Server") # 透過FastMCP建立物件，包進變數app中
# 提供一個加法的工具
@app.tool # 裝飾器
def add(n1:int,n2:int)->int: # 明確定義輸入格式為整數，用箭頭符號定義回傳值也是整數
    """Add Two Numbers""" # FastMCP提供的：在工具函式中，用字串告訴AI Agent這個工具在做什麼。AI代理人會根據說明決定是否調用
    return n1+n2

# 部署到 FastMCP Cloud 雲端服務

# 使用 Google Antigravity 測試


