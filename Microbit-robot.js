serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    command = serial.readLine()
    distance = parseFloat(command.substr(7, command.length))
    direction = command.substr(0, 4)
    Speed_Char = command.substr(5, 1)
    if (Speed_Char == "S") {
        Speed = Slow_Speed
        Coeff = Slow_Speed_Coeff
    } else if (Speed_Char == "M") {
        Speed = Medium_Speed
        Coeff = Medium_Speed_Coeff
    } else {
        Speed = Fast_Speed
        Coeff = Fast_Speed_Coeff
    }
    if (direction == "LEFT") {
        left(distance * Angle_Duration_Left_90 / 90)
        stop(1)
    } else if (direction == "RGHT") {
        right(distance * Angle_Duration_Right_90 / 90)
        stop(1)
    } else if (direction == "FRWD") {
        forward(distance * Coeff, Speed)
        stop(1)
    } else if (direction == "BKWD") {
        backward(distance * Coeff, Speed)
        stop(1)
    } else {
        stop(1)
    }
})
function forward(distance: number, speed: number) {
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED1, 0, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED2, speed, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED3, 0, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED4, speed, 67)
    basic.pause(distance)
}
function backward(distance: number, speed: number) {
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED1, 100, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED2, speed, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED3, 100, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED4, speed, 67)
    basic.pause(distance)
}
maqueen.IR_callbackUser(function ({ myparam: message }) {
    val = message
    if (val == 70) {
        forward(2, Fast_Speed)
    }
    if (val == 68) {
        left(90)
    }
    if (val == 67) {
        right(90)
    }
    if (val == 21) {
        backward(2, Fast_Speed)
    }
    if (val == 64) {
        stop(1)
    }
})
function left(angle: number) {
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED1, 0, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED2, 0, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED3, 0, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED4, 60, 67)
    basic.pause(angle)
}
function right(angle: number) {
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED1, 0, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED2, 60, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED3, 0, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED4, 0, 67)
    basic.pause(angle)
}
function stop(duration: number) {
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED1, 0, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED2, 0, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED3, 0, 67)
    PCA9685.setLedDutyCycle(PCA9685.LEDNum.LED4, 0, 67)
    basic.pause(duration)
}
let direction = ""
let distance = 0
let command = ""
let Coeff = 0
let Speed = 0
let Speed_Char = ""
let Slow_Speed_Coeff = 0
let Slow_Speed = 0
let Medium_Speed_Coeff = 0
let Medium_Speed = 0
let Fast_Speed_Coeff = 0
let Fast_Speed = 0
let Angle_Duration_Right_90 = 0
let Angle_Duration_Left_90 = 0
let val = 0
val = 0
Angle_Duration_Left_90 = 400
Angle_Duration_Right_90 = 520
Fast_Speed = 100
Fast_Speed_Coeff = 13.5
Medium_Speed = 75
Medium_Speed_Coeff = 20
Slow_Speed = 50
Slow_Speed_Coeff = 27
Speed_Char = "S"
Speed = Slow_Speed
Coeff = Slow_Speed_Coeff
serial.redirectToUSB()
PCA9685.init(67, 0)
basic.forever(function () {

})
