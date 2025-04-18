from music_notes import note
from machine import Pin, PWM
import time
buzzer = PWM(Pin(0))
def buzzer_on(freq):
    buzzer.freq(freq)
    buzzer.duty_u16(32768)
def buzzer_off():
    buzzer.duty_u16(0)
def buzz(freq, buzz_time):
    buzzer_on(freq)
    time.sleep(buzz_time)
    buzzer_off()
def play(Verse):
    for i in Verse:
        buzz(i, 0.2)
    time.sleep(0.2)
v1 = [note.d4, note.c4, note.sc4, note.skip, note.d4, note.sd4, note.e4, note.f4, note.f4, note.skip, note.f4, note.e4, note.f4, note.e4, note.sd4, note.d4, note.sd4, note.c4,]
v2 = [note.skip, note.c5, note.sc5, note.d5, note.sd5, note.d5, note.sc5, note.c5, note.skip,]
v3 = [note.a5, note.sg5, note.g5, note.skip, note.e5, note.d5, note.c5, note.sc5, note.sd5, ]
v4 = [note.sc5, note.b4, note.a4, note.b4, note.skip, note.sa4, note.a4, note.a4, note.sa4, note.sg4, note.g4, note.sf4, note.e4, note.sf4, note.g4, ]
v5 = [note.d4, note.sd4, note.e4, note.f4, note.sf4, note.sa4, note.a4, note.b4, ]
v6 = [note.skip, note.e4, note.e4, note.e4, note.f4, note.e4, note.f4, note.f4, note.e4, note.sf4, note.skip, ]
while True:
    play(v1)
    play(v2)
    play(v3)
    play(v2)
    play(v4)
    play(v6)
    play(v1)
    play(v5)
    play(v2)
    play(v4)
    print("done")
    break
