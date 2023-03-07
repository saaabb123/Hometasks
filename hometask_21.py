class Good:
    def __init__(self,item,price,quantity=1):
        self.item = item 
        self.price = price
        self.quantity = quantity

    def total_price(self):
        total_price = self.price * self.quantity
        return total_price 
    
    def __str__(self):

        return f"{self.item:<20} {self.price:>7.2f} *{self.quantity:>3} = {self.total_price():>5.2f}"
    

class DiscountGood(Good):
    def __init__(self,item,price,quantity=1,discount=0):
        super().__init__(item,price,quantity)
        self.discount = discount
            
    def total_price(self):
        return super().total_price() - super().total_price() * (self.discount/100)
        
    def __str__(self):
        return super().__str__() + "  (-{}%)".format(self.discount)
        # return super().__str__() + f"{-self.discount:>5}%"
     

class Cart:
    def __init__(self,goods_list):
        self.goods_list = goods_list

    
    def total_price(self):
        total_price = 0
        
        for good in self.goods_list:
            if isinstance(good,DiscountGood) and good.discount > 0:
                total_price += good.total_price()
            else:
                total_price += good.total_price()
            
        return total_price

    
    def display(self):
        print("{:<20} {:>7} {:>5} {:>6} {:>7}".format("Name","PPU","CNT","Price","Disc."))
        print("==================================================")
        for good in self.goods_list:
            print(good)
        print("==================================================")
        print("{:<30} {:>4} {:<10.2f}".format("Total", "=",self.total_price()))

    


goods = [
Good('Bread', 17, 3),
Good('Water', 19, 2),
DiscountGood('Juice', 80, 1, 20),
Good('Toilet Paper', 19, 10)
]

        
        
cart = Cart(goods)      
cart.display()






# item1 = DiscountGood("Juice",100,1,15)

# print(item1)