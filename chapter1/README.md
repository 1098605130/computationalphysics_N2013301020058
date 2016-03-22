
#README
#摘要
  本次作业选取的是1.1题
#背景
  物体在地球表面做自由落体运动过程中速度满足方程
  $$\frac{dv}{dt}=-g$$
#正文
  根据欧拉方法我们得到    $v(t+\Delta t)\approx v(t)-g\Delta t$
  若取$\Delta t$为某一足够小的近似值，当已知v的初值v0后多次迭代，便可得到之后所有的数值近似解。
  解答本题利用了python程序，程序内容参见[1zuoye.py](https://github.com/1098605130/computationalphysics_N2013301020058/blob/master/chapter1/1zuoye.py)
  我们选择适当时间间隔并运行程序后得到一系列速度与时间的数组（参见[chapter.txt](https://github.com/1098605130/computationalphysics_N2013301020058/blob/master/chapter1/chapter1.txt))
  并得到图片
  ![](https://raw.githubusercontent.com/1098605130/computationalphysics_N2013301020058/master/chapter1/chapter1.png)
#结论
由图可见，自由落体过程中物体速度与时间成线性关系。
#致谢
本次作业完成过程中参考借鉴了[蔡浩老师](https://github.com/caihao/computational_physics_whu/blob/master/chapter1/rr.py)及[郭潇同学](https://github.com/guoxiaowhu/computationalphysics_N2013301020099/blob/master/chapter1.py)的程序，在此表示感谢！

> Written with [StackEdit](https://stackedit.io/).