from binascii import crc32
import string
import zipfile

dic = string.printable


def CrackCrc(crc):
    for i in dic:
        # print (i)
        for j in dic:
            for p in dic:
                for q in dic:
                    s = i + j + p + q
                    # print (crc32(bytes(s,'ascii')) & 0xffffffff)
                    if crc == (crc32(bytes(s, 'ascii')) & 0xffffffff):
                        print(s)
                        return

def getcrc32(fname):
    l = []
    file = fname
    f = zipfile.ZipFile(file, 'r')  # 以只读方式打开 ZIP 文件，返回 ZipFile 对象
# 'r' 只读，文件必须存在 'w' 写入，覆盖已有文件 'a' 追加到已有 ZIP 'x' 创建新 ZIP，已存在则报错
    global fileList #这里是将其声明为全局变量,便于再main（）方法调用
    fileList = f.namelist()  # 返回 ZIP 中所有文件名列表，如 ["flag.txt", "key.txt"]
    print(fileList)
    # print (type(fileList))
    for filename in fileList:
        Fileinfo = f.getinfo(filename) # 通过前面获得的Zipile对象，获取他携带的信息，信息内包含CRC
        # print(Fileinfo)
        crc = Fileinfo.CRC
        # print ('crc',crc)
        l.append(crc)  # 把crc写入数组并返回
    return l


def main(filename=None):
    l = getcrc32(filename)
    # print(l)
    for i in range(len(l)):
        print(fileList[i], end='的内容是:')
        print(f"此时l[i]的值是: {l[i]}")
        CrackCrc(l[i])


if __name__ == "__main__":
    main('00000075.zip')