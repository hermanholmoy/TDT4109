import random

def pop_random_song(songs):
    return songs[random.randint(0, len(songs)-1)]

songs = [("You hear the door slam. And realize there's nowhere left to", "run"),
         ("Oh, I wanna dance with somebody. I wanna feel the",  "heat"),
         ("There's a fire starting in my heart. Reaching a fever", "pitch"),
         ("Hey, I just met you and this is crazy. But here's my", "number"),
         ("'Cause baby, you're a firework. Come on, show 'em what you're", "worth")]


def pop_song(songs):
    n = random.randint(0, len(songs)-1)
    lyric = songs[n]
    res = []
    for song in songs:
        if song != lyric:
            res.append(song)
    return lyric

def get_input(song):
    print(song[0])
    guess = input("Hva er neste ord?")    
    return guess


def song_contest(songs):
    while True:
        song = pop_song(songs)
        songs.remove(song)
        guess = get_input(song)
        
        if guess == song[1]:
            print("Riktig!")
        else:
            print("Feil. Prøv igjen")
        
        if len(songs) == 0:
            print("Du gjettet alle!")
            break

        again = input("Vil du prøve igjen? (Y/N)")
        if again == "Y":
            pass
        else:
            print("Ferdig.")
            break


    

song_contest(songs)
