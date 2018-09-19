# DPark

　　DPark是一个基于Mesos的集群计算框架(cluster computing framework)，是Spark的Python实现版本，类似于MapReduce，但是比其更灵活，可以用Python非常方便地进行分布式计算，并且提供了更多的功能以便更好的进行迭代式计算。

　　DPark的计算模型是基于两个中心思想的：对分布式数据集的并行计算以及一些有限的可以在计算过程中、从不同机器访问的共享变量类型。这个的目标是为了提供一种类似于global address space programming model的工具，例如OpenMP，但是我们要求共享变量的类型必须是那些很容易在分布式系统当中实现的，当前支持的共享变量类型有只读的数据和支持一种数据修改方式的累加器(accumulators)。DPark具有的一个很重要的特性：分布式的数据集可以在多个不同的并行循环当中被重复利用。这个特性将其与其他数据流形式的框架例如Hadoop和Dryad区分开来。



* 目录
    * [01.基础](01.Basic)
    * [02.常用](02.Framework)
    * [03.项目](03.Project)
    * [04.总结](04.Summary)

* 相关资料
    * [官网](https://pypi.org/project/DPark/)