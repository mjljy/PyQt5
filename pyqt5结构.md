##  <font color=#FF0000> 1. QtCore </font>
涵盖了包的核心的非GUI功能  
此模块被用于处理程序中涉及的    
时间   
文件   
目录
数据类型、文本流、链接、QMimeData、线程或进程等对象


##   <font color=#FF0000> 2. QtGui </font>
涵盖了多种基本图形功能的类，包括但不限于：窗口集、事件处理、2D图形、基本的图像和界面、字体和文本类

## <font color=#FF0000> 2. QtWidgets </font>
包含了一整套UI元素控件，用于建立符合系统风格的Classic界面，非常方便，可以在安装时选择是否使用此功能

> 1. QApplication
> > 用于管理图形用户界面应用程序的控制流和主要设置。
它包含主事件循环，对来自窗口系统和其他资源的所有事件进行处理和调度；
它也对应用程序的初始化和结束进行处理，并且提供对话管理；
还对绝大多数系统范围和应用程序范围的设置进行处理  
> >
> > QApplication采用事件循环机制，当QApplication初始化后，就进入应用程序的主循环（Main Loop），
开始进行事件处理，主循环从窗口系统接收事件，
并将这些事件分配到应用程序的控件中。
当调用sys.exit()函数时，主循环就会结束


> 2. move() 
> > 方法定位了每一个元素，使用 x、y 坐标。x、y 坐标的原点是程序的左上角
> >
> 3. QTableView
> > 实例化的时候 要执行行和列
> > https://blog.csdn.net/weixin_48088847/article/details/136759157
> > https://www.cnblogs.com/linyfeng/p/11832237.html
> > 
> > QTableWidget  继承自 QTableView  QAbstractItemView  QAbstractScrollArea  QWidget
> >
> >
> > 
> >
> >
> >
> >
> >