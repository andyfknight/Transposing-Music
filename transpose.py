def transpose(song, goal_key):
    notes = ("C,Db,D,Eb,E,F,Gb,G,Ab,A,Bb,B," * 2).split(",")
    starting_key, song = song.split(".")
    song = song.split(",")
    starting_key_pos = notes.index(starting_key)
    shift = notes[starting_key_pos:].index(goal_key)
    result = []
    for chord in song:
        if "m" in chord:
            result.append(notes[notes.index(chord[:-1]) + shift] + "m")
        else:
            result.append(notes[notes.index(chord) + shift])
    return song, shift, ",".join(result)

s1 = "F.C,F,Dm,Gm,C,F,Dm,Gm,C,F,Dm,Bb,C,F,Dm,Gm,C"
s2 = "Eb.Eb,Gm,Ab,Eb,Gm,Ab,Bb7,Eb,Gm,Ab,Eb,Cm,Eb,Ab,Eb"

print(transpose(s1, "A"))