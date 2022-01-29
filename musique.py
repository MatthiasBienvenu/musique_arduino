notes = str(input("notes : ")) ; notes = notes.split()
delay = str(input("temps après note : ")) ; delay = delay.split()
duree = str(input("durées : ")) ; duree = duree.split()
frequence = 0
error = 0
for i in range (len(notes)):
    k = notes[i]
# ---------- octave -2 ----------
    if k == "la-2" or k == "a0":
        frequence = 27
    elif k == "la-2#" or k == "a0#":
        frequence = 29
    elif k == "si-2" or k == "b0":
        frequence = 31
# ---------- octave -1 ----------
    elif k == "do-1" or k == "c1":
        frequence = 33
    elif k == "do-1#" or k == "c1#":
        frequence = 35
    elif k == "re-1" or k == "d1":
        frequence = 37
    elif k == "re-1#" or k == "d1#":
        frequence = 39
    elif k == "mi-1" or k == "e1":
        frequence = 41
    elif k == "fa-1" or k == "f1":
        frequence = 44
    elif k == "fa-1#" or k == "f1#":
        frequence = 46
    elif k == "sol-1" or k == "g1":
        frequence = 49
    elif k == "sol-1#" or k == "g1#":
        frequence = 52
    elif k == "la-1" or k == "a1":
        frequence = 55
    elif k == "la-1#" or k == "a1#":
        frequence = 58
    elif k == "si-1" or k == "b1":
        frequence = 62
# ---------- octave 1 ----------
    elif k == "do1" or k == "c2":
        frequence = 65
    elif k == "do1#" or k == "c2#":
        frequence = 69
    elif k == "re1" or k == "d2":
        frequence = 73
    elif k == "re1#" or k == "d2#":
        frequence = 78
    elif k == "mi1" or k == "e2":
        frequence = 82
    elif k == "fa1" or k == "f2":
        frequence = 87
    elif k == "fa1#" or k == "f2#":
        frequence = 92
    elif k == "sol1" or k == "g2":
        frequence = 98
    elif k == "sol#1" or k == "g2#":
        frequence = 104
    elif k == "la1" or k == "a2":
        frequence = 110
    elif k == "la1#" or k == "a2#":
        frequence = 117
    elif k == "si1" or k == "b2":
        frequence = 123
# ---------- octave 2 ----------
    elif k == "do2" or k == "c3":
        frequence = 131
    elif k == "do2#" or k == "c3#":
        frequence = 139
    elif k == "re2" or k == "d3":
        frequence = 147
    elif k == "re2#" or k == "d3#":
        frequence = 156
    elif k == "mi2" or k == "e3":
        frequence = 165
    elif k == "fa2" or k == "f3":
        frequence = 175
    elif k == "fa2#" or k == "f3#":
        frequence = 185
    elif k == "sol2" or k == "g3":
        frequence = 196
    elif k == "sol2#" or k == "g3#":
        frequence = 208
    elif k == "la2" or k == "a3":
        frequence = 220
    elif k == "la2#" or k == "a3#":
        frequence = 233
    elif k == "si2" or k == "b3":
        frequence = 247
# ---------- octave 3 ----------
    elif k == "do3" or k == "c4":
        frequence = 262
    elif k == "do3#" or k == "c4#":
        frequence = 277
    elif k == "re3" or k == "d4":
        frequence = 294
    elif k == "re3#" or k == "d4#":
        frequence = 311
    elif k == "mi3" or k == "e4":
        frequence = 330
    elif k == "fa3" or k == "f4":
        frequence = 349
    elif k == "fa3#" or k == "f4#":
        frequence = 370
    elif k == "sol3" or k == "g4":
        frequence = 392
    elif k == "sol3#" or k == "g4#":
        frequence = 415
    elif k == "la3" or k == "a4":
        frequence = 440
    elif k == "la3#" or k == "a4#":
        frequence = 466
    elif k == "si3" or k == "b4":
        frequence = 494
# ---------- octave 3 ----------
    elif k == "do4" or k == "c5":
        frequence = 523
    elif k == "do4#" or k == "c5#":
        frequence = 554
    elif k == "re4" or k == "d5":
        frequence = 587
    elif k == "re4#" or k == "d5#":
        frequence = 622
    elif k == "mi4" or k == "e5":
        frequence = 659
    elif k == "fa4" or k == "f5":
        frequence = 698
    elif k == "fa4#" or k == "f5#":
        frequence = 740
    elif k == "sol4" or k == "g5":
        frequence = 784
    elif k == "sol4#" or k == "g5#":
        frequence = 831
    elif k == "la4" or k == "a5":
        frequence = 880
    elif k == "la4#" or k == "a5#":
        frequence = 932
    elif k == "si4" or k == "b5":
        frequence = 988
# ---------- octave 5 ----------
    elif k == "do5" or k == "c6":
        frequence = 1047
    elif k == "do5#" or k == "c6#":
        frequence = 1109
    elif k == "re5" or k == "d6":
        frequence = 1175
    elif k == "re5#" or k == "d6#":
        frequence = 1245
    elif k == "mi5" or k == "e6":
        frequence = 1319
    elif k == "fa5" or k == "f6":
        frequence = 1397
    elif k == "fa5#" or k == "f6#":
        frequence = 1480
    elif k == "sol5" or k == "g6":
        frequence = 1568
    elif k == "sol5#" or k == "g6#":
        frequence = 1661
    elif k == "la5" or k == "a6":
        frequence = 1760
    elif k == "la5#" or k == "a6#":
        frequence = 1865
    elif k == "si5" or k == "b6":
        frequence = 1976
# ---------- octave 6 ----------
    elif k == "do6" or k == "c7":
        frequence = 2093
    elif k == "do6#" or k == "c7#":
        frequence = 2217
    elif k == "re6" or k == "d7":
        frequence = 2349
    elif k == "re6#" or k == "d7#":
        frequence = 2489
    elif k == "mi6" or k == "e7":
        frequence = 2637
    elif k == "fa6" or k == "f7":
        frequence = 2794
    elif k == "fa6#" or k == "f7#":
        frequence = 2960
    elif k == "sol6" or k == "g7":
        frequence = 3136
    elif k == "sol6#" or k == "g7#":
        frequence = 3322
    elif k == "la6" or k == "a7":
        frequence = 3520
    elif k == "la6#" or k == "a7#":
        frequence = 3729
    elif k == "si6" or k == "b7":
        frequence = 3951
# ---------- octave 7 ----------
    elif k == "do7" or k == "c8":
        frequence = 4186
    else :
        error = 1
    if error == 1:
        print(f"la valeur {notes[i]} n'est pas correcte.")
        error = 0
    elif i == 0:
        print(f"\n\nCode en C++ :\n\ntone(A0, {frequence}, {duree[i]});\n  delay({delay[i]});")
    else :
        print(f"  tone(A0, {frequence}, {duree[i]});\n  delay({delay[i]});")