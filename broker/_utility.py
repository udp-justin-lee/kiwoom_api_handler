

def readTxt(path):
    ''' read txt from a file '''

    # line by line으로 txt파일을 읽는 함수입니다.
    with open(path, 'r') as f:
        lines = f.readlines()

        if len(lines) == 1:
            return lines[0]

        return [l.replace('\n', '') for l in lines]

def saveTxt(x, path):
    ''' save given string or list of strings to filepath

    params
    =============================
    x: str or list, list of str
    path: str, file path
    '''

    # list에 속한 원소(str)들을 line by line으로 저장합니다.
    with open(path, 'w') as f:
        if isinstance(x, list):
            for i in x:
                f.write('%s\n'%i)
        else:
            f.write(str(x))

def str2int(x):
    return int(x.replace('+', '').replace('-', ''))

def str2float(x):
    return float(x.replace('+', ''))

def removeSign(x):
    return x.replace('+', '').replace('-', '').replace(',', '')
