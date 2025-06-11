from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

base_html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: Arial;
            margin: 0;
            background: #f9f9f9;
            display: flex;
            height: 100vh;
            overflow: hidden;
        }
        .sidebar {
            background: #333;
            color: white;
            height: 100vh;
            padding: 20px 10px 20px 10px;
            width: 60px; /* 收合時寬度 */
            transition: width 0.3s;
            box-sizing: border-box;
            position: relative;
        }
        .sidebar-content {
            margin-top: 60px; /* 讓內容往下移，避免被☰擋住 */
        }
        .sidebar.expanded {
            width: 200px; /* 展開寬度 */
        }
        .sidebar h2 {
            font-size: 1.2em;
            margin-bottom: 20px;
            white-space: nowrap;
            overflow: hidden;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .sidebar.expanded h2 {
            opacity: 1;
        }
        .sidebar a {
            display: block;
            color: white;
            text-decoration: none;
            margin: 15px 0;
            font-size: 18px;
            white-space: nowrap;
            overflow: hidden;
            opacity: 0;
            transition: opacity 0.3s;
            text-align: left;
            padding-left: 0;
        }
        .sidebar.expanded a {
            opacity: 1;
        }
        .sidebar details {
            opacity: 0;
            height: 0;
            overflow: hidden;
            transition: opacity 0.3s, height 0.3s;
        }
        .sidebar.expanded details {
            opacity: 1;
            height: auto;
        }
        .toggle-btn {
            position: absolute;
            top: 10px;
            left: 10px;
            background: #333;
            border-radius: 0;  /* 方形 */
            width: 40px;
            height: 40px;
            color: white;
            border: none;      /* 無框 */
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            user-select: none;
            z-index: 10;
            font-size: 20px;
        }
        .main {
            flex-grow: 1;
            padding: 40px;
            overflow-y: auto;
            transition: margin-left 0.3s;
            margin-left: 60px;
        }
        .main.expanded {
            margin-left: 200px;
        }
    </style>
</head>
<body>
    <div id="sidebar" class="sidebar">
        <div class="toggle-btn" onclick="toggleSidebar()" title="切換選單">☰</div>
        <div class="sidebar-content">
            <h2>選單</h2>
            <details>
                <summary>I. 時間管理與專注</summary>
                <!-- 之後將功能連結放這裡 -->
            </details>
            <details>
                <summary>II. 任務與專案管理</summary>
            </details>
            <details>
                <summary>III. 目標與習慣養成</summary>
            </details>
            <details>
                <summary>IV. 日程與提醒</summary>
            </details>
            <details>
                <summary>V. 分析與回顧</summary>
            </details>
            <details>
                <summary>VI. 社群與激勵</summary>
            </details>
            <details>
                <summary>VII. 健康與生活平衡</summary>
            </details>
            <details>
                <summary>VIII. 知識與輔助</summary>
            </details>
        </div>
    </div>
    <div id="main" class="main">
        {{ content|safe }}
    </div>
<script>
    function toggleSidebar() {
        const sidebar = document.getElementById('sidebar');
        const main = document.getElementById('main');
        sidebar.classList.toggle('expanded');
        main.classList.toggle('expanded');
    }
</script>
</body>
</html>
'''

@app.route('/')
def index():
    content = "<h1>歡迎使用自律系統</h1><p>請從左側分類選擇功能。</p>"
    return render_template_string(base_html, title="自律系統", content=content)

if __name__ == '__main__':
    app.run(debug=True)
