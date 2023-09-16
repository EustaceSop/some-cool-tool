import tkinter as tk
from tkinter import filedialog
import random
import traceback
import datetime
import re

# Obfuscated function names
def obfuscate_function_names(lua_code):
    functions = re.findall(r'function\s+(\w+)', lua_code)
    for func_name in functions:
        obfuscated_name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(len(func_name)))
        lua_code = lua_code.replace(func_name, obfuscated_name)
    return lua_code

# Obfuscated variable names
def obfuscate_variable_names(lua_code):
    variables = re.findall(r'\blocal\s+(\w+)', lua_code)
    for var_name in variables:
        obfuscated_name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(len(var_name)))
        lua_code = lua_code.replace(var_name, obfuscated_name)
    return lua_code

# Compress Lua code into one line
def minify_lua_code(lua_code):
    # Remove comments and line breaks
    lua_code = re.sub(r'--.*', '', lua_code)
    lua_code = lua_code.replace('\n', '')
    lua_code = lua_code.replace('\r', '')

    return lua_code

try:
    # Open file selection dialog
    root = tk.Tk()
    root.withdraw()  # Hide Tkinter window
    input_file_path = filedialog.askopenfilename(title="选择 Lua 文件", filetypes=[("Lua file", "*.lua")])

    if not input_file_path:
        print("No file selected.")
    else:
        # Reading Lua input files
        with open(input_file_path, "r") as input_file:
            lua_code = input_file.read()

        # Obfuscating Lua code
        lua_code = obfuscate_function_names(lua_code)
        lua_code = obfuscate_variable_names(lua_code)

        # Compress Lua code into one line
        lua_code = minify_lua_code(lua_code)

        # Path to generate output file
        output_file_path = input_file_path.replace(".lua", "_obfuscated.lua")

        # Write obfuscated and compressed Lua code to output file
        with open(output_file_path, "w") as output_file:
            output_file.write(lua_code)

        print(f"Obfuscation and compression completed, saved as {output_file_path}")

        # Wait for the user to press any key before exiting
        input("Press any key to continue...")

    # Close Tkinter
    root.quit()
except Exception as e:
    # Write error message when exception occurs
    error_message = f"{datetime.datetime.now()}: {str(e)}\n"
    with open("error_log.txt", "a") as error_log_file:
        error_log_file.write(error_message)
    print(f"An error occurred and was written to error_log.txt: {error_message}")
    input("Press any key to continue...")
