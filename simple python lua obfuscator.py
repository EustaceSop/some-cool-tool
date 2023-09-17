import tkinter as tk
from tkinter import filedialog
import random
import traceback
import datetime
import re

# 字母、数字和符号的混淆函数
def obfuscate_all_characters(lua_code):
    obfuscated_code = ''
    for char in lua_code:
        # 检查字符是否是字母、数字或一些常见符号
        if char.isalnum() or char in "!@#$%^&*()_-+=<>?/,. ":
            obfuscated_char = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?/,.') for _ in range(1))
            obfuscated_code += obfuscated_char
        else:
            # 对于不是字母、数字或常见符号的字符，保留原字符
            obfuscated_code += char
    return obfuscated_code

# 压缩 Lua 代码为一行
def minify_lua_code(lua_code):
    # 移除注释和换行符
    lua_code = re.sub(r'--.*', '', lua_code)
    lua_code = lua_code.replace('\n', '')
    lua_code = lua_code.replace('\r', '')
    return lua_code

try:
    # 打开文件选择对话框
    root = tk.Tk()
    root.withdraw()  # 隐藏 Tkinter 窗口
    input_file_path = filedialog.askopenfilename(title="选择 Lua 文件", filetypes=[("Lua 文件", "*.lua")])

    if not input_file_path:
        print("未选择文件。")
    else:
        try:
            # 尝试使用 'utf-8' 编码打开文件
            with open(input_file_path, "r", encoding="utf-8") as input_file:
                lua_code = input_file.read()
        except UnicodeDecodeError:
            # 如果 utf-8 编码失败，尝试 'gbk' 编码
            with open(input_file_path, "r", encoding="gbk") as input_file:
                lua_code = input_file.read()

        # 混淆 Lua 代码
        lua_code = obfuscate_all_characters(lua_code)

        # 压缩 Lua 代码为一行
        lua_code = minify_lua_code(lua_code)

        # 生成输出文件的路径
        output_file_path = input_file_path.replace(".lua", "_obfuscated.lua")

        # 将混淆后的 Lua 代码写入输出文件
        with open(output_file_path, "w") as output_file:
            output_file.write(lua_code)

        print(f"混淆和压缩完成，已保存为 {output_file_path}")

        # 等待用户按任意键后再退出
        input("按任意键继续...")

    # 关闭 Tkinter
    root.quit()
except Exception as e:
    # 当发生异常时，将错误信息写入 error_log.txt
    error_message = f"{datetime.datetime.now()}: {str(e)}\n"
    with open("error_log.txt", "a") as error_log_file:
        error_log_file.write(error_message)
    print(f"发生错误，已写入到 error_log.txt: {error_message}")
    input("按任意键继续...")
