
""" open 方法 """
filename = 'files/file1.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()
    print(contents)
    words = contents.split()
    num_words = len(words)
    print(num_words)