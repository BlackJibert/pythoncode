# 简单排序

## 插入排序
摸牌的过程

void Insertion_Sort(ElementType A[], int N)
{
    for (int p=1,p<N,p++)
    {
        tmp = A[p] /*摸下张牌*/
        for (i=p,i>0 && A[i-1]>tmp,i--)
        {
            A[i] = A[i-1];/*移除空位*/
        }
        A[i] = tmp;/*新牌落位*/
    }
}


- 时间复杂度：最好：顺序,T=O(N)，最坏:逆序T = o(N^2)
好处：冒泡好，
从上到下依次比较，如何相等，不做交换，所以是稳定的。
