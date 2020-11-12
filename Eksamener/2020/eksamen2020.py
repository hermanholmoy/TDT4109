

def sec_to_time(s):
    hours = s // 3600
    rest_s = s % 3600
    mins = rest_s // 60
    secs = rest_s % 60

    if secs < 10:
        secs_str = "0" + str(secs)
    else:
        secs_str = str(secs)

    secs_str = "0" + str(secs) if secs < 10 else str(secs)
    mins_str = "0" + str(mins) if mins < 10 and hours > 0 else str(mins)

    if hours > 0:
        return ":".join([str(hours), mins_str, secs_str])
    else:
        return ":".join([mins_str, secs_str])


def time_to_sec(tstring):
    ledd = tstring.count(":")
    data = tstring.split(":")
    s = [1, 60, 3600]
    total_secs = 0

    for i, string in enumerate(reversed(data)):
        n = 0 if string == "" else int(string)
        total_secs += n * s[i]

    return total_secs


def enter_song():

    def check_format(data):
        if len(data) != 4:
            print("Invalid data. Format: Title;Artist;Genre;Duration")
            return False
        else:
            duration = data[3]
            mins, secs = duration.split(":")
            if int(mins) > 0 and int(secs) in range(0, 60):
                return True
            else:
                print("Duration has invalid format.")
                return False

    inp = input("Enter song (Title;Artist;Genre;Duration)")
    data = inp.split(";")
    while not check_format(data):
        inp = input("Enter song (Title;Artist;Genre;Duration)")
        data = inp.split(";")

    return data


def read_file(fname):
    with open(fname, "r") as f:
        data = f.read().split("\n")

    clean_data = [line.split(";") for line in data]

    return clean_data


def list_content(fname, choice):
    indexes = {
        "title": 0,
        "artist": 1,
        "genre": 2
    }

    if choice not in indexes.keys():
        return []

    data = read_file(fname)
    index = indexes[choice]
    res = [row[index] for row in data]

    return res


def list_songs_genre(fname):
    data = read_file(fname)
    genres = ["Rock", "Folk", "Blues", "Pop", "Country"]
    genre = input(f"Choose genre: ({', '.join(genres)}) ")

    if genre not in genres:
        return ([], "0:0")

    res = []
    for song in
