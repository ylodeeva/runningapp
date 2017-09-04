print ('Начнем с темпа!')
def pace():
  distance = input('Сколько км вы хотите пробежать? ')
  distance == float(distance)
  if True:
    print ('Отличная дистанция')
    time = input('Какое время вы хотите показать(ЧЧ:ММ:СС)? ')
    if len(time)==8:
      hours = time[:2]
      minutes = time[3:5]
      seconds = time[6:]
      hours == int(hours)
      if True:
        minutes==int(minutes)
        int(minutes)<60
        if True:
          seconds == int(seconds)
          int(seconds)<60
          if True:
            secs = (int(hours))*3600+(int(minutes))*60+int(seconds)
            pace_minutes = int(int(secs)// float(distance)/60)
            secs1=int(secs)-(int(pace_minutes)*float(distance))*60
            pace_secs = int(float(secs1)//float(distance))
            print (f'Чтобы пробежать {distance} км за {time}, ваш средний темп должен быть {pace_minutes} минут {pace_secs} секунд или быстрее')
          else:
            print ('Секунды заданы неверно')
        else:
          print ('Минуты заданы неверно')
      else:
        print ('Часы заданы неверно')
    else:
      print ('Значение некорректно')
  else:
    print ('Значение некорректно')
  
pace()
