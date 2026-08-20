# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation

Encapsulation basically lets us bundle product details (productName, price stockQuantity) together with the code that handles them inside a Product class. Instead of letting anyone freely change these variables from anywhere in the program,we hide them and force changes to go through specific methods (such as updateStock() or setPrice()). This keeps our data safe from accidental bugs, like someone setting a negative item price or reducing stock below zero by mistake.

### 2. Abstraction

Abstraction helps simplify things by hiding the messy background calculations and giving us simple functions to work with. For ex, when a cashier uses a method like checkoutItem(productId, quantity), they don't need to see the underlying logic that calculates totals, deducts stock, or checks for low inventory. It keeps the rest of our code clean and manageable because we can then focus on what an object does rather than how it does.

### 3. Inheritance

Inheritance lets us build specialized product types without rewriting code we already made. We start with a main Product class for shared traits like name, price, and stock, and then create sub-classes like PerishableProduct (which adds an expirationDate) or BulkProduct (which adds a unitMeasurement). This saves us time, keeps our code organized, and eliminates unnecessary repetition across different inventory items.

### 4. Polymorphism

Polymorphism allows different objects to use the same method name but execute it in their own unique way. For instance, both regular and perishable items can call calculateDiscount(), but PerishableProduct can override this method to give a clearance discount if an item is close to expiring. It makes our system flexible because we can easily add new product rules without breaking existing checkout code.

## Reflection

Out of the four pillars, ENCAPSULATION is definitely the most useful for fixing up a sari-sari store system. In a small store, keeping track of exact stock levels and prices is everything, and Encapsulation makes sure nobody can accidentally mess up that data. By locking down variables like stock counts and only changing them through proper functions you stop glitches like negative inventory or accidental price changes from happening. It basically gives the code a built-in safet+y net, keeping the whole system reliable and accurate.



