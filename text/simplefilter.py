import re


#re 实践，真的是太多了！！！
puncs = "？?＂＃＄￥％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～?????、〃《》「」『』【】〔〕〖〗?????〝〞????–—‘’?“”??…?﹏."
pch="\·\;\:\t\n\f\!\@\#\$\%\^\&\*\(\)\[\]\{\}\-\_\=\`"
pch+=",\.\/\+\-\*\?\>\<\'\" "
puncs2 = puncs+pch

nore="2090(?P<nor>[A-Za-z0-9%s]*)"%(puncs2)#如果多个2090 会怎么版？
# resu=re.search(nore,name)
# while resu:
#     nametem=name[:a.span(0)[0]]
#     if len(name)!=a.span(0)[1]:
#         nametem+=name[a.span(0)[1]:]
#     resu=re.search(nore,nametem)
#     name=nametem
## 挖掘书名号
rule_one = r'[《](.*?)[》]'
rule_two = [r'(.*?)[》】」』〗〕\]>]', r'[《ㄍㄑ<【「『〖〔[](?=[^ ]+$)(.*?)$']
rule_three = [r'[[|(|【](.*?)[]|】]', r'[[|【](.*?)[】|]]']

#https://blog.csdn.net/sophicchen/article/details/107338777
pa = re.compile(rule_one)
query = "暗恋有了美好的结局，《圣少女》结局太暖心了"
#match只能匹配开头
print(pa.match(query))

print(pa.search(query))
print(pa.search(query).group())

