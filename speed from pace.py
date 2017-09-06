def speed():
  yourpace = input('Введите ваш темп(ММ:СС): ')
  if len(yourpace) == 5:
    p_mins = int(yourpace[:2])
    p_secs = int(yourpace[3:])
    if True:
      a = p_mins+(p_secs/60)
      speed1 = 60/a
      speed2= int((speed1%1)*100)/100
      speed=int(speed1)+speed2
      print(f'Ваша скорость = {speed} км/час')
  else:
    print ('Значение некорректно')
    
speed()
  
