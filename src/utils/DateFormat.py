import datetime 

class DateFormat():

    @classmethod
    def convert_date(self, date):
        return datetime.datetime.strftime(date,'%d/%m/%Y')  # Se convierte la fecha a un formato específico
