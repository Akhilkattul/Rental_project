class user:
    def __init__(self,U_name,U_id,c_name) -> None:
        self.U_name=U_name
        self.U_id=U_id
        self.c_name=c_name
    
    def __str__(self) -> str:
        return self.U_name+' || '+str(self.U_id)+' || '+self.c_name+'\n'
    