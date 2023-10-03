import os
import time
import shutil
import pathlib

try:
    os.makedirs("CS")
except FileExistsError:
    pass

with open('homework.txt', 'w') as file :
    file.write("4112029004_王定軒")

content = open('homework.txt', 'r')

file_content = content.read()

print(f"檔案內容為：{file_content}")

file_size = os.path.getsize('homework.txt')
print(f"文件大小：{file_size}字節")

file_time = os.path.getmtime("homework.txt")
print(f"最後修改時間：{file_time}")

file_formatted_time = time.ctime(file_time)

print(f"最後修改時間（人類可讀格式):{file_formatted_time}")

shutil.move('homework.txt', 'CS')

shutil.rmtree("CS", ignore_errors= True)










