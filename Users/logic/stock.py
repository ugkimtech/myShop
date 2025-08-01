from Users.models import StockHistory, Status, ItemList, AvailableStock


class StockManager:

    def register_item(self, item):
        ItemList.objects.create(item = item)
        print('\n\n',item, 'saved\n\n')
        return


    def new_stock(self, item, qty, total_buying_price, selling_price_each, source, ):
        #this updates stock and status

        buying_price_each = (float(total_buying_price) / float(qty))
        profits_each = float(selling_price_each) - float(buying_price_each)
        total_selling_price = float(selling_price_each) * qty
        total_profits = float(total_selling_price) - float(total_buying_price)

        try:
            stock = AvailableStock.objects.get(item = item)
            stock.qty = float(stock.qty) + qty
            stock.buying_price_each = buying_price_each
            stock.selling_price_each = selling_price_each
            stock.profits_each = profits_each
            stock.save()
        except AvailableStock.DoesNotExist:
            AvailableStock.objects.create(
                item = item, 
                qty = qty,
                buying_price_each = buying_price_each,
                selling_price_each = selling_price_each,
                profits_each = profits_each
            )
        
        StockHistory.objects.create(
            item = item,
            qty = qty,
            total_buying_price = total_buying_price,
            buying_price_each = buying_price_each,
            selling_price_each = selling_price_each,
            profits_each = profits_each,
            total_selling_price = total_selling_price,
            total_profits = total_profits,
        )

        print('\n\nStock added')
        #update status
        self.update_busines_status(source, total_buying_price, total_profits)
        print('\n\nStatus updated')
        return True
    

    def update_busines_status(self, source, total_buying_price, total_profits):
        if source == 'internal':

            status = Status.objects.get(id = 1)
            new_available_cash = float(status.available_cash) - total_buying_price
            status.available_cash = new_available_cash
            new_stock_amount = float(status.stock_amount) + total_buying_price
            status.stock_amount = new_stock_amount
            status.save()

            status = Status.objects.get(id = 1)
            new_weight = status.available_cash + status.stock_amount
            status.weight = new_weight
            dev = status.development + total_profits
            status.development = dev
            status.save()
            return
        else:
            status = Status.objects.get(id = 1)
            new_stock_amount = status.stock_amount + total_buying_price
            status.stock_amount = new_stock_amount
            status.save()

            status = Status.objects.get(id = 1)
            new_weight = status.available_cash + status.stock_amount
            status.weight = new_weight
            dev = float(status.development) + float(total_profits)
            status.development = dev
            status.save()
            return