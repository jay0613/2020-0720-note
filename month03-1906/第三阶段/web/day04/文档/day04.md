[TOC]
# 一、布局方式
![定位机制0](assets\定位机制0.png)

### 1. 普通文档流

​		默认布局方式，按照代码书写顺序及标签类型从上到下，从左到右依次显示。

![普通流定位1](assets\普通流定位1.png)

### 2. 浮动布局（04-float.html）（05-float2.html）

​		主要用于设置块元素的水平排列

![浮动流定位2](assets\浮动流定位2.png)

#### 1）属性

```
float
```

#### 2）取值 

可取 left 或 right，设置元素向左浮动或向右浮动

```css
float:left/right;
clear:left/right/both
```

#### 3）特点

- 元素设置浮动会从原始位置脱流，向左或向右依次停靠在其他元素边缘，在文档中不再占位
- 元素设置浮动，就具有块元素的特征(原来是行内元素设置浮动也会变成块元素)，可以手动调整宽高
- "文字环绕"：浮动元素遮挡正常元素的位置，无法遮挡正常内容的显示，内容围绕在浮动元素周围显示

#### 4）常见问题 

子元素全部设置浮动，导致父元素高度为0，影响父元素背景色和背景图片展示,影响页面布局

#### 5）解决（04-float.html 方式一二三）

- 对于内容固定的元素，如果子元素都浮动，可以给父元素固定高度(例:导航栏)
- 在父元素的末尾添加空的块元素。设置 clear:both; 清除浮动
- 为父元素设置 overflow:hidden; 解决高度为0，从而可以包裹浮动的元素

### 3. 定位布局(01-pos.html)

​		结合偏移属性调整元素的显示位置

![绝对与相对定位关系3](assets\绝对与相对定位关系3.png)

#### 1）属性
position
#### 2）取值(01-pos.html)
可取relative（相对定位）/ absolute（绝对定位）/ fixed（固定定位）
```css
position:relative/absolute/fixed
```
#### 3）偏移属性（设置了定位的元素才可以使用下面的偏移方法）
设置定位的元素可以使用偏移属性调整距离参照物的位置
```text
top   	距参照物的顶部
right	距参照物的右侧
bottom	距参照物的底部
left	距参照物的左侧   left: 8px;  以左边为参照物向右偏移8px 
```
#### 4）分类 
+ relative 相对定位   position:relative;     》》》》》(01-pos.html)
```text
元素设置相对定位,可参照元素在文档中的原始位置进行偏移,不会脱离文档流（意思是偏离前的原始位置还占着不能给别人使用）
```
+ absolute 绝对定位  position:absolute;    》》》》》（02-abs.html）
```text
1. 绝对定位的元素参照离他最近的已经定位的祖先元素（父辈元素以上都行，前提是已经定位，不管是什么定位方式）进行偏移,如果没有,则参照窗口进行偏移
2. 绝对定位的元素会脱流,在文档中不占位,可以手动设置宽高
```
使用绝对定位 : 父元素设置相对定位,子元素绝对定位，参照已定位的父元素偏移

+ fixed 固定定位  position:fixed;    >>>>>(03-fixed.html)
```text
1. 参照窗口进行定位,不跟随网页滚动而滚动
2. 脱离文档流
```
#### 5）堆叠次序 (04-zindex.html)
元素发生堆叠时可以使用 z-index 属性调整已定位元素的显示位置，值越大元素越靠上：
+ 属性 : z-index
+ 取值 : 无单位的数值,数值越大，越靠上
+ 堆叠：
 1. 定位元素与文档中正常元素发生堆叠，永远是已定位元素在上

 2. 同为已定位元素发生堆叠，按照 HTML 代码的书写顺序，后来者居上

    

    **扩展内容：div:nth-child(1)通过元素的伪类选择器获取相同元素的某个元素;参数1表示第一个，2,3分别表示第二第三个**(01-pos.html) 
# 二、背景属性
### 1. 背景颜色
```css
background-color: red;
```
### 2. 背景图片相关
#### 1）设置背景图片(05-bgimg.html)
```css
background-image : url("路径");
```
设置背景图片，指定图片路径，如果路径中出现中文或空格，需要加引号
#### 2）设置背景图片的重复方式(05-bgimg.html)
默认背景图片从元素的左上角显示，如果图片尺寸与元素尺寸不匹配时，会出现以下情况：
1. 如果元素尺寸大于图片尺寸，会自动重复平铺，直至铺满整个元素
2. 如果元素尺寸小于图片尺寸，图片默认从元素左上角开始显示，超出部分不可见
```css
background-repeat:repeat/repeat-x/repeat-y/no-repeat
```
```text
取值 ：
	repeat  默认值，沿水平和垂直方向重复平铺
	repeat-x 沿X轴重复平铺
	repeat-y 沿Y轴重复平铺
	no-repeat 不重复平铺
```
#### 3）设置背景图片的显示位置(05-bgimg.html)
默认显示在元素左上角
```css
background-position:x y;
例如：background-position: 10px 20px;  左上角为原点，沿x（右边）移动10px，沿y（下边）移动20px
```
取值方式 ：
```text
1. 像素值
	设置背景图片的在元素坐标系中的起点坐标
2. 方位值
	水平：left/center/right    ——————》   x的值
	垂直：top/center/bottom	——————》   y的值
	注：如果只设置某一个方向的方位值，另外一个方向默认为center;
水平和纵向都居中: background-position: center;
```
精灵图技术 ：为了减少网络请求，可以将所有的小图标拼接在一张图片上，一次网络请求全部得到；借助于background-position 进行背景图片位置的调整，实现显示不同的图标
#### 4）设置背景图片的尺寸
```css
background-size:width height;
```
取值方式 ：
```text
1. 像素值
	1. 500px 500px; 同时指定宽高
	2. 500px;  指定宽度，高度自适应
2. 百分比
	百分比参照元素的尺寸进行计算
	1. 50% 50%; 根据元素宽高,分别计算图片的宽高
	2. 50%; 根据元素宽度计算图片宽高,图片高度等比例缩放
```

### 3. 背景属性简写(05-bgimg.html)
```css
background:color url("") repeat position;（可以同时一次性写完这么多格式）
```
注意 ：
1. 如果需要同时设置以上属性值，遵照相应顺序书写
2. background-size 单独设置
#  三、文本属性
### 1. 字体相关
#### 1）设置字体大小
```css
font-size:20px;
```
#### 2）设置字体粗细程度
```css
font-weight:normal;
```
取值 ：
```text
1. normal（默认值）等价于400
2. bold   (加粗) 等价于700
```
#### 3）设置斜体
```css
font-style:italic;
```
#### 4）设置字体名称
```css
font-family:Arial,"黑体","宋体"; 
```
取值 :

    1.防止有的浏览器不识别该字体，可以指定多个字体名称作为备选字体，使用逗号隔开，
    优先选择第一个字体

   2. 如果字体名称为中文，或者名称中出现了空格，必须使用引号

         例 :

```Css
font-family:Arial;
font-family:"黑体","Microsoft YaHei",Arial;
```

#### 5）字体属性简写
```css
font : style weight size family;
```
注意 :

       1. 如果四个属性值都必须设置，严格按照顺序书
       2. size family 是必填项

### 2. 文本样式
#### 1）文本颜色
```css
color:red;
```
#### 2）文本装饰线
```css
text-decoration:none;
```
取值 :
    underline		  下划线
    overline		     上划线
    line-through 	 删除线
    none			       取消装饰线

#### 3）文本内容的水平对齐方式
```css
text-align:center;
```
取值 : 
```text
left(默认值)	左对齐
center		  居中对齐
right		  右对齐
```
块元素居中实现方式：margin: 0 auto;

#### 4）行高

```css
line-height:30px;
```
使用 :
    文本在当前行中永远垂直居中，可以借助行高调整文本在元素中的垂直显示位置
     	line-height = height 设置一行文本在元素中垂直居中（上下居中）
     	line-height > height 文本下移显示
     	line-height < height 文本靠上显示
     特殊 :
     	line-height可以采用无单位的数值，代表当前字体大小的倍数,以此计算行高

