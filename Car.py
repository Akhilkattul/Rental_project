class car:
    def __init__(self,C_name,p_no,price,avail,num,rented=0) -> None:
        self.C_name=C_name
        self.p_no=p_no
        self.price=price
        self.avail=avail
        self.num=num
        self.rented=rented
    
    def __str__(self) -> str:
        return self.C_name+' || '+self.p_no+' || '+str(self.price)+" || "+str(self.avail)+" || "+ str(self.num) + ' || '+ str(self.rented)+"\n"