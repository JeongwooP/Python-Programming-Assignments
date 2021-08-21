def meter_to_feet_yard(meter):
    feet=meter/0.305
    yard=meter/0.305
    message=print(meter,'meter 는',yard,'yard,',feet,'feet입니다')
    return message

meter=30
meter_to_feet_yard(meter)
