import csv
import os
from datetime import datetime

LOG_FILE = 'exam_log.csv'

def add_log(total, correct, memo=''):
    rate = round(correct / total * 100)
    date = datetime.now().strftime('%Y-%m-%d')
    exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(['日付', '問題数', '正解数', '正解率', 'メモ'])
        writer.writerow([date, total, correct, str(rate) + '%', memo])
    print(f'{date} | {correct}/{total}問 | {rate}% | {memo}')
    print('記録しました')

def show_log():
    if not os.path.exists(LOG_FILE):
        print('記録がありません')
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

import sys
if len(sys.argv) == 1:
    show_log()
elif len(sys.argv) >= 3:
    memo = sys.argv[3] if len(sys.argv) > 3 else ''
    add_log(int(sys.argv[1]), int(sys.argv[2]), memo)
