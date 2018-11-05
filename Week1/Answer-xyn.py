"""
题目：鉴于愈加严峻的形势，请大家写一个专属于527的脏话过滤器2333
要求：只要给出文本中的脏话词汇被说出，就要用“*”号替换掉
提示：
（1）使用set()或list()
（2）运用打开文件的操作
（3）全靠自觉哈，明早八点前上传代码到群
（4）这次是第一次，有需要改进的地方尽管提，但尽量会放在下次的考核中，避免影响本次考核
（5）要不这样，每周由管券(rmb)的人出题，大家解题，题目不难，只起督促作用
样例参考
模板.txt
keywords
"""
class NaiveFilter():

    def __init__(self): 
        # 设置成set
        self.keywords = set([])


    def parse(self, path):
        # 
        for keyword in open(path, 'rb'):
            self.keywords.add(keyword.strip().decode('utf-8').lower())
        #检查str是否在文件中
        #print("好的" in self.keywords) 

    def filter(self, message, repl="*"):
        message = str(message).lower()
        for kw in self.keywords:
            message = message.replace(kw, repl)
        return message

if __name__ == "__main__":
    f = NaiveFilter()
    f.parse("keywords")

    print (f.filter("弘扬正能量，从在宿舍说文明话坐起"))
    # 结果：弘扬正能量，从在宿舍说文明话坐起
    print (f.filter("我他妈的"))
    # 我*
    print (f.filter("我日"))
    # *


