
class Crop:

    def __init__(self, name ,category,crpno, price = 0) :
        self.name = name
        self.category = category
        self.crpno = crpno
        self.price = price
        
class Cropshop:

    crops = []
    selectedcrop = []

    def __init__(self, name, category,crpno, price):
        c = Crop(name,category,crpno = crpno,price= price )
        self.crops.append(c)
    
    def show(self):
        print("============== AVAILBALE CROPS ==========")
        
        pos=0

        for Crop in self.crops:
            print("============ ", pos, " ==========") 
            pos += 1   
            self.display(Crop)
            
    
    def select(self):
        print("========== SELECT A CATEGORY =======")
        print("====== ENTER THE NO OF ITEMS ======")
        neededCrops = int(input())

        for i in range(0, neededCrops ):
            print("====== INPUT THE CROP NO ======")
            selectedcrop = int(input())
            print("========== SELECTED A CATEGORY =======")
            c = self.getCropByNo(selectedcrop- 1)
            self.selectedcrop.append(c)
            print(self.display(c))

    def getCropByNo(self, position):
        return self.crops[position]

    def display(self, crop):
        print("Crop name  : ", crop.name)
        print("Crop category: ", crop.category)
        print("Crop Number : ", crop.crpno)
        print("Crop Price: ",crop.price)
       


    def selectedcrops(self):
        return self.selectedcrop


class BillCounter:

    crops = []
    def __init__(self, myCrops):
        self.crops = myCrops
    
    def display(self):
        pos = 0
        for crop in self.crops:
            print("============ BILL COUNTER CROPS ========")
            pos += 1
            print("============CROP NO", pos,"========")
            print("Crop name  : ", crop.name)
            print("Crop category: ", crop.category)
            print("Crop Number : ", crop.crpno)
            print("Crop Price: ",crop.price)
       

            

    def getTotal(self):
        total = sum(map(lambda c : c.price, self.crops))
        print("=========== GRAND TOTAL  =======")
        print(total)
    
    def getMax(self):
        total = max(map(lambda c : c.price, self.crops))
        print("=========== MAX PRICE =======")
        print(total)

    def getMin(self):
        total = min(map(lambda c : c.price  , self.crops))
        print("=========== MIN PRICE =======")
        print(total)


    def getCategory(self):
        print("================== CATEGORY  =============")
        categories = map(lambda d : d.category, self.crops)
        for category in categories  :
            print(category)
    

    def delete(self):
        print("=========== DO YOU WANT TO DELETE (if yes press 1,if no press 0)===============")
        choice = int(input())
        if (choice == 1):
            print("=========== WHICH CROP DO YOU WANT TO DELETE?  =======")
            cropno= int(input())
            self.crops.remove(self.getCropByNo(cropno))
        else:
            print("=========== NO CROPS =========")

    def getCropByNo(self, position):
        return self.crops[position - 1]

    
        
    
if "__MAIN__":
    print("========== WELCOME TO THE KRISHI SHOPPING ==========")

    cs = Cropshop("RICE","Crops","01",50)
    cs = Cropshop("TOMATO ","Vegetable","02",80)
    cs = Cropshop("NILGIRI","Plants","03",35)
    cs = Cropshop("CHERRY","Fruits","04",140)   
    cs = Cropshop("Big Chilli Seeds","Seeds","05",165)
    
    cs.show()

    cs.select()

    selectedCrops = cs.selectedcrops()
    
    print(selectedCrops)

    bc = BillCounter(selectedCrops)

    bc.display()

    bc.delete()

    bc.getTotal()

    bc.getMax()

    bc.getMin()

    bc.getCategory()

    

    