from datetime import date, time, datetime

def trabalhando_com_datetime() :
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%M - %H:%M:%S'))
    print(data_atual.strftime('%c'))


def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %m %Y')
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=16)
    print(horario)
    horario_str = (horario.strftime('%H:%M:%S'))
    print(horario_str)
    print(type(horario_str))


if __name__ == '__main__':
    #trabalhando_com_date()
    trabalhando_com_time()