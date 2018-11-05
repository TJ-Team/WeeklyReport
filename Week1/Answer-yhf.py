# -*- coding: utf-8 -*-  

class NaiveFilter():
    lst=[]
    
    def __init__(self): 
        pass
    
    def parse(self, keywords):
        f=open ("keywords","r",encoding='utf-8')            
        
        for line in f:
            self.lst.append(line.strip('\n'))
    
    def filter(self, words):
        for key in self.lst:
            words = words.replace(key, '*')
        return(words)
        

if __name__ == "__main__":
        f = NaiveFilter()
        f.parse("keywords")
        
        # 举例：
        print (f.filter("弘扬正能量，从在宿舍说文明话坐起"))
        # 结果：弘扬正能量，从在宿舍说文明话坐起
        print (f.filter("我他妈的"))
        # 我*
        print (f.filter("你日"))
        # *
