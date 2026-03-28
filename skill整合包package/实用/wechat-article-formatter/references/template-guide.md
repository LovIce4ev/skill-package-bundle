# 模板添加指南

## 模板配置文件格式

每个风格模板是一个 JSON 文件，包含完整的样式定义。

### 基础结构

```json
{
  "name": "template-id",
  "displayName": "显示名称",
  "description": "风格描述",
  "colors": { ... },
  "typography": { ... },
  "layout": { ... },
  "elements": { ... }
}
```

### 配置项说明

#### 1. 基础信息
```json
{
  "name": "swiss-brutalism",           // 模板 ID（小写字母+连字符）
  "displayName": "瑞士现代主义",        // 显示名称
  "description": "高对比度黑白粉配色..."  // 风格描述
}
```

#### 2. 颜色方案 (colors)
```json
{
  "colors": {
    "primary": "#FFB3BA",           // 主色调
    "background": "#FFFFFF",        // 背景色
    "text": "#000000",              // 正文颜色
    "textSecondary": "#666666",     // 次要文字颜色
    "border": "#000000",            // 边框颜色
    "quoteBg": "#FFB3BA",          // 引用块背景
    "photoPlaceholder": "#F5F5F5",  // 图片占位背景
    "conclusionBg": "#000000",      // 总结区背景
    "conclusionText": "#FFFFFF"     // 总结区文字
  }
}
```

#### 3. 字体规范 (typography)
```json
{
  "typography": {
    "fontFamily": "-apple-system, BlinkMacSystemFont, ...",
    "mainTitle": {
      "fontSize": "42px",
      "fontWeight": "900",
      "letterSpacing": "-1px",
      "lineHeight": "1.1",
      "textTransform": "uppercase",
      "marginBottom": "30px"
    },
    "subtitle": { ... },
    "guestNumber": { ... },
    "guestName": { ... },
    "guestTitle": { ... },
    "bodyText": { ... },
    "quoteText": { ... }
  }
}
```

#### 4. 布局参数 (layout)
```json
{
  "layout": {
    "maxWidth": "677px",        // 最大宽度
    "padding": "40px 20px",     // 内边距
    "sectionMargin": "100px",   // 章节间距
    "dividerMargin": "80px"     // 分隔符间距
  }
}
```

#### 5. 特殊元素 (elements)
```json
{
  "elements": {
    "badge": {                  // 圆形徽章
      "width": "120px",
      "height": "120px",
      "borderRadius": "50%",
      "background": "#FFB3BA",
      "border": "3px solid #000",
      ...
    },
    "divider": {                // 分隔线
      "width": "100%",
      "height": "1px",
      "background": "#000"
    },
    "photoBox": {               // 照片占位
      "aspectRatio": "4/3",
      "background": "#F5F5F5",
      "border": "3px solid #000",
      ...
    },
    "quoteBlock": {             // 引用块
      "background": "#FFB3BA",
      "padding": "40px",
      "border": "3px solid #000",
      ...
    },
    "conclusionBox": { ... },   // 总结区
    "tag": { ... }              // 标签
  }
}
```

## 添加新模板的步骤

### 方法 1：从 HTML 示例提取

1. **提供 HTML 示例**
   用户提供一个完整的 HTML 文件或代码片段

2. **分析样式特征**
   - 提取所有颜色值
   - 识别字体大小、粗细、行高
   - 记录边框、圆角、阴影等装饰
   - 分析布局结构和间距

3. **生成配置文件**
   ```bash
   # 文件命名：templates/[template-id].json
   # 例如：templates/warm-humanist.json
   ```

4. **测试生成**
   用相同内容测试新模板，确保输出符合预期

### 方法 2：从设计描述创建

1. **收集设计要求**
   - 配色方案（主色、辅色、背景）
   - 字体风格（大小、粗细、间距）
   - 装饰元素（边框、圆角、图标）
   - 整体氛围（正式/轻松、现代/复古）

2. **参考现有模板**
   复制 `swiss-brutalism.json`，修改关键参数

3. **调整细节**
   - 颜色：改为新的配色方案
   - 字体：调整大小和粗细
   - 间距：根据风格调整疏密
   - 装饰：添加或移除特殊元素

4. **保存并测试**

## 模板命名规范

- 使用小写字母和连字符
- 描述性命名，体现风格特点
- 示例：
  - `swiss-brutalism` - 瑞士风格
  - `warm-humanist` - 温暖人文
  - `minimalist-mono` - 极简黑白
  - `retro-cyberpunk` - 复古赛博朋克

## 常见风格参考

### 温暖人文风
- 配色：米色、棕色、暖橙色
- 字体：中等粗细，圆润
- 边框：圆角，细线条
- 装饰：柔和阴影，渐变

### 极简主义
- 配色：黑白灰
- 字体：细线条，大留白
- 边框：极细或无边框
- 装饰：最少化，强调空间

### 赛博朋克
- 配色：霓虹色（粉、蓝、紫）+ 深色背景
- 字体：等宽字体，科技感
- 边框：发光效果（用阴影模拟）
- 装饰：故障效果、网格背景

## 注意事项

1. **所有样式必须可内联**
   不要使用需要 `<style>` 标签的特性

2. **测试微信兼容性**
   生成后必须在微信编辑器中测试

3. **保持一致性**
   同一模板内的所有元素要风格统一

4. **考虑可读性**
   无论什么风格，正文必须清晰易读

5. **提供示例**
   新模板添加后，生成一个示例文件到 `assets/`
