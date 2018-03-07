class item(object):
    def __init__(self, itemName, price, weight, brand):
        self.itemName = itemName;
        self.price = price;
        self.weight = weight;
        self.brand = brand;
        self.status = "for sale"
        #self.tax = self.addTax();
    
    def sold(self):
        self.status = "sold"
        return self;

    def addTax(self):
        self.tax = self.price * 0.08
        self.total = self.price + self.tax;
        return self;

    def returnProduct(self, returnState):
        self.returnState = returnState;
        if (self.returnState == 'defective'):
            self.status = 'defective';
            self.price = 0;
        elif (self.returnState == 'likeNew'):
            self.status = 'for sale';
            self.addTax();
        elif (self.returnState == 'opened'):
            self.status == 'used';
            self.price =  self.price - 0.20;
            self.addTax();
        return self;

    def display_all(self):
        print("Price:", self.price)
        if (self.price > 0):
            self.addTax();
            print("Taxes:", self.tax);
            print("Total:", self.total);
        else:
            print("No total; Do NOT sell")
        print("Status:", self.status);
        print("meta:")
        print("Brand:", self.brand);
        print("Weight:", self.weight);

yellowKing = item("The King In Yellow-A Cursed Play", 20, 1.5, "Lovecraft Publishing");

#yellowKing.display_all();

#yellowKing.sold().display_all();

yellowKing.returnProduct("defective").display_all();