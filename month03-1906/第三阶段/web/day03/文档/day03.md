[TOC]
# 一、盒子模型

## 1. 基础概念

​	盒子模型分别由外边距、边框、内边距和标签内容组成。

![盒模型概念2](assets\盒模型概念2.png)

## 2. 外边距margin

![外边距4](assets\外边距4.png)

1. 属性：margin

2. 作用：调整标签与标签之间的距离

3. 特殊：
   1）margin:0; 取消默认外边距
   2）margin:0 auto;左右自动外边距，实现标签在父标签范围内水平居中
   3）margin:-10px;标签位置的微调

4. 单方向外边距：只取一个值

   ```html
    margin-top
    margin-right
    margin-bottom
    margin-left
   ```

5. 外边距合并：（03-margin.html）当边框设置为0px宽度的时候才会这样
   1）垂直相遇

   - 子标签的margin-top作用于父标签上

   - 标签之间同时设置垂直方向的外边距，最终取较大的值	

     ![外边距包含合并6](assets\外边距垂直合并5.png)

   2）包含合并

   - 当一个标签包含在另一个标签中时，它们的上面和包含上面的父标签

   - 下面和包含下面的外标签的边距之间也会发生合并

       ![外边距包含合并6](assets\外边距包含合并6.png)

## 3. 边框border

### 1) 边框实现（01-border.html）
语法：
```css
border:width style color; (三项都必须设置：宽度 样式  颜色)
例如：border:2px solid blue;
```
边框样式为必填项，分为：

| style样式取值 | 含义     |
| ------------- | -------- |
| solid         | 实线边框 |
| dotted        | 点线边框 |
| dashed        | 虚线边框 |
| double        | 双线边框 |

### 2) 单边框设置
分别设置某一方向的边框，取值：width style color;

| 属性          | 作用       |
| ------------- | ---------- |
| border-top    | 设置上边框 |
| border-bottom | 设置下边框 |
| border-left   | 设置左边框 |
| border-right  | 设置右边框 |

固定宽度元素的居中实现方式：margin: 0 auto;

### 3) 网页三角标制作（01-border.html）

1. 标签设置宽高为0

2. 统一设置四个方向透明边框

3. 调整某个方向边框可见色

   例如：border-bottom-color: transparent;最下面三角形的颜色(只有设置边框属性很高时候撑出来的图形才可以用这个函数)      ransparent 透明

   border-left-color: transparent;最左边三角形的颜色(只有设置边框属性很高时候撑出来的图形才可以用这个函数)      ransparent 透明
### 4) 圆角边框（01-border.html）

​    ![圆角边框0](assets\圆角边框0.png)

1. 属性：border-radius 指定圆角半径  (半径越大看起来越圆)

   border-top-left-radius: 50%;  左上角弧度为圆的弧度

   border-radius: 50%;    等于整一个圆

2. 取值：像素值或百分比 %  

3. 取值规律：上（左上角）；右（右上角）；下（右下角）；左（左下角）
```
一个值 	表示上右下左都设置这个值
四个值 	表示分别设置上右下左
两个值 	表示分别设置上下 左右   
三个值 	表示分别设置上右下，左右保持一致
```
### 5) 轮廓线
1. 属性：outline
1. 取值：width style color
1. 区别：边框实际占位，轮廓不占位
1. 特殊：取none可以取消文本输入框默认轮廓线
## 2. 内边距padding

![内边距3](assets\内边距3.png)

1. 属性：padding
2. 作用：调整标签内容框与边框之间的距离
3. 取值：单位是 px 或百分比，但不允许使用负值
```
20px;			 一个值表示统一设置上右下左
20px 30px;		 两个值表示分别设置(上下) (左右)
20px 30px 40px;	三个值表示分别设置上右下，左右保持一致
20px 30px 40px 50px;	表示分别设置上右下左
```
4. 单方向内边距,只能取一个值：
```
padding-top  （上方的内边距）
padding-right
padding-bottom（下方的内边距）
padding-left
```
## 3. 盒阴影（02-show.html）

  ![盒子阴影1](assets\盒子阴影1.png)

1. 属性： box-shadow
2. 取值：h-shadow v-shadow blur spread color;
3. 使用：不管是浏览器窗口还是标签自身都可以构建坐标系，统一以左上角为原点，向右向下为X轴和Y轴的正方向

```
h-shadow 	取像素值，阴影的水平向右偏移距离(必须写)
v-shadow 	取像素值，阴影的垂直向下偏移距离(必须写)
blur 		取像素值，表示阴影的模糊程度，值越大越模糊(必须写)
spread 		选填，取像素值，阴影的尺寸
color 		设置阴影颜色,默认为黑色
```

## 4. 盒模型概念

1. 在模型中，它规定了标签处理内容、内边距、边框和外边距的方式
2. 最内是内容，包围内容的是内边距，内边距的边缘是边框
3. 边框以外是外边距，外边距默认是透明的

## 5. 标签最终尺寸的计算

1. 盒模型相关的属性会影响标签在文档中的实际占位，进而影响布局

2. 标签设置width/height指定的是内容框的大小
3. 最终尺寸 = width/height+padding+border+margin

​		

