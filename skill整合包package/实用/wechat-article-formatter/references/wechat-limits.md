# 微信公众号 HTML/CSS 限制说明

## 支持的特性

### ✅ HTML 标签
- 基础标签：`<section>`, `<div>`, `<p>`, `<span>`, `<br>`
- 标题标签：`<h1>` - `<h6>`
- 图片：`<img>`
- 链接：`<a>`
- 列表：`<ul>`, `<ol>`, `<li>`
- 强调：`<strong>`, `<em>`, `<b>`, `<i>`

### ✅ 内联样式
所有 CSS 必须通过 `style=""` 属性内联使用：

```html
<section style="background: #FFB3BA; padding: 40px; border: 3px solid #000;">
  <p style="font-size: 20px; font-weight: 700; color: #000;">内容</p>
</section>
```

### ✅ 支持的 CSS 属性

**布局**：
- `display`: flex, block, inline-block
- `position`: relative, absolute
- `margin`, `padding`
- `width`, `height`, `max-width`, `max-height`
- `aspect-ratio` (部分支持)

**文字**：
- `font-size`, `font-weight`, `font-family`
- `line-height`, `letter-spacing`
- `text-align`, `text-transform`
- `color`

**背景和边框**：
- `background`, `background-color`
- `border`, `border-radius`
- `opacity`

**Flexbox**：
- `justify-content`, `align-items`
- `flex-direction`, `flex-wrap`
- `gap` (部分支持)

## 不支持的特性

### ❌ 外部资源
- `<style>` 标签
- 外部 CSS 文件 (`<link rel="stylesheet">`)
- JavaScript (`<script>`)
- 外部字体 (`@font-face`)

### ❌ 高级 CSS
- CSS 变量 (`--variable`)
- CSS Grid (不稳定)
- 动画和过渡 (`@keyframes`, `transition`)
- 伪元素 (`::before`, `::after`)
- 伪类 (`:hover`, `:active` 等)
- `calc()` 函数

### ❌ 媒体查询
- `@media` 查询不生效
- 响应式设计需要用固定宽度 + 百分比实现

## 最佳实践

### 1. 使用 `<section>` 而非 `<div>`
微信编辑器对 `<section>` 的兼容性更好：
```html
<!-- 推荐 -->
<section style="padding: 20px;">内容</section>

<!-- 不推荐 -->
<div style="padding: 20px;">内容</div>
```

### 2. 颜色使用十六进制
```html
<!-- 推荐 -->
<p style="color: #000000;">文字</p>

<!-- 不推荐 -->
<p style="color: rgb(0,0,0);">文字</p>
<p style="color: black;">文字</p>
```

### 3. 字体栈使用系统字体
```css
font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif;
```

### 4. 图片占位使用背景色 + 文字
```html
<section style="width: 100%; aspect-ratio: 4/3; background: #F5F5F5; border: 3px solid #000; display: flex; align-items: center; justify-content: center;">
  <p style="font-size: 14px; color: #999;">📷 请插入图片</p>
</section>
```

### 5. 避免深层嵌套
微信编辑器对深层嵌套支持不佳，尽量保持 3 层以内。

### 6. 测试复制粘贴
生成后务必测试：
1. 在浏览器中打开 HTML
2. 全选复制（Cmd+A, Cmd+C）
3. 粘贴到微信公��号编辑器
4. 检查样式是否保留

## 常见问题

### Q: 为什么粘贴后样式丢失？
A: 检查是否使用了 `<style>` 标签或外部 CSS，必须全部改为内联样式。

### Q: 为什么 flexbox 布局不生效？
A: 确保父元素设置了 `display: flex`，并且没有使用不支持的属性如 `gap`。

### Q: 如何实现响应式？
A: 使用百分比宽度和 `max-width`，避免使用媒体查询。

### Q: 图片如何插入？
A: 先用占位符生成 HTML，粘贴到编辑器后，在编辑器中直接上传图片替换占位符。

## 兼容性检查清单

生成 HTML 前检查：
- [ ] 所有样式都是内联的（`style=""`）
- [ ] 没有使用 `<style>` 标签
- [ ] 没有使用 JavaScript
- [ ] 颜色使用十六进制格式
- [ ] 字体使用系统字体栈
- [ ] 使用 `<section>` 而非 `<div>`
- [ ] 嵌套层级不超过 3 层
- [ ] 图片使用占位符而非外部链接
