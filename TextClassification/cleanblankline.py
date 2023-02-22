# coding = utf-8
# 去空白行的操作
def clearBlankLine():
    file1 = open('./resources/cropus/comment_all1.txt', 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open('./resources/cropus/comment_all2.txt', 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()

