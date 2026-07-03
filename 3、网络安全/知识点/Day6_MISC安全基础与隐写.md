# 第六天：MISC安全基础与隐写（一）（二）

---

## 学习目标

- 了解MISC题目类型和解题思路
- 掌握常见编码解码技术
- 学会压缩包破解技术
- 掌握图片隐写技术
- 学会流量分析技术
- 掌握音频隐写技术

---

## 一、MISC杂项介绍及信息收集

### 1.1 MISC题目类型

**MISC常见题型：**
```
1. 编码解码
   - Base64、Base32、Base16
   - URL编码、HTML编码
   - Unicode编码
   - 自定义编码

2. 隐写术
   - 图片隐写
   - 音频隐写
   - 视频隐写
   - 文档隐写

3. 流量分析
   - HTTP流量
   - DNS流量
   - ICMP流量
   - USB流量

4. 文件分析
   - 文件头分析
   - 文件修复
   - 文件分离
   - 文件恢复

5. 压缩包分析
   - 密码破解
   - 伪加密
   - CRC32爆破
   - 明文攻击
```

### 1.2 信息收集方法

**文件类型识别：**
```bash
# file命令
file mystery_file
file -b mystery_file

# 十六进制查看
xxd mystery_file | head -20
hexdump -C mystery_file | head -20

# binwalk分析
binwalk mystery_file
binwalk -e mystery_file

# foremost文件分离
foremost mystery_file
```

**文件头常见类型：**
```
JPEG: FF D8 FF
PNG:  89 50 4E 47
GIF:  47 49 46 38
BMP:  42 4D
ZIP:  50 4B 03 04
RAR:  52 61 72 21
7z:   37 7A BC AF
PDF:  25 50 44 46
```

---

## 二、常见编码解码及实战题分析

### 2.1 Base64编码

**Base64特点：**
```
- 由A-Z、a-z、0-9、+、/组成
- 长度是4的倍数
- 末尾可能有1-2个=号
```

**Base64编码解码：**
```bash
# 命令行
echo "Hello" | base64
echo "SGVsbG8=" | base64 -d

# Python
import base64
encoded = base64.b64encode(b"Hello")
decoded = base64.b64decode(encoded)
```

**Base64变种：**
```
Base64URL：使用-和_替代+和/
Base58：不使用0、O、I、l和+、/
Base32：使用A-Z和2-7
Base16：使用0-9和A-F（十六进制）
```

### 2.2 URL编码

**URL编码规则：**
```
- 使用%加两位十六进制数
- 空格编码为%20或+
- 特殊字符需要编码
```

**常见URL编码：**
```
空格：%20 或 +
<：%3C
>：%3E
"：%22
'：%27
&：%26
=：%3D
?：%3F
/：%2F
```

**URL解码：**
```bash
# Python
from urllib.parse import unquote
decoded = unquote("%E4%BD%A0%E5%A5%BD")

# 在线工具
# https://www.urldecoder.org
```

### 2.3 HTML编码

**HTML实体编码：**
```
<：&lt; 或 &#60;
>：&gt; 或 &#62;
&：&amp; 或 &#38;
"：&quot; 或 &#34;
'：&#39;
空格：&nbsp; 或 &#160;
```

**HTML解码：**
```bash
# Python
from html import unescape
decoded = unescape("&lt;script&gt;")
```

### 2.4 Unicode编码

**Unicode编码格式：**
```
\uXXXX：Unicode转义
&#XXXX;：HTML实体
U+XXXX：Unicode表示
```

**Unicode解码：**
```bash
# Python
decoded = "你好"
print(decoded)  # 你好
```

### 2.5 其他编码

**摩尔斯电码：**
```
A: .-      B: -...    C: -.-.
D: -..     E: .       F: ..-.
G: --.     H: ....    I: ..
J: .---    K: -.-     L: .-..
M: --      N: -.      O: ---
P: .--.    Q: --.-    R: .-.
S: ...     T: -       U: ..-
V: ...-    W: .--     X: -..-
Y: -.--    Z: --..

0: -----   1: .----   2: ..---
3: ...--   4: ....-   5: .....
6: -....   7: --...   8: ---..
9: ----.
```

**培根密码：**
```
每个字母用5个二进制表示
A: AAAAA   B: AAAAB   C: AAABA
D: AAABB   E: AABAA   F: AABAB
G: AABBA   H: AABBB   I: ABAAA
J: ABAAB   K: ABABA   L: ABABB
M: ABBAA   N: ABBAB   O: ABBBA
P: ABBBB   Q: BAAAA   R: BAAAB
S: BAABA   T: BAABB   U: BABAA
V: BABAB   W: BABBA   X: BABBB
Y: BBAAA   Z: BBAAB
```

---

## 三、压缩包密码爆破、伪加密、CRC32爆破

### 3.1 压缩包加密原理

**ZIP加密方式：**
```
- ZipCrypto：传统加密，安全性低
- AES-128/256：强加密，安全性高
```

**RAR加密方式：**
```
- AES-128/256加密
- 固有加密
```

### 3.2 密码爆破

**工具使用：**
```bash
# fcrackzip（ZIP爆破）
fcrackzip -u -D -p passwords.txt file.zip
fcrackzip -u -c a -l 1-4 file.zip

# rar2john + john（RAR爆破）
rar2john file.rar > hash.txt
john hash.txt --wordlist=passwords.txt

# hashcat（GPU加速）
zip2john file.zip > hash.txt
hashcat -m 17200 hash.txt passwords.txt
```

**常用字典：**
```bash
# Kali Linux字典
/usr/share/wordlists/rockyou.txt
/usr/share/wordlists/dirb/common.txt

# 自定义字典
# 使用crunch生成
crunch 4 4 0123456789 -o dict.txt
```

### 3.3 伪加密

**伪加密原理：**
```
ZIP文件中有一个加密标志位
修改这个标志位可以伪装成加密
实际并未加密，可以直接解压
```

**识别伪加密：**
```bash
# 使用010 Editor查看
# 搜索 50 4B 03 04
# 查看加密标志位

# 正常未加密：00 00
# 加密：00 01 或 09 00
# 伪加密：00 01 但实际未加密
```

**破解伪加密：**
```bash
# 方法1：修改标志位
# 使用010 Editor将09 00改为00 00

# 方法2：使用工具
# ZipCenOp
java -jar ZipCenOp.jar e file.zip

# 方法3：直接尝试解压
# 部分解压软件可以忽略加密标志
```

### 3.4 CRC32爆破

**CRC32原理：**
```
- CRC32是循环冗余校验
- 生成32位校验值
- 用于验证数据完整性
```

**CRC32爆破条件：**
```
- 文件内容很短（1-6字节）
- 已知CRC32值
- 可以暴力枚举所有可能
```

**CRC32爆破工具：**
```bash
# CRC32爆破脚本
# Python实现
import binascii
import itertools
import string

def crc32_brute(target_crc, length):
    chars = string.printable
    for combo in itertools.product(chars, repeat=length):
        text = ''.join(combo)
        if binascii.crc32(text.encode()) & 0xffffffff == target_crc:
            return text
    return None

# 使用方法
target_crc = 0x12345678
result = crc32_brute(target_crc, 4)
print(result)
```

---

## 四、流量分析、图片隐写、二维码、LSB加密

### 4.1 流量分析基础

**Wireshark过滤器：**
```
# IP过滤
ip.addr == 192.168.1.1
ip.src == 192.168.1.1
ip.dst == 192.168.1.1

# 协议过滤
http
dns
tcp
udp
icmp

# 端口过滤
tcp.port == 80
tcp.dstport == 443

# 内容过滤
http contains "flag"
tcp contains "flag"
```

**HTTP流量分析：**
```
1. 查看请求URL
2. 查看请求参数
3. 查看响应内容
4. 查看Cookie信息
5. 查看文件传输
```

**DNS流量分析：**
```
1. 查询域名
2. 响应IP地址
3. 子域名信息
4. DNS隧道检测
```

**ICMP流量分析：**
```
1. ping请求响应
2. 数据长度
3. 数据内容
4. ICMP隧道检测
```

### 4.2 图片隐写技术

**常见图片隐写方法：**

**文件头隐写：**
```bash
# 在图片末尾添加数据
# 使用binwalk检测
binwalk image.jpg
binwalk -e image.jpg

# 使用foremost分离
foremost image.jpg
```

**EXIF信息隐写：**
```bash
# 查看EXIF信息
exiftool image.jpg

# 修改EXIF信息
exiftool -Comment="secret message" image.jpg

# 清除EXIF信息
exiftool -all= image.jpg
```

**LSB隐写：**
```
Least Significant Bit - 最低有效位
修改像素的最低位来隐藏数据
视觉上无法察觉
```

**LSB隐写工具：**
```bash
# Stegsolve
# 下载：https://www.caesum.com/handbook/Stegsolve.jar
java -jar Stegsolve.jar

# 功能：
# - 查看各个位平面
# - 提取LSB数据
# - 图片对比
# - 数据提取

# zsteg（PNG/BMP）
zsteg image.png
zsteg -a image.png

# stegdetect（JPEG）
stegdetect image.jpg
steghide extract -sf image.jpg
```

**图片隐写实操：**
```bash
# 使用Stegsolve分析图片
1. 打开Stegsolve
2. 加载图片
3. 切换位平面（左右箭头）
4. 观察异常位平面
5. 提取隐藏数据

# 使用zsteg分析PNG
zsteg secret.png
zsteg -a secret.png
zsteg -b 1 secret.png
```

### 4.3 二维码隐写

**二维码结构：**
```
- 定位图案：三个角落的方块
- 对齐图案：用于校正
- 数据区域：存储数据
- 纠错级别：L/M/Q/H
```

**二维码识别工具：**
```bash
# zbarimg
zbarimg qrcode.png

# Python
from pyzbar.pyzbar import decode
from PIL import Image
img = Image.open('qrcode.png')
result = decode(img)
print(result[0].data.decode())
```

**二维码修复：**
```
1. 定位图案损坏
   - 手动修复定位图案
   - 使用PS或其他工具

2. 数据区域损坏
   - 使用纠错恢复
   - 尝试不同扫描角度

3. 二维码变形
   - 使用图像处理工具校正
   - 调整对比度和亮度
```

### 4.4 LSB加密实操

**LSB嵌入数据：**
```python
from PIL import Image

def lsb_embed(image_path, message, output_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    # 将消息转换为二进制
    binary = ''.join(format(ord(c), '08b') for c in message)
    binary += '00000000'  # 结束标记
    
    # 嵌入数据
    idx = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if idx < len(binary):
                r, g, b = pixels[i, j]
                r = (r & 0xFE) | int(binary[idx])
                pixels[i, j] = (r, g, b)
                idx += 1
    
    img.save(output_path)

# 使用
lsb_embed('original.png', 'flag{test}', 'secret.png')
```

**LSB提取数据：**
```python
from PIL import Image

def lsb_extract(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    binary = ''
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            binary += str(r & 1)
    
    # 提取字符
    message = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if byte == '00000000':
            break
        message += chr(int(byte, 2))
    
    return message

# 使用
message = lsb_extract('secret.png')
print(message)
```

---

## 五、图片结构分析、压缩包题型综合分析

### 5.1 图片文件结构分析

**PNG文件结构：**
```
文件头：89 50 4E 47 0D 0A 1A 0A
数据块：
  IHDR：图像头信息
  PLTE：调色板
  IDAT：图像数据
  IEND：图像结束
```

**JPEG文件结构：**
```
文件头：FF D8 FF
标记段：
  SOI：FF D8（开始）
  APP0：FF E0
  DQT：FF DB
  SOF：FF C0
  DHT：FF C4
  SOS：FF DA
  EOI：FF D9（结束）
```

**GIF文件结构：**
```
文件头：47 49 46 38 39 61
数据块：
  逻辑屏幕描述符
  全局颜色表
  图像描述符
  局部颜色表
  图像数据
  扩展块
  结束块：3B
```

### 5.2 图片修复

**文件头修复：**
```bash
# 使用010 Editor
# 手动添加正确的文件头

# JPEG文件头
FF D8 FF E0 00 10 4A 46 49 46 00 01

# PNG文件头
89 50 4E 47 0D 0A 1A 0A
```

**CRC32修复：**
```bash
# PNG使用CRC32校验
# 可以使用工具修复
# pngcheck检查
pngcheck image.png

# pngfix修复
pngfix image.png
```

### 5.3 压缩包题型综合分析

**明文攻击：**
```
条件：
- 知道压缩包中某个文件的部分内容
- 使用相同压缩算法

工具：
- Advanced Archive Password Recovery (ARCHPR)
- bkcrack
```

**明文攻击实操：**
```bash
# 使用bkcrack
# 安装
git clone https://github.com/kimci86/bkcrack.git
cd bkcrack
cmake -S . -B build
cmake --build build

# 使用
bkcrack -C encrypted.zip -c target.txt -p plaintext.txt

# 获取密钥后解密
bkcrack -C encrypted.zip -k KEY1 KEY2 KEY3 -U unlocked.zip ""
```

**已知明文攻击：**
```python
# Python实现
import zipfile

def known_plaintext_attack(zip_file, known_file, known_content):
    with zipfile.ZipFile(zip_file) as zf:
        # 读取加密文件
        with zf.open(known_file) as f:
            encrypted = f.read()
        
        # 尝试解密
        # ...
```

---

## 六、SSTV、DTMF、音频隐写

### 6.1 SSTV慢扫描电视

**SSTV原理：**
```
- 将图片转换为音频信号
- 通过无线电传输
- 接收端解码还原图片
```

**SSTV解码工具：**
```bash
# QSSTV（Linux）
qsstv

# RX-SSTV（Windows）
# 下载：https://www.qsl.net/on6mu/rxsstv.htm

# Python实现
# pip install pysstv
from pysstv.sstv import SSTV

with open('sstv.wav', 'rb') as f:
    sstv = SSTV.from_file(f)
    sstv.write_image('output.png')
```

### 6.2 DTMF拨号音

**DTMF原理：**
```
- 双音多频
- 由高频和低频组合
- 用于电话拨号
```

**DTMF频率：**
```
       1209Hz 1336Hz 1477Hz 1633Hz
697Hz    1      2      3      A
770Hz    4      5      6      B
852Hz    7      8      9      C
941Hz    *      0      #      D
```

**DTMF解码工具：**
```bash
# multimon-ng
multimon-ng -t wav -a DTMF audio.wav

# Python
# pip install dtmf
import dtmf

with open('audio.wav', 'rb') as f:
    data = f.read()
    tones = dtmf.decode(data)
    print(tones)
```

### 6.3 MP3Stego

**MP3Stego原理：**
```
- 在MP3文件中隐藏数据
- 利用MP3编码的冗余
- 不影响音频质量
```

**MP3Stego使用：**
```bash
# 下载：https://www.petitcolas.net/steganography/mp3stego/

# 隐藏数据
encode -E secret.txt -P password input.wav output.mp3

# 提取数据
decode -X -P password output.mp3
```

### 6.4 音频频谱分析

**使用Audacity分析：**
```
1. 打开Audacity
2. 导入音频文件
3. 查看频谱图
4. 识别异常频率
5. 分析隐藏信息
```

**频谱隐写类型：**
```
1. 文字隐写
   - 在特定频率显示文字
   - 需要切换频谱视图

2. 图片隐写
   - 在频谱中嵌入图片
   - 需要合适的频谱设置

3. 摩尔斯电码
   - 以声音形式编码
   - 需要分析节奏
```

### 6.5 波形分析

**波形图分析：**
```
1. 振幅分析
   - 高振幅：1
   - 低振幅：0
   - 转换为二进制

2. 频率分析
   - 不同频率表示不同信息
   - 需要频率解调

3. 时域分析
   - 分析时间序列
   - 识别编码模式
```

**左右声道分析：**
```python
from pydub import AudioSegment

# 加载音频
audio = AudioSegment.from_wav("audio.wav")

# 分离声道
left = audio.split_to_mono()[0]
right = audio.split_to_mono()[1]

# 声道相减
diff = left.overlay(right.invert_phase())

# 导出
diff.export("diff.wav", format="wav")
```

---

## 七、pyc隐写、pdf隐写、word/excel隐写

### 7.1 pyc隐写

**pyc文件结构：**
```
- Python字节码文件
- 由Python源码编译生成
- 包含魔数、时间戳、代码对象
```

**pyc分析工具：**
```bash
# uncompyle6（反编译）
pip install uncompyle6
uncompyle6 file.pyc

# pycdc（反编译）
pycdc file.pyc

# dis模块（反汇编）
python -c "import dis; import importlib; mod = importlib.import_module('file'); dis.dis(mod)"
```

**pyc隐写方法：**
```
1. 在常量池中隐藏数据
2. 修改代码对象属性
3. 添加注释信息
4. 利用魔数字段
```

### 7.2 PDF隐写

**PDF文件结构：**
```
- 文件头：%PDF-1.x
- 对象体：包含文本、图片等
- 交叉引用表：对象位置
- 文件尾：startxref
```

**PDF隐写方法：**
```
1. 隐藏文本
   - 使用白色字体
   - 覆盖在图片上
   - 使用极小字体

2. 隐藏文件
   - 嵌入附件
   - 使用JavaScript
   - 利用注释

3. 隐藏层
   - 使用OCG层
   - 可见性控制
```

**PDF分析工具：**
```bash
# pdf-parser
pdf-parser.py file.pdf

# pdfid
pdfid.py file.pdf

# peepdf
peepdf file.pdf

# Python
import PyPDF2
reader = PyPDF2.PdfReader("file.pdf")
for page in reader.pages:
    print(page.extract_text())
```

### 7.3 Word/Excel隐写

**Word隐写方法：**
```
1. 隐藏文本
   - 字体颜色与背景相同
   - 使用隐藏文字属性
   - 极小字体

2. 隐藏图片
   - 裁剪图片隐藏内容
   - 使用图层覆盖
   - 修改透明度

3. 隐藏文件
   - 嵌入OLE对象
   - 使用宏代码
   - 修改文档属性
```

**Excel隐写方法：**
```
1. 隐藏工作表
   - 隐藏行/列
   - 隐藏工作表
   - 使用白色字体

2. 隐藏数据
   - 使用条件格式
   - 数据验证隐藏
   - 公式隐藏
```

**Office分析工具：**
```bash
# oletools
pip install oletools
olevba file.docx
oleid file.docx
olemap file.docx

# python-docx
from docx import Document
doc = Document("file.docx")
for para in doc.paragraphs:
    print(para.text)
```

---

## 八、盲水印、Python处理图片

### 8.1 盲水印

**盲水印原理：**
```
- 不需要原图即可提取
- 利用频域变换
- 鲁棒性强
```

**盲水印工具：**
```bash
# blind-watermark
pip install blind-watermark

# 嵌入水印
bwm embed --image original.png --watermark secret.png --output watermarked.png

# 提取水印
bwm decode --image watermarked.png --output extracted.png

# 频域方法
# 使用DWT/DCT变换
```

### 8.2 Python处理图片

**PIL/Pillow库：**
```python
from PIL import Image

# 打开图片
img = Image.open("image.png")

# 获取图片信息
print(img.size)  # 尺寸
print(img.mode)  # 模式（RGB/RGBA等）
print(img.format)  # 格式

# 获取像素
pixel = img.getpixel((x, y))
print(pixel)  # (R, G, B)

# 修改像素
img.putpixel((x, y), (255, 0, 0))

# 保存图片
img.save("output.png")
```

**图片处理示例：**
```python
from PIL import Image, ImageEnhance, ImageFilter

# 调整亮度
enhancer = ImageEnhance.Brightness(img)
img_bright = enhancer.enhance(1.5)

# 调整对比度
enhancer = ImageEnhance.Contrast(img)
img_contrast = enhancer.enhance(2.0)

# 应用滤镜
img_blur = img.filter(ImageFilter.BLUR)
img_edge = img.filter(ImageFilter.FIND_EDGES)

# 图片旋转
img_rotate = img.rotate(45)

# 图片翻转
img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
```

**图片分离RGB通道：**
```python
from PIL import Image

img = Image.open("image.png")
r, g, b = img.split()

# 查看单个通道
r.show()
g.show()
b.show()

# 保存单个通道
r.save("red.png")
g.save("green.png")
b.save("blue.png")
```

---

## 九、Wireshark流量分析进阶

### 9.1 鼠标流量分析

**鼠标流量特征：**
```
- USB HID协议
- 数据长度：4字节
- 包含按键状态和移动信息
```

**鼠标流量分析：**
```python
# 使用tshark提取鼠标数据
import subprocess

cmd = "tshark -r capture.pcap -Y 'usb.transfer_type==0x01 && frame.len==72' -T fields -e usb.capdata"
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

# 解析鼠标数据
for line in result.stdout.strip().split('\n'):
    if line:
        data = bytes.fromhex(line.replace(':', ''))
        dx = data[1] if data[1] < 128 else data[1] - 256
        dy = data[2] if data[2] < 128 else data[2] - 256
        print(f"dx={dx}, dy={dy}")
```

### 9.2 键盘流量分析

**键盘流量特征：**
```
- USB HID协议
- 数据长度：8字节
- 包含按键码
```

**键盘流量分析：**
```python
# USB键盘键码映射
KEY_MAP = {
    0x04: 'a', 0x05: 'b', 0x06: 'c',
    0x07: 'd', 0x08: 'e', 0x09: 'f',
    0x0A: 'g', 0x0B: 'h', 0x0C: 'i',
    0x0D: 'j', 0x0E: 'k', 0x0F: 'l',
    0x10: 'm', 0x11: 'n', 0x12: 'o',
    0x13: 'p', 0x14: 'q', 0x15: 'r',
    0x16: 's', 0x17: 't', 0x18: 'u',
    0x19: 'v', 0x1A: 'w', 0x1B: 'x',
    0x1C: 'y', 0x1D: 'z', 0x1E: '1',
    0x1F: '2', 0x20: '3', 0x21: '4',
    0x22: '5', 0x23: '6', 0x24: '7',
    0x25: '8', 0x26: '9', 0x27: '0',
    0x28: '\n', 0x2C: ' ', 0x2D: '-',
    0x2E: '=', 0x2F: '[', 0x30: ']',
    0x33: ';', 0x34: "'", 0x36: ',',
    0x37: '.', 0x38: '/'
}

# 使用tshark提取键盘数据
import subprocess

cmd = "tshark -r capture.pcap -Y 'usb.transfer_type==0x01 && frame.len==72' -T fields -e usb.capdata"
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

# 解析键盘数据
for line in result.stdout.strip().split('\n'):
    if line:
        data = bytes.fromhex(line.replace(':', ''))
        key = data[2]
        if key in KEY_MAP:
            print(KEY_MAP[key], end='')
```

### 9.3 Web扫描流量识别

**扫描流量特征：**
```
- 短时间内大量请求
- 请求路径规律
- User-Agent异常
- 响应状态码分布
```

**识别扫描流量：**
```
# Wireshark过滤器
http.request.method == "GET"
http.response.code == 404

# 分析请求频率
Statistics -> Conversations -> HTTP
```

### 9.4 蚁剑/冰蝎/哥斯拉流量特征

**蚁剑流量特征：**
```
- 请求体包含@ini_set
- 使用base64编码
- 参数名通常为cmd或pass
```

**冰蝎流量特征：**
```
- 使用AES加密
- 请求体长度固定
- Content-Type: application/octet-stream
```

**哥斯拉流量特征：**
```
- 使用AES加密
- 请求体包含特定标记
- 响应体包含特定标记
```

---

## 十、综合实操练习

### 10.1 练习1：编码解码综合

**实验目标：**
```
完成编码解码综合题目
```

**实验步骤：**
```
1. 识别编码类型
2. 多层解码
3. 提取隐藏信息
4. 获取flag
```

### 10.2 练习2：图片隐写综合

**实验目标：**
```
完成图片隐写综合题目
```

**实验步骤：**
```
1. 文件头分析
2. LSB提取
3. EXIF信息查看
4. 盲水印提取
5. 获取flag
```

### 10.3 练习3：流量分析综合

**实验目标：**
```
完成流量分析综合题目
```

**实验步骤：**
```
1. 协议分析
2. 过滤关键流量
3. 提取敏感信息
4. 还原攻击过程
5. 获取flag
```

---

## 十一、课后作业

### 作业1：编码解码练习
```
完成编码解码练习题：
1. Base64多层编码
2. 自定义编码识别
3. 摩尔斯电码解码
4. 培根密码解码
5. 撰写解题报告
```

### 作业2：图片隐写练习
```
完成图片隐写练习题：
1. LSB隐写提取
2. 盲水印提取
3. 图片修复
4. 撰写解题报告
```

### 作业3：压缩包破解练习
```
完成压缩包破解练习题：
1. 密码字典爆破
2. 伪加密识别
3. CRC32爆破
4. 明文攻击
5. 撰写解题报告
```

### 作业4：音频隐写练习
```
完成音频隐写练习题：
1. 频谱分析
2. DTMF解码
3. SSTV解码
4. MP3Stego提取
5. 撰写解题报告
```

---

## 常用工具速查

### 文件分析工具
```bash
file              # 文件类型识别
binwalk           # 文件分析分离
foremost          # 文件恢复
xxd               # 十六进制查看
hexdump           # 十六进制查看
```

### 图片隐写工具
```bash
stegsolve         # 图片分析
zsteg             # PNG/BMP隐写
stegdetect        # JPEG隐写检测
steghide          # JPEG隐写提取
exiftool          # EXIF信息
```

### 音频隐写工具
```bash
audacity          # 音频分析
multimon-ng       # DTMF解码
mp3stego          # MP3隐写
qsstv             # SSTV解码
```

### 流量分析工具
```bash
wireshark         # 流量分析
tshark            # 命令行分析
tcpdump           # 抓包工具
networkminer      # 网络取证
```

---

## 学习资源

### CTF平台
- CTFHub：https://www.ctfhub.com
- 攻防世界：https://adworld.xctf.org.cn
- BugKuctf：https://www.bugku.com

### 学习资源
- MISC入门：https://ctf-wiki.org/misc/introduction/
- 隐写术：https://ctf-wiki.org/misc/steganography/
- 流量分析：https://ctf-wiki.org/misc/traffic/

### 工具集合
- https://github.com/Gallopsled/pwntools
- https://github.com/calebstewart/pwncat
- https://github.com/AresS31/arsenal

---

## 总结

第六天的学习重点：
1. **MISC基础**：了解MISC题目类型和解题思路
2. **编码解码**：掌握常见编码解码技术
3. **压缩包技术**：掌握密码爆破、伪加密、CRC32爆破
4. **图片隐写**：掌握LSB、EXIF、盲水印等技术
5. **音频隐写**：掌握频谱分析、DTMF、SSTV等技术
6. **流量分析**：掌握USB流量、Web流量分析技术
7. **文件分析**：掌握pyc、PDF、Office文档分析

通过今天的学习，你将具备MISC题目的解题能力。