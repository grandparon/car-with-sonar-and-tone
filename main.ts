let x1 = 0
let x2 = 0
let sonar_reading = 0
function avg_sonar () {
    x1 = cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
    basic.pause(100)
    x2 = cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
    basic.pause(100)
    sonar_reading = (x1 + x1) / 2
    return sonar_reading
}
basic.forever(function () {
    basic.pause(200)
    avg_sonar()
    cuteBot.motors(15, 15)
    basic.pause(500)
    cuteBot.stopcar()
    cuteBot.motors(15, 0)
    cuteBot.stopcar()
    x2 = cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
    if (x2 < sonar_reading) {
        cuteBot.stopcar()
    }
})
