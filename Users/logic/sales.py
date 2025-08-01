from Users.models import AvailableStock, Status, Sales


class SalesManager:
    def add_sale(self, item, quantity):
        stock = AvailableStock.objects.get(item = item)
        #update stock
        if stock.qty >= quantity:
            new_stock = float(stock.qty) - quantity
            stock.qty = new_stock
            stock.save()

            amount = float(stock.selling_price_each) * quantity
            profits = float(stock.profits_each) * quantity
            Sales.objects.create(item=item, quantity=quantity, amount=amount, profits=profits)

            #update status
            status = Status.objects.get(id = 1)
            new_available_cash = float(status.available_cash) + amount
            status.available_cash = new_available_cash
            new_stock_amount = float(status.stock_amount) - amount
            status.stock_amount = new_stock_amount
            status.save()
            return True
        return False