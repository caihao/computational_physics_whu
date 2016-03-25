# 武汉大学计算物理课程

## 教材
- **Computational Physics**, Nicholas J. Giordano & Hisao Nakanishi
- [**How to think like a computer scientist**](http://www.greenteapress.com/thinkpython/), Allen B. Downey

## 参考书
- **An Introduction to Computer Simulation Methods: Applications to Physical Systems**, Harvey Gould, Jan Tobochnik and Wolfgang Christian
- **Numerical Recipes 3rd Edition: The Art of Scientific Computing**, William H. Press and Saul A. Teukolsky
- [**How to think like a computer scientist -- Learning with Python: Interactive Edition 2.0**](http://interactivepython.org/runestone/static/thinkcspy/index.html)

## 工具
- [markdown](https://daringfireball.net/projects/markdown/)
- [matplotlib](http://matplotlib.org/)
- [VPython](http://vpython.org/)
- [pygame](http://pygame.org/hifi.html)
- [github](https://github.com/)

## 如何提交作业
- 作业在github上提交，使用markdown写作。
- 作业由5部分构成
  - 摘要
  - 背景介绍
  - 正文
  - 结论
  - 致谢（本课程既然全网络共享，允许诸位同学借鉴他人的程序，如有借鉴请致谢。作业其他内容严禁『借鉴』！！！）

### 使用github的方法
1. 注册github账号
2. 建立自己针对计算物理课程的软件池（repository），命名方式computationalphysics_NXXXXXXX（XXXXXXX为个人的学号）
3. 在软件池的README.md文件中给出每次作业的超链接

### 写markdown的工具
- 在github上直接写    
简洁明了，操作略繁琐，不能显示latex公式
- 使用[stackedit](https://stackedit.io/)    
接近完美的在线markdown编辑器，格式非常漂亮，缺点只能单向发布到github
- 使用[作业部落](https://www.zybuluo.com/)    
不错的在线markdown编辑器，中文支持好，缺点不能与github关联

### 作业列表
所有作业都列在[Exercises.md](Exercises.md)里面

## 一点建议
- 物理学院女生本来就少，请各位来上我课的女同学一定要有**信心**
- 学好我这门课的不二法门就是『练习』二字，请各位同学给我惊喜吧，我准备**以作业长度论英雄**

## 学生名单
- [2016年计算物理课学生名单](friends/students_2016.md)

## 各位同学贡献的技巧
### GitHub不支持LaTex公式的一种解决办法
- 公式中不含有空格时，可通过`![](http://latex.codecogs.com/gif.latex?\alpha_A+\beta)`来发布公式，将连接中的`\alpha_A+\beta`替换为想输入的公式即可。
- 公式中含有空格时，可以在[codecogs](http://latex.codecogs.com/)先编辑好公式，然后右击公式，选择图象属性，复制其中“源文件”一栏中的url，在markdown文档中以图片格式发布。
- 基于上述方法以及markdown链接字符的character escape要求，ron89 写了一个[简单的vim插件](github.com/ron89/md_insert_equation.vim)帮助方便地插入/修改公式，和他的另一个插件一样，这个插件需要python支持。使用vim的同学可以安装它。使用方法：
 + 用`<localleader>ee`或`:EditEquation`调出公式编辑栏，若此刻光标不在公式图片链接的区域，会在操作结束后在光标处插入新的公式图片链接；若光标在已插入公式图片链接内，则会开始修改当前公式。
 + 在编辑窗内键入LaTeX语法的公式，回车即可结束公式编辑。
 + **注** `<localleader>` 默认是键盘上的`\`键。
