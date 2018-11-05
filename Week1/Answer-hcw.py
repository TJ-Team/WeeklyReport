# -*- coding: utf-8 -*-  

class NaiveFilter():
        
    prase_list=[]
        # 初始化
    def __init__(self): 
        pass
    
        # 将文件中的词汇输入到集合/列表中
    def parse(self,keywords):
        f=open("keywords","r",encoding='utf-8')            
        
        for line in f:
            self.prase_list.append(line.strip('\n'))
        print(self.prase_list)
    
        # 将脏话过滤
    def filter(self,words):
        prase_index=[]
        for keyword in self.prase_list:
            length,i = len(keyword),0
            while i+length <= len(words):
                if(words[i:i+length])==keyword:
                    prase_index.append((i,length))
                    i = i+length
                else:
                    i = i+1
                
            
        temp=list(words)
        for pair in reversed(prase_index):
            temp[pair[0]:pair[0]+pair[1]]='*'
            
        
        return ''.join(temp)     
        
        
        
        
       
            
    
            


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