void Bubble_Sort(ElementType A[], int N)
{ for (p=N-1,p>=0;p--)

        for(int i = 0; i<p，i++)
        {   /*一趟排序*/
            if (A[i]>A[i+1])
            {
                Swap(A[i],A[i+1]);
            }
        }
    }
}

- 若中间一趟排序之后，已经出现有序

- 改进

void Bubble_Sort(ElementType A[], int N)
{ for (p=N-1,p>=0;p--)
        flag =0;
        for(int i = 0; i<p，i++)
        {   /*一趟排序*/
            if (A[i]>A[i+1])
            {
                Swap(A[i],A[i+1]);
                flag=1; /*标识发生了交换*/
            }
        }
        if (flag == 0) break;/*全程无交换*/
    }
}

- 时间复杂度：最好：顺序：T=O(N)，最坏，逆序， T = o(N^2)
好处：非常简单，对于数组和单向链表都是没有问题的。每次
从上到下依次比较，如何相等，不做交换，所以是稳定的。
