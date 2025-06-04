#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:admin
# datetime:2025/6/4 16:09
# software: PyCharm
# brief :
"""
Qt的多线程的锁

https://www.cnblogs.com/zzzsj/p/14553701.html

QMutex类提供的是线程之间的访问顺序化
QMutex的目的是保护一个对象、数据结构或者代码段，所以同一时间只有一个线程可以访问它

void DebugInfo()
{
 qDebug("ABC");
 qDebug("DEF");
}

如果同时在两个线程中调用这个方法，结果的顺序将是：

ABC ABC DEF DEF


如果你使用了一个互斥量：
QMutex mutex;

void DebugInfo()
{
     mutex.lock();
     qDebug("ABC");
     qDebug("DEF");
     mutex.unlock();
}
你在一个线程中调用lock()，其它线程将会在同一地点试图调用lock()来阻塞，知道这个线程调用unlock()之后其它线程才会获得这个锁

lock()的一种非阻塞选择是tryLock()
QMutex::QMutex ( bool recursive = FALSE )
构造一个新的互斥量。这个互斥量是在没有锁定的状态下创建的。
如果recursive为真，就构造一个递归互斥量，
如果recursive为假（默认值），就构造一个普通互斥量。
对于一个递归互斥量，一个线程可以锁定一个互斥量多次并且只有在相同数量的unlock()调用之后，
它才会被解锁

QMutex::~QMutex ()
销毁这个互斥量

void QMutex::lock ()
试图锁定互斥量。如果另一个线程已经锁定这个互斥量，那么这次调用将阻塞直到那个线程把它解锁
试图锁定互斥量。如果另一个线程已经锁定这个互斥量，那么这次调用将阻塞直到那个线程把它解锁

bool QMutex::tryLock ()
试图锁定互斥量。如果锁被得到，这个函数返回真。
如果另一个进程已经锁定了这个互斥量，这个函数返回假，而不是一直等到这个锁可用为止，比如，它不是阻塞的。
在另一个线程可以成功锁定它之前，这个锁必须被调用unlock()来解锁。
也可以参考lock()、unlock()和locked()

void QMutex::unlock ()
解锁这个互斥量。试图对不同的线程中锁定的互斥量进行解锁将会返回一个错误。
对一个没有锁定的互斥量进行解锁的结果是将导致未定义的行为（不同的操作系统的线程实现是有很大不同的）。
也可以参考lock()和locked()

"""