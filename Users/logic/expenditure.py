from Users.models import Expenditure, Status


class ExpenditureManager:
    def expend(self, amount, reason):
        status = Status.objects.get(id=1)
        cash = status.available_cash - amount
        status.available_cash = cash
        dev = status.development - amount
        status.development = dev
        status.weight = cash + status.stock_amount
        status.save()
        Expenditure.objects.create(amount=amount, reason=reason)
        return