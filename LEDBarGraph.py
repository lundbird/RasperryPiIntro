from gpiozero import LEDBarGraph
from time import sleep

graph = LEDBarGraph(17,27,22,5,6, pwm=True)
while (True):
    graph.value = 0
    sleep(.1)
    graph.value = 2/10  # (0.5, 0, 0, 0, 0)
    sleep(.1)
    graph.value = 4/10  # (1, 0.5, 0, 0, 0)
    sleep(.1)
    graph.value = 6/10  # (0, 0, 0, 0.5, 1)
    sleep(.1)
    graph.value = 8/10  # (1, 1, 1, 1, 0.5)
    sleep(.1)
    graph.value = 1 # (1, 1, 1, 1, 0.75)
    sleep(.1)
