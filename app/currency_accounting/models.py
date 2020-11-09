from django.db import models

# Create your models here.



class CurrencyInfo(models.Model):
    __tablename__ = "currency_info"

    bank_currency=models.FloatField(max_length=20, default=0, null=True)
    market_currency=models.FloatField(max_length=20, default=0, null=True)
    value = models.FloatField(max_length=255, default=0, null=True)

    def __repr__(self):
        return (
           f"{self.__tablename__}:<bank_currency: {self.bank_currency}, market_currency: {self.market_currency}"
           f", value: {self.value}>"
        )