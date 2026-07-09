from binascii import crc32
import string
import zipfile
from itertools import product

dic = string.printable
# dic = string.printable 作为 CRC32 暴力破解的字典


def CrackCrc(crc, min_len=1, max_len=6):
    """
    CRC32 碰撞爆破
    crc: 目标 CRC32 值
    min_len: 最小长度（默认 1）
    max_len: 最大长度（默认 6），设为 0 则自动递增直到找到
    """
    if max_len == 0:
        max_len = 999  # 自动模式，设一个安全上限

    total_tested = 0
    for length in range(min_len, max_len + 1):
        combos = len(dic) ** length
        print(f"  尝试长度={length}, 组合数={combos:,}...", end=" ", flush=True)

        for chars in product(dic, repeat=length):
            s = "".join(chars)
            total_tested += 1
            if total_tested % 1000000 == 0:  # 每 100 万次打印进度
                print(f"\n    已尝试 {total_tested:,} 次，当前: {s}", end="", flush=True)
            if crc == (crc32(bytes(s, "ascii")) & 0xffffffff):
                print(f"\n  找到! 共尝试 {total_tested:,} 次")
                return s
        print(f"\r  长度={length} 未找到")

    print(f"\n  未找到匹配内容（已尝试 {total_tested:,} 次，长度 {min_len}-{max_len}）")
    return None


def getcrc32(fname):
    l = []
    file = fname
    f = zipfile.ZipFile(file, 'r')
    global fileList
    fileList = f.namelist()
    print(fileList)
    # print (type(fileList))
    for filename in fileList:
        Fileinfo = f.getinfo(filename)
        # print(Fileinfo)
        crc = Fileinfo.CRC
        # print ('crc',crc)
        l.append(crc)
    return l


def main(filename=None, min_len=1, max_len=6):
    """
    filename: ZIP 文件路径
    min_len:  爆破最小长度
    max_len:  爆破最大长度，0 = 自动递增
    """
    l = getcrc32(filename)
    for i in range(len(l)):
        print(f"\n[{fileList[i]}] 的内容: ")
        result = CrackCrc(l[i], min_len=min_len, max_len=max_len)
        if result:
            print(f">>> {result}")
        else:
            print(f">>> 未找到")


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if not args:
        print("用法: python ZIPbaopo.py <zip文件> [最小长度] [最大长度]")
        print("示例: python ZIPbaopo.py test.zip")
        print("      python ZIPbaopo.py test.zip 3 6")
        print("      python ZIPbaopo.py test.zip 1 0   # 自动递增")
    else:
        filename = args[0]
        min_len = int(args[1]) if len(args) > 1 else 1
        max_len = int(args[2]) if len(args) > 2 else 6
        main(filename, min_len, max_len)