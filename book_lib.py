import sys
from pymongo import MongoClient
class Book:
    def __init__(self,lname,lid,sname,sno,amount=0):
        self.lname=lname
        self.lid=lid
        self.sname=sname
        self.sno=sno
        self.amount=amount
    def create(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client[self.lname]
        A_name=str(input("Enter the Author name:"))
        coll=dp[A_name]
        b_name=str(input("Enter the Book name:"))
        b_number=int(input("Enter how many Books:"))
        b_amount=int(input("Enter the Book Amount:"))
        coll.insert_one({"Book_Name":b_name,"Author_name":A_name,"Book_count":b_number,"Library_name":self.lname,"Library_id":self.lid,"amount":b_amount})
    def view(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client[self.lname]
        A_name=str(input("Enter the Author name:"))
        coll=dp[A_name]
        fin={"Author_name":A_name}
        for x in coll.find({},{"Book_Name":1,"Author_name":1,"Book_count":1,"Library_name":1,"Library_id":1,"amount":1}):
            print("Book_Name:",x["Book_Name"])
            print("Author_name:",x["Author_name"])
            print("Book_count:",x["Book_count"])
            print("amount:",x["amount"])
            print("Library_name:",x["Library_name"])
            print("Library_id:",x["Library_id"])
            print("\t=======================================================================================")
            
            
    def arrange(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client[self.lname]
        A_name=str(input("Enter the Author name:"))
        coll=dp[A_name]
        sor=coll.find().sort("Book_Name")
        for x in sor:
            print("Book_Name:",x["Book_Name"])
            print("Author_name:",x["Author_name"])
            print("Book_count:",x["Book_count"])
            print("amount:",x["amount"])
            print("Library_name:",x["Library_name"])
            print("Library_id:",x["Library_id"])
            print("\t=======================================================================================")
    def darrange(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client[self.lname]
        A_name=str(input("Enter the Author name:"))
        coll=dp[A_name]
        sor=coll.find().sort("Book_Name",-1)
        for x in sor:
            print("Book_Name:",x["Book_Name"])
            print("Author_name:",x["Author_name"])
            print("Book_count:",x["Book_count"])
            print("amount:",x["amount"])
            print("Library_name:",x["Library_name"])
            print("Library_id:",x["Library_id"])
            print("\t=======================================================================================")
    def buy(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client[self.lname]
        A_name=str(input("Enter the Author name:"))
        coll=dp[A_name]
        bn=str(input("Enter the book name to find:"))
        fn={"Book_Name":bn}
        fb=coll.find(fn)
        for x in fb:
            no=x["Book_count"]
            if no!=0:
                cou=int(input("how many books you want:"))
                mins=no-cou
                print("\t\t==Remaining Book is ==",mins)
                up={"$set":{"Book_count":mins}}
                coll.update_one(fn,up)
                af={"Book_Name":bn}
                ab=coll.find(af)
                for z in ab:
                    t=z["amount"]
                    total=t*cou
                    print(f" \t\t you purchesd {cou} books and the amount is {total}")
                    self.amount+=total
                    print(f" \t\t your bill total is over all purchesed {self.amount}" )
                    cn=client["Customer"]
                    cos_n=cn[self.sname]
                    cos_n.insert_one({"C_name":self.sname,"C_phone":self.sno,"B_name":bn,"B_rate":t,"N_book_brought":cou,"total":total,"O_all_rate":self.amount})
                    
            else:
                print("=== The Book is out of Stock!!!!===")
    def buyer_details(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Customer"]
        A_name=str(input("Enter the Customer name to find:"))
        coll=dp[A_name]
        for x in coll.find({}):
            print("C_name:",x["C_name"])
            print("C_phone:",x["C_phone"])
            print("B_name:",x["B_name"])
            print("B_rate:",x["B_rate"])
            print("N_book_brought:",x["N_book_brought"])
            print("total:",x["total"])
            print("O_all_rate:",x["O_all_rate"])
            print("\t=======================================================================================")
            
    def main(self):
        print(f"\t {1}-->if you want to insert the Book \n\t {2}-->To View the books \n\t {3}-->To see A-Z order the Book \n\t {4}-->To see Z-A order the book \n\t {5}--> To Buy the Book \n\t {6}-->To Buyer Details \n\t {7}-->Quit")
        number=int(input("enter the option:"))
        if number==1:
            q=int(input("how many books you want to insert:"))
            for i in range(0,q):
                b.create()
        elif number==2:
            b.view()
        elif number==3:
            b.arrange()
        elif number==4:
            b.darrange()
        elif number==5:
            b.buy()
        elif number==6:
            b.buyer_details()
        elif number==7:
            print("\t\t You are exit the application now!!!")
            sys.exit("------------------------")
ln=str(input("Enter the library name:"))
li=int(input("Enter the library id:"))
na=str(input("Enter the Buyer Name:"))
nn=int(input("Enter the Buyer Phone Number:"))
b=Book(ln,li,na,nn)
while(True):
    b.main()
        
        
        
        
