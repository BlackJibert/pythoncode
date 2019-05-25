## 3.1 Package overview
panda是一个Python包，提供快速、灵活和富有表现力的数据结构，旨在使处理“关系”或“标记”数据既简单又直观。
它的目标是成为用Python进行实际的、真实的数据分析的基本高层构建块。
此外，它还有一个更广泛的目标，即成为任何语言中可用的最强大、最灵活的开源数据分析/操作工具。它已经在朝着这个目标迈进。


pandas非常适合许多不同类型的数据:

•具有不同类型列的表格数据，如SQL表或Excel电子表格

•有序和无序(不一定是固定频率)时间序列数据。

•带有行和列标签的任意矩阵数据(同质或异构类型)

•任何其他形式的观察/统计数据集。这些数据实际上根本不需要标记就可以放入panda数据结构中

pandas的两个主要数据结构Series(一维)和DataFrame(二维)处理金融、统计、社会科学和许多工程领域的绝大多数典型用例。对于R用户，
DataFrame提供了R的data.frame提供的所有内容，甚至更多。
panda构建在NumPy之上，旨在与许多其他第三方库很好地集成在科学计算环境中。

以下是padas擅长的几件事:

•易于处理浮点数据和非浮点数据中丢失的数据(以NaN表示)

•大小可变性:可以从DataFrame和高维对象中插入和删除列

•自动显式数据对齐:对象可以显式对齐到一组标签上，用户也可以

只需忽略标签，让Series、DataFrame等自动对齐计算中的数据

•功能强大、灵活的group by功能，可以对数据集执行拆分应用组合操作，用于聚合和转换数据

•易于将其他Python和NumPy数据结构中不规则的、不同索引的数据转换为DataFrame对象

•基于智能标签的切片、花哨的索引和大型数据集的子集

•直观地合并和连接数据集

•数据集的灵活重塑和旋转

•坐标轴分层标注(每滴答可能有多个标签)

• 健壮的IO工具，用于从平面文件(CSV和分隔符)、Excel文件、数据库中加载数据，以及从超快HDF5格式中保存/加载数据

•时间序列特有的功能:日期范围生成和频率转换、移动窗口统计、移动窗口线性回归、日期移位和滞后等。

这里的许多原则都是为了解决使用其他语言/科学研究环境时经常遇到的缺点。对于数据科学家来说，处理数据通常分为多个阶段:咀嚼和清理数据，分析/建模数据，然后将分析结果组织成适合绘图或表格显示的形式。熊猫是所有这些任务的理想工具。

其他一些笔记:
pandas是很快的。Cython代码中对许多底层算法位进行了广泛的调整。然而，与其他任何泛化方法一样，泛化通常会牺牲性能。因此，如果您专注于应用程序的一个特性，您可能能够创建一个更快的专用工具。
•pandas依赖于状态模型，这使得它成为Python统计计算生态系统的重要组成部分。
•pandas已被广泛用于金融应用的生产中。

### 3.1.1 Data Structures

 
 
|Dimensions | Name | Description|
|:-----:|:---:|:-------------:| 
|1| Series | 1D labeled homogeneously-typed array |
|2| DataFrame General| 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed column|

为什么要有多个数据结构?
考虑panda数据结构的最佳方法是将其作为低维度数据的灵活容器。例如，DataFrame是Series的容器，Series是scalars的容器。我们希望能够以类似词典的方式从这些容器中插入和删除对象。
此外，我们希望考虑时间序列和横断面数据集的典型方向的公共API函数的合理默认行为。当使用ndarrays存储2维和3维数据时，用户在编写函数时需要考虑数据集的方向;轴被认为或多或少是等价的(除非C或fortran关系到性能)。在panda中，坐标轴的作用是赋予数据更多的语义;即。，对于特定的数据集，可能有一种“正确”的方法来确定数据的方向。因此，目标是减少在下游函数中编码数据转换所需的脑力劳动。

例如，对于表格数据(DataFrame)，考虑索引(行)和列比考虑轴0和轴1在语义上更有帮助。因此，遍历DataFrame的列可以提高可读性

代码:
for col in df.columns:
series = df[col]
//do something with series

### 3.1.2数据的可变性和复制性
所有panda数据结构都是值可变的(它们包含的值可以更改)，但并不总是大小可变的。序列的长度不能更改，但是，例如，可以将列插入到DataFrame中。然而，绝大多数方法都会生成新的对象，并且不改变输入数据。一般来说，我们喜欢在合理的地方保持不变。
### 3.1.3 Getting Supporst
The first stop for pandas issues and ideas is the Github Issue Tracker. If you have a general question, pandas community experts can answer through Stack Overflow.

## 3.2  10 Minutes to pandas

### 3.2.1 Object Creation
See the Data Structure Intro section.
Creating a Series by passing a list of values, letting pandas create a default integer index:
    
    import numpy as np
    import pandas as pd
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)
 outputs:
 
    0    1.0
    1    3.0
    2    5.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64 

Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
    
    import pandas as pd
    dates = pd.date_range('20190411', periods=6)
    print(dates)
 outputs:
 
    DatetimeIndex(['2019-04-11', '2019-04-12', '2019-04-13', '2019-04-14',
                   '2019-04-15', '2019-04-16'],
                  dtype='datetime64[ns]', freq='D')
    
Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:

    import numpy as np
    import pandas as pd
    dates = pd.date_range('20190411', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    
outputs:

                      A         B         C         D
    2019-04-11 -1.201804 -0.266710 -0.882411  0.595759
    2019-04-12  0.897528 -0.800323  0.301689 -0.941926
    2019-04-13  0.884472  0.323029  0.877872  2.257509
    2019-04-14  0.911898 -1.064034 -0.657938  1.035056
    2019-04-15 -0.029871  1.429455 -0.528715 -0.876533
    2019-04-16 -1.229636  1.729853  0.423710 -0.799559

Creating a DataFrame by passing a dict of objects that can be converted to series-like.

    import numpy as np
    import pandas as pd
    df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20190411'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'), 'D': np.array([3] * 4, dtype='int32'), 'E': pd.Categorical(["test", "train", "test", "train"]), 'F': 'foo'})
    print(df2)
 
 outputs:
 
             A          B    C  D      E    F
    0  1.0 2019-04-11  1.0  3   test  foo
    1  1.0 2019-04-11  1.0  3  train  foo
    2  1.0 2019-04-11  1.0  3   test  foo
    3  1.0 2019-04-11  1.0  3  train  foo
    

The columns of the resulting DataFrame have different dtypes.

    print(df2.dtypes)

outputs:

    A float64
    B datetime64[ns]
    C float32
    D int32
    E category
    F object
    dtype: object


If you’re using IPython, tab completion for column names (as well as public attributes) is automatically enabled.
Here’s a subset of the attributes that will be completed:

### 3.2.2 Viewing Data

See the Basics section.
Here is how to view the top and bottom rows of the frame:
    
    import numpy as np
    import pandas as pd
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20190411'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'), 'D': np.array([3] * 4, dtype='int32'), 'E': pd.Categorical(["test", "train", "test", "train"]), 'F': 'foo'})
    #输出不带索引的数据
    print('---df.head()----')
    print(df.head())
    #切割前三行
    print('----df.tail(3)--')
    print(df.tail(3))
    #输出第一列(索引)
    print('---df.index----')
    print(df.index)
    #输出第一行
    print('----df.columns--')
    print(df.columns)
    
outputs:
    
    ---df.head()----
                       A         B         C         D
    2013-01-01 -1.563444  1.111645  1.374893  1.400039
    2013-01-02  0.631673 -0.896159  1.244630  0.320330
    2013-01-03  0.685311  1.991504 -0.030118  0.414124
    2013-01-04  1.856709 -0.062462 -0.892879 -0.182180
    2013-01-05  0.472852 -0.086991  0.023884 -0.307264
    ----df.tail(3)--
                       A         B         C         D
    2013-01-04  1.856709 -0.062462 -0.892879 -0.182180
    2013-01-05  0.472852 -0.086991  0.023884 -0.307264
    2013-01-06 -1.673916  1.159550 -1.198338  1.231877
    ---df.index----
    DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                   '2013-01-05', '2013-01-06'],
                  dtype='datetime64[ns]', freq='D')
    ----df.columns--
    Index(['A', 'B', 'C', 'D'], dtype='object')
    
to_numpy()给出了底层数据的NumPy表示。注意，当您的数据aframe具有具有不同数据类型的列时，他的操作可能是一个昂贵的操作，这归根结底是panda和NumPy之间的一个基本区别:NumPy数组对于整个数组有一个dtype，而panda数据aframes对于每一列有一个dtype。当您调用DataFrame.to_numpy()时，panda将找到可以容纳DataFrame中所有dtype的NumPy dtype。这可能最终成为对象，这需要将每个值转换为Python对象。

For df, our DataFrame of all floating-point values, DataFrame.to_numpy() is fast and doesn’t require copying
data.

    import numpy as np
    import pandas as pd
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20190411'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'), 'D': np.array([3] * 4, dtype='int32'), 'E': pd.Categorical(["test", "train", "test", "train"]), 'F': 'foo'})
    print(df)
    print("after convert:")
    print(df.to_numpy())
    

outputs:

                 A         B         C         D
    2013-01-01 -1.326985 -0.149831  1.567691  0.041660
    2013-01-02  0.554152 -2.061275 -0.170587 -0.273717
    2013-01-03 -0.500863 -1.843006 -0.834873 -0.594004
    2013-01-04 -0.767220 -1.800286 -0.223219  0.568272
    2013-01-05 -0.258687  0.578685  0.886993  1.489890
    2013-01-06  1.998994 -1.049193  2.739308 -0.231561
    after convert:
    [[-1.32698474 -0.14983142  1.56769146  0.0416601 ]
     [ 0.55415215 -2.06127451 -0.17058673 -0.27371658]
     [-0.50086279 -1.84300578 -0.83487307 -0.59400436]
     [-0.76721999 -1.80028649 -0.22321937  0.5682725 ]
     [-0.25868651  0.57868452  0.88699252  1.48989019]
     [ 1.99899378 -1.04919284  2.73930778 -0.23156064]]
    
 For df2, the DataFrame with multiple dtypes, DataFrame.to_numpy() is relatively expensive.
 
    import numpy as np
    import pandas as pd
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20190411'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'), 'D': np.array([3] * 4, dtype='int32'), 'E': pd.Categorical(["test", "train", "test", "train"]), 'F': 'foo'})
    print(df2)
    print("after convert:")
    print(df2.to_numpy())
    
    
 outputs:
    
       A          B    C  D      E    F
    0  1.0 2019-04-11  1.0  3   test  foo
    1  1.0 2019-04-11  1.0  3  train  foo
    2  1.0 2019-04-11  1.0  3   test  foo
    3  1.0 2019-04-11  1.0  3  train  foo
    after convert:
    [[1.0 Timestamp('2019-04-11 00:00:00') 1.0 3 'test' 'foo']
     [1.0 Timestamp('2019-04-11 00:00:00') 1.0 3 'train' 'foo']
     [1.0 Timestamp('2019-04-11 00:00:00') 1.0 3 'test' 'foo']
     [1.0 Timestamp('2019-04-11 00:00:00') 1.0 3 'train' 'foo']]
     
Note: DataFrame.to_numpy() does not include the index or column labels in the output.


- describe() shows a quick statistic summary of your data:


    import numpy as np
    import pandas as pd
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20190411'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'), 'D': np.array([3] * 4, dtype='int32'), 'E': pd.Categorical(["test", "train", "test", "train"]), 'F': 'foo'})
    print(df.describe())   

outputs:

                      A         B         C         D
    count  6.000000  6.000000  6.000000  6.000000
    mean  -0.138340 -0.221658  0.785762  0.685796
    std    0.810988  0.368206  0.356595  0.688125
    min   -1.232401 -0.648718  0.297851 -0.030942
    25%   -0.428714 -0.404668  0.512335  0.179292
    50%   -0.226481 -0.331579  0.862874  0.574514
    75%    0.027861 -0.062563  1.082150  1.013740
    max    1.238807  0.383852  1.140240  1.788988

Transposing your data:
    
    df.T
 
Sorting by an axis:

    df.sort_index(axis=1,ascending=False)
    
Sorting by values:

    df.sort_values(by='B')
    
### 3.2.3 Selection

Note: While standard Python / Numpy expressions for selecting and setting are intuitive and come in handy for
interactive work, for production code, we recommend the optimized pandas data access methods, .at, .iat, .loc
and .iloc.


See the indexing documentation Indexing and Selecting Data and MultiIndex / Advanced Indexing.


Getting

Selecting a single column, which yields a Series, equivalent to df.A:

    df['A']

Selecting via [], which slices the rows.
    
    df[0:3]
    
Selection by Label
See more in Selection by Label.

For getting a cross section using a label:
    
    df.loc[dates[0]]
    
Selecting on a multi-axis(多列) by label:
    
    df.loc[:, ['A', 'B']]
    
    
Showing label slicing, both endpoints are included:
    
     df.loc['20130102':'20130104', ['A', 'B']]
     
Reduction in the dimensions of the returned object:
    
    df.loc['20130102', ['A', 'B']]
    
For getting a scalar value:
    
    df.loc[dates[0], 'A']
    Out: 0.2508310832095117
For getting fast access to a scalar (equivalent to the prior method):
    
    df.at[dates[0], 'A']
    Out: 0.2508310832095117
    
Selection by Position
See more in Selection by Position.
Select via the position of the passed integers:

看到21页