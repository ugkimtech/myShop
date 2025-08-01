from Users.models import Expenditure, Status


class ExpenditureManager:
    def expend(self, amount, reason):
        Expenditure.objects.create(amount=amount, reason=reason)
        status = Status.objects.get(id=1)
        cash = status.available_cash - amount
        status.available_cash = cash
        dev = status.development - amount
        status.development = dev
        status.save()
        return