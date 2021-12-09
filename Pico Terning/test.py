from machine import Pin, Timer

led = Pin(25, Pin.OUT)
led0 = Pin(0, Pin.OUT)
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)
led4 = Pin(4, Pin.OUT)
led5 = Pin(5, Pin.OUT)
led6 = Pin(6, Pin.OUT)
led7 = Pin(7, Pin.OUT)
led8 = Pin(8, Pin.OUT)
led9 = Pin(9, Pin.OUT)

timer = Timer()

def blink(timer):
    led0.toggle()
    led1.toggle()
    led2.toggle()
    led3.toggle()
    led4.toggle()
    led5.toggle()
    led6.toggle()
    led7.toggle()
    led8.toggle()
    led9.toggle()


timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
