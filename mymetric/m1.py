from sklearn import metrics
import numpy as np
"""
https://blog.csdn.net/weixin_38753213/article/details/114609950


"""


# auc
y_true = np.array([0, 1, 1, 1, 1])
y_score = np.array([0.4, 0.4, 0.55, 0.8, 0.7])
fpr, tpr, thresholds = metrics.roc_curve(y_true, y_score)
roc_auc = metrics.auc(fpr, tpr)
print("auc",roc_auc)

# 排序 逆序对！


# 辉哥 pr矩阵


#f1-score
from sklearn.metrics import f1_score

y_true = [1, 1, 1, 1, 2, 2, 2, 3, 3]
y_pred = [1, 1, 2, 3, 2, 2, 3, 2, 3]

f1_micro = f1_score(y_true, y_pred, average='micro')
f1_macro = f1_score(y_true, y_pred, average='macro')

print('f1_micro: {0}'.format(f1_micro))
print('f1_macro: {0}'.format(f1_macro))
print('f1-none',f1_score(y_true, y_pred, average=None))
print('f1-weight',f1_score(y_true, y_pred, average='weighted'))

y_true = [1, 1, 1, 1, 0,0,0,0]
y_pred = [1, 0,0,0,1,1,1,0]
print('f1-f1_micro',f1_score(y_true, y_pred, average='micro'))
print('f1-f1_macro',f1_score(y_true, y_pred, average='macro'))
print('f1-none',f1_score(y_true, y_pred, average=None))
print('f1-weight',f1_score(y_true, y_pred, average='weighted'))

from sklearn.metrics import precision_score,recall_score
y_true = [0, 1, 2, 1, 1, 2]
y_pred = [0, 2, 1, 1, 0, 1]

print('p-macro',precision_score(y_true, y_pred, average='macro')  )
print('p-micro',precision_score(y_true, y_pred, average='micro')    )
print('p-weight',precision_score(y_true, y_pred, average='weighted'))
print('p-None',precision_score(y_true, y_pred, average=None)   )

print('r-macro',recall_score(y_true, y_pred, average='macro')  )
print('r-micro',recall_score(y_true, y_pred, average='micro')    )
print('r-weight',recall_score(y_true, y_pred, average='weighted'))
print('r-None',recall_score(y_true, y_pred, average=None)   )


#推荐系统中的 MAP 评估指标
###不是多标签的，意义不大
def AP(ranked_list, ground_truth):
    """Compute the average precision (AP) of a list of ranked items
    ground_truth 表示是否正确的标识
    hits 表示 score （预测结果分值）倒排，从第0个到当前个的累计预测正确样本数
    sum_precs 表示每个 ground_truth = 1 的位置的 precision 的累加

    1  ||  1  ||  1/1=1
    2  ||  0  ||  0
    3  ||  1  ||  (1+1)/3=0.66
    4  ||  0  ||  0
    5  ||  0  ||  0
    6  ||  1  ||  (2+1)/6=0.5
    (1+0.66+0.5)/3 = 0.72
    """
    hits = 0
    sum_precs = 0
    for n in range(len(ranked_list)):
        if ranked_list[n] in ground_truth:
            hits += 1
            sum_precs += hits / (n + 1.0)
    if hits > 0:
        return sum_precs / len(ground_truth)
    else:
        return 0
# ————————————————
# 版权声明：本文为CSDN博主「xiedelong」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/xiedelong/article/details/112500657

#MAP(Mean Average Precision)
#为所有用户 u 的AP再取均值(mean)而已。那么计算公式如下：


'''
HR 关注准确性：
意义：关心用户想要的，我有没有推荐到，强调预测的“准确性”
hits(i):第i个用户访问的值是否在推荐列表中，是则为1，否则为0
HR= 1/N( sigmahits(i) )

MRR(平均倒数排名:关心是否放在了显眼的位置：
MRR = 1/N ( sigma 1~N (1/pi))

NDGC （归一化折损累计增益）
https://blog.csdn.net/shiaiao/article/details/109004341
NDGC = （1/N) sigma (i=1~N) 1/(log2(pi+1))

'''
def indicators_5(rankedList, testList):
    Hits_i = 0
    Len_R = 0
    Len_T = len(testList)
    MRR_i = 0
    HR_i = 0
    NDCG_i = 0
    for i in range(len(rankedList)):
        for j in range(len(rankedList[i])):
            if testList[i][0]==rankedList[i][j]:
                Hits_i+=1
                HR_i+=1
                # 注意j的取值从0开始
                MRR_i+=1/(j+1)
                NDCG_i+=1/(math.log2(1+j+1))
                break
    HR_i/=Len_T
    MRR_i/=Len_T
    NDCG_i/=Len_T
    print(Hits_i)
    #因为推荐列表就5个
    print(f'HR@5={HR_i}')
    print(f'MRR@5={MRR_i}')
    print(f'NDCG@5={NDCG_i}')



if __name__ == '__main__':
    import math

    # 推荐列表
    R = [[3, 10, 15, 12, 17], [20, 15, 18, 14, 30], [2, 5, 7, 8, 15], [56, 14, 25, 12, 19], [21, 24, 36, 54, 45]]
    # 用户访问列表
    T = [[12], [3], [5], [14], [20]]
    indicators_5(R, T)
    #ndgc torch
    #https://zhuanlan.zhihu.com/p/493958358
