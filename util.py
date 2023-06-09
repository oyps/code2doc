import os, random, re


def str_blocks(text: str, block_len: int = 300, step_len: int = 300) -> list:
    '''字符串跳跃分块

    从多行字符串中，每次取 block_len 行，然后跳过 step_len 行，循环如此

    参数列表
    ----------
    text : str
        被提取的多行字符串
    block_len : int, 可选
        每次取的行数, 默认值 300
    step_len : int, 可选
        每次跳过的行数, 默认值 300

    返回值
    -------
    list
        提取到的块列表，每个块中是 block_len 行字符串
    '''
    lines = text.splitlines()
    i = 0
    blocks = []
    while True:
        item: str = lines[i : i + block_len]
        i += block_len + step_len
        if not item:
            break
        blocks.append('\n'.join(item))
    return blocks


def dirlist(path, allfile):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            if not filename.startswith('.') and filename not in ['node_modules']:
                dirlist(filepath, allfile)
        else:
            if filepath.split('.')[-1] in [
                'js',
                'php',
                'html',
                'css',
                'txt',
                'c',
                'cpp',
                'java',
                'py',
            ]:
                allfile.append(filepath)
    return allfile


def get_all_code(path: str) -> str:
    '''提取文件夹中的所有代码
    :param path: 文件夹路径
    '''
    text = ''
    fileList = dirlist(path, [])
    random.shuffle(fileList)
    for i in fileList:
        f = open(i, 'r', encoding='utf-8')
        text += f.read() + '\n'
    text = re.sub(' {2,}', '', text)
    text = re.sub('\n+', '\n', text)
    text = re.sub('(\n\s*){2,}', '\n', text)
    open('allCode', 'w', encoding='utf-8').write(text)
    return text
