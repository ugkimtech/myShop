from Users.models import Expenditure, Status


class ExpenditureManager:
    def expend(self, amount, reason):
        Expenditure.objects.create(amount=amount, reason=reason)
        status = Status.objects.get(id=1)
        cash = float(status.available_cash) - amount
        status.available_cash = cash
        dev = float(status.development) - amount
        status.development = dev
        status.weight = cash + float(status.stock_amount)
        status.save()
        return