class inv_item(object):
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

    def productDict(self):
        self.prodDict = {}

        self.prodDict["itemName"] = self.itemName;
        self.prodDict["price"] = self.price;
        self.prodDict["weight"] = self.weight;
        self.prodDict["brand"] = self.brand;
        #self.prodDict["tax"] = self.add_tax;
        #self.prodDict["total"] = self.total;
        return self.prodDict;

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

yellowKing = inv_item("The King In Yellow-A Cursed Play", 20, 1.5, "Lovecraft Publishing");

#print(yellowKing.productDict());

#yellowKing.sold().display_all();

#yellowKing.returnProduct("").display_all()

class Store(object):
    def __init__(self, owner, location):
        self.owner = owner;
        self.location = location;
        self.products = [];

    def add_product(self, itemName, price, weight, brand):
        temp_prods = inv_item(itemName, price, weight, brand)
        #print(prods)
        self.products.append(temp_prods)
        #print(vars(self.products))
        return self

    def remove_product(self, itemName):
        for item in range(0, self.products):
            if (self.products[item].itemName == itemName):
                self.products.remove(self.products[item].itemName);

    def displayInv(self):
        for items in self.products:
            print(vars(items))

Curiousities = Store("Wilbert Whatley", "Northside")

Curiousities.add_product("The King In Yellow-A Cursed Play", 20, 1.5, "Lovecraft Publishing");
Curiousities.add_product("Holy Water", 2, 5, "Saint Mary's Cathedral")

Curiousities.remove_product("The King In Yellow-A Cursed Play")
Curiousities.displayInv();
