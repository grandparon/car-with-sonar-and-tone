x1 = 0
x2 = 0
sonar_reading = 0
def avg_sonar():
    global x1, x2, sonar_reading
    x1 = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)
    basic.pause(100)
    x2 = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)
    basic.pause(100)
    sonar_reading = (x1 + x1) / 2

def on_forever():
    global x2
    basic.pause(200)
    avg_sonar()
    cuteBot.motors(15, 15)
    basic.pause(500)
    cuteBot.stopcar()
    cuteBot.motors(15, 0)
    cuteBot.stopcar()
    x2 = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)
    if x2 < sonar_reading:
        cuteBot.stopcar()
basic.forever(on_forever)
