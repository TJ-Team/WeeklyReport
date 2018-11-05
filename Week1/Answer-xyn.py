class NaiveFilter():

    def __init__(self): 
    
        self.keywords = set([])


    def parse(self, path):

        for keyword in open(path, 'rb'):
            self.keywords.add(keyword.strip().decode('utf-8').lower())

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


