#主体文件在这里。

class ShoppingList:  #创建一个购物清单类
    def __init__(self,name,list):  #初始化方法
        self.name = name
        self.list = list

    def caculate_total_price(self):
        total_price=0
        for price in self.list.values():
            total_price+=price
        return total_price
    
    def caculate_items_count(self):
        return len(self.list)

