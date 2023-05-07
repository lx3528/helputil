import collections

def calhitratio(pred_list,label_list):
    '''
    input:
    pred_list:[user,item]
    label_list:[user,item]
    07:01

    label_list  里面有的结果的个数，平均值向下作为分母，其实是一个（n个）

    然后看下 pred_list 包含n个中的几个，k

    avg(k/n)

    0 user
    1 label的个数
    2 predlist中hit的个数

    
    '''
    print("input:pred_len:{} label_len:{}".format(len(pred_list),len(label_list)))

    #根据user聚合

    pred_user_map=collections.defaultdict(list)
    label_user_map=collections.defaultdict(list)

    input_list=[pred_list,label_list]
    output_list=[pred_user_map,label_user_map]

    for ind,_input in enumerate(input_list):
        for i in _input:
            user=i[0]
            item=i[1]
            output_list[ind][user].append(item)

    #cal hit ratio
    hit_sum=0
    for user in label_user_map:
        label_list=label_user_map[user]
        pred_list = pred_user_map[user]
        cross = set(label_list) & set(pred_list)
        cross_score = (len(cross)/len(label_list))
        #print("cross_score",cross_score)
        hit_sum+=cross_score

    return hit_sum/len(label_user_map)