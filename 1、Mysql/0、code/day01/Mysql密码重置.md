  第一步：停止MySQL服务
  以管理员身份打开CMD或PowerShell，运行：

```
  net stop mysql80
```

  ▎ 如果上面命令无效，尝试 net stop mysql 或在服务管理器中手动停止

  第二步：跳过权限验证启动MySQL

```sql
mysqld --console --skip-grant-tables --shared-memory
```

  ▎ 保持这个窗口不要关闭

  第三步：新开一个CMD窗口，连接MySQL

```
  mysql -u root
```

  第四步：修改密码

```
FLUSH PRIVILEGES;
  ALTER USER 'root'@'localhost' IDENTIFIED BY '你的新密码';
  EXIT;
```

  第五步：重启MySQL服务
  1. 关闭第二步的窗口（Ctrl+C）
  2. 正常启动MySQL：
    
    ```
    net start mysql80
    ```
    
    

