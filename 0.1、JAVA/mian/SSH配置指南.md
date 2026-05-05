# GitHub SSH 配置指南

本指南将帮助您设置 SSH 连接到 GitHub 仓库，解决 HTTPS 连接问题。

## 步骤 1：生成 SSH 密钥

1. **打开 Git Bash 或终端**
2. **运行密钥生成命令**：
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   （将 `your_email@example.com` 替换为您的 GitHub 邮箱）

3. **按 Enter 键**接受默认保存位置（通常是 `~/.ssh/id_ed25519`）
4. **输入密码**（可选，按 Enter 键跳过）

## 步骤 2：查看并复制公钥

1. **查看公钥内容**：
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
2. **复制输出的完整内容**（以 `ssh-ed25519` 开头，以您的邮箱结尾）

## 步骤 3：添加公钥到 GitHub

1. **登录 GitHub**
2. **进入 Settings**（右上角头像 → Settings）
3. **点击 SSH and GPG keys**（左侧菜单）
4. **点击 New SSH key**
5. **填写信息**：
   - Title：任意名称（如 "My Laptop"）
   - Key：粘贴刚才复制的公钥内容
6. **点击 Add SSH key**

## 步骤 4：测试 SSH 连接

1. **运行测试命令**：
   ```bash
   ssh -T git@github.com
   ```
2. **首次连接会提示确认**，输入 `yes`
3. **成功信息**：看到 `Hi username! You've successfully authenticated...` 即表示连接成功

## 步骤 5：更新远程仓库 URL

1. **查看当前远程 URL**：
   ```bash
   git remote -v
   ```
2. **更新为 SSH URL**：
   ```bash
   git remote set-url origin git@github.com:xiaojiahuo123/-JAVA.git
   ```
3. **验证更新**：
   ```bash
   git remote -v
   ```
   应该显示 SSH 格式的 URL（以 `git@github.com:` 开头）

## 步骤 6：推送代码

1. **尝试推送**：
   ```bash
   git push origin main
   ```
2. **首次使用 SSH 可能会提示输入密码**（如果生成密钥时设置了密码）

## 常见问题排查

- **权限被拒绝**：检查公钥是否正确添加到 GitHub
- **连接超时**：检查网络连接，确保 SSH 端口（22）未被防火墙阻止
- **密钥未找到**：确认密钥文件路径正确（默认 `~/.ssh/id_ed25519`）

## 注意事项

- SSH 密钥是本地计算机与 GitHub 之间的安全凭证
- 每个设备需要单独生成和添加 SSH 密钥
- 不要与他人共享私钥文件（`id_ed25519`），只分享公钥（`id_ed25519.pub`）

完成以上步骤后，您应该能够使用 SSH 协议成功推送代码到 GitHub 仓库。