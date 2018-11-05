#-*- coding:utf-8 -*-
class NaiveFilter():
    filter_list = []
    def __init__(self):
        pass
    def parse(self,name):
        with open(r'C:/Users/Yuning Xia/Desktop/week1-hxp/week1-hxp/keywords.txt', 'r',encoding='utf-8') as f:
            for line in f:
                self.filter_list.append(line.strip('\n'))
    def filter(self,message):
        clean_message = list(message)
        for keyword in self.filter_list:
            i = 0
            while i + len(keyword) <= len(message):
                if(message[i:i + len(keyword)]) == keyword:
                    clean_message[i:i + len(keyword)] = '*'
                    if i + len(keyword) + 1 <= len(message):
                        for j in range(i + len(keyword),len(message)):
                            clean_message[j] = clean_message[j - len(keyword) + 1]
                    i = i + len(keyword)
                else:
                    i += 1
        return ''.join(clean_message)
if __name__ == "__main__":
    f = NaiveFilter()
    f.parse("keywords")
    print(f.filter("弘扬正能量，从在宿舍说文明话做起"))
    print(f.filter("我他妈的"))
    print(f.filter("你日"))