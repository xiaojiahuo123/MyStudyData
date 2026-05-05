# Claude Code Skills 参考手册

> 生成日期: 2026-05-05

---

## 一、已安装的插件 Skill

### 1. frontend-design

**来源:** claude-plugins-official（官方市场）  
**调用方式:** `/frontend-design`，或描述 UI/前端需求自动触发

**功能:** 创建独具特色、生产级前端界面。生成避免"AI 味"的创造性、精美代码，注重排版、配色、动效等美学细节。

**适用场景:**
- 构建 Web 组件、页面或应用
- 需要高设计品质的前端界面
- 想要独特的视觉风格（极简、极繁、复古未来、有机、奢侈、玩具感、编辑风、野蛮主义等）

---

### 2. banner-design

**来源:** ui-ux-pro-max-skill（第三方插件）  
**调用方式:** `/banner-design [platform] [style] [dimensions]`

**功能:** 为社交媒体、广告、网站 Hero 图、印刷品等设计横幅/封面。支持多种艺术风格方向，AI 生成视觉元素。

**支持的平台:** Facebook、Twitter/X、LinkedIn、YouTube、Instagram、Google Display、网页 Hero、印刷品  
**支持的风格:** 极简、渐变、大胆排版、照片式、插画、几何、复古、玻璃态、3D、霓虹、双色调、编辑风、拼贴等

---

### 3. brand

**来源:** ui-ux-pro-max-skill（第三方插件）  
**调用方式:** `/brand [update|review|create] [args]`

**功能:** 品牌标识管理：品牌声音、视觉识别、消息框架、资产管理、品牌一致性审查。

**适用场景:**
- 品牌语调定义和内容语调指导
- 视觉识别标准和风格指南开发
- 消息框架创建
- 品牌一致性审查和审计
- 资产组织、命名和审批

---

### 4. design

**来源:** ui-ux-pro-max-skill（第三方插件）  
**调用方式:** `/design [design-type] [context]`

**功能:** 综合设计 skill，涵盖品牌标识、设计 Token、UI 样式、Logo 生成（55 种风格）、企业形象项目（50 种交付物）、HTML 演示文稿、横幅设计（22 种风格）、图标设计（15 种风格）、社交图片生成。

**适用场景:**
- Logo 设计和 AI 生成
- 企业形象项目 (CIP) 和 Mockup
- 社交图片和多媒体素材
- 图标和横幅制作
- 品牌 / Token / UI 全套设计

---

### 5. design-system

**来源:** ui-ux-pro-max-skill（第三方插件）  
**调用方式:** `/design-system [component or token]`

**功能:** 三层设计 Token 架构（原始→语义→组件），CSS 变量、间距/排版缩放、组件规格说明、战略幻灯片生成。

**适用场景:**
- 设计 Token 创建
- 组件状态定义
- CSS 变量系统
- 间距/排版标准制定

---

### 6. slides

**来源:** ui-ux-pro-max-skill（第三方插件）  
**调用方式:** `/slides [topic] [slide-count]`

**功能:** 使用 HTML + Chart.js 创建策略性演示文稿，支持设计 Token、响应式布局、文案公式和上下文幻灯片策略。

**适用场景:**
- 营销演示和 Pitch Deck
- 数据驱动幻灯片（图表）
- 策略性幻灯片设计

---

### 7. ui-styling

**来源:** ui-ux-pro-max-skill（第三方插件）  
**调用方式:** `/ui-styling [component or layout]`

**功能:** 基于 shadcn/ui 组件（Radix UI + Tailwind）+ Canvas 视觉设计，创建美观、可访问的用户界面。

**适用场景:**
- 构建用户界面组件（对话框、下拉、表单、表格等）
- 实现设计系统
- 响应式布局
- 主题和颜色定制、暗色模式
- 生成视觉设计和海报

---

### 8. ui-ux-pro-max

**来源:** ui-ux-pro-max-skill（第三方插件）  
**调用方式:** `/ui-ux-pro-max <query>` 或通过 Python 搜索脚本调用

**功能:** UI/UX 设计智能数据库。包含 50+ 风格、161 套色板、57 组字体配对、161 种产品类型、99 条 UX 指南、25 种图表类型，覆盖 10 个技术栈。

**支持的技术栈:** React、Next.js、Vue、Svelte、SwiftUI、React Native、Flutter、Tailwind、shadcn/ui、HTML/CSS

**搜索命令:**
```bash
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain>
```
可选领域: `product`, `style`, `typography`, `color`, `landing`, `chart`, `ux`

---

## 二、内置 System Skill

以下 skill 随 Claude Code 内置，无需安装即可使用：

### 1. init
**调用方式:** `/init`  
**功能:** 初始化新项目的 CLAUDE.md 文件，自动分析代码库并生成项目文档。

---

### 2. review
**调用方式:** `/review`  
**功能:** 审查 Pull Request，检查代码质量和潜在问题。

---

### 3. security-review
**调用方式:** `/security-review`  
**功能:** 对当前分支的待提交变更进行安全审查。

---

### 4. claude-api
**调用方式:** `/claude-api`  
**功能:** 构建、调试和优化 Claude API / Anthropic SDK 应用。处理模型迁移（4.5→4.6→4.7）、Prompt Caching、工具使用等。

---

### 5. simplify
**调用方式:** `/simplify`  
**功能:** 审查已修改代码的重用性、质量和效率，自动修复发现的问题。

---

### 6. loop
**调用方式:** `/loop [间隔] [命令]`（例如 `/loop 5m /review`）  
**功能:** 按指定间隔循环执行某个命令，用于轮询、持续监控等场景。默认间隔 10 分钟。

---

### 7. update-config
**调用方式:** `/update-config`  
**功能:** 通过 settings.json 配置 Claude Code 的行为，包括权限、环境变量、Hook 等。

---

### 8. keybindings-help
**调用方式:** `/keybindings-help`  
**功能:** 自定义键盘快捷键，修改 `~/.claude/keybindings.json`。

---

### 9. fewer-permission-prompts
**调用方式:** `/fewer-permission-prompts`  
**功能:** 扫描历史对话中的只读 Bash/MCP 工具调用，自动添加权限白名单以减少授权提示。

---

## 三、调用方式汇总

| Skill | 手动调用 | 自动触发 |
|---|---|---|
| frontend-design | `/frontend-design` | 构建 UI 组件/页面时 |
| banner-design | `/banner-design` | 设计横幅/封面时 |
| brand | `/brand` | 品牌相关内容时 |
| design | `/design` | 综合设计需求时 |
| design-system | `/design-system` | 设计 Token/组件规格时 |
| slides | `/slides` | 创建演示文稿时 |
| ui-styling | `/ui-styling` | UI 组件/样式开发时 |
| ui-ux-pro-max | `/ui-ux-pro-max` | UI/UX 设计决策时 |
| init | `/init` | -- |
| review | `/review` | -- |
| security-review | `/security-review` | -- |
| claude-api | `/claude-api` | Anthropic SDK 代码中 |
| simplify | `/simplify` | -- |
| loop | `/loop` | -- |
| update-config | `/update-config` | -- |
| keybindings-help | `/keybindings-help` | -- |
| fewer-permission-prompts | `/fewer-permission-prompts` | -- |

> **说明:** "自动触发"表示在对话中提及相关需求时，Claude 会自动判断并调用对应 skill，无需手动输入 `/` 命令。
