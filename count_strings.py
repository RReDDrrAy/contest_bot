import os
import codecs
from pathlib import Path

total_lines = 0
total_chars = 0
total_files = 0
file_name = []


for root, dirs, files in os.walk(Path('./app')):
    for file in files:
        if file.endswith('.py'):
            total_files += 1
            file_name.append(file)
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                lines = f.readlines()
                total_lines += len(lines)
                for line in lines:
                    total_chars += len(line)

print(f'Всего строк: {total_lines}')
print(f'Всего символов: {total_chars}\n'
      f'Всего файлов.py: {total_files}\n'
      f'{file_name}')