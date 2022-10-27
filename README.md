# LAB2B


https://user-images.githubusercontent.com/114169032/198328750-bc83e748-e7e6-47df-a3f3-6a067ac96de0.mp4

As the video shows, the main function is distance detection. When the distance is too close, flashing blue light, but can stop flashing by pressing the button. When the distance is at a safe distance, the yellow light is always on.

rp2040 is written in circuitpython. The two leds are connected to SDA and SCL respectively. The distance detection part is done with the help of APDS9960 used in Lab1.

`
led = digitalio.DigitalInOut(board.SDA)
`

`
led.direction = digitalio.Direction.OUTPUT
`

Above is the code added to connect the led to the SDA pin of the rp2040.

`led.value = True`

We can change the status of the led through `.value`.




## Components I used

Name  | quantity
------------- | -------------
Resistor(620 ohms) | 2
Led  | 2
Jumper wires  | many
6 Pin Self-Locking Push Button Switch | 1
Stemma Qt connector | 1
