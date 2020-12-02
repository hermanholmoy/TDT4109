import json
import os


GENRES = ("Action", "Adventure", "Adult", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Family", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Short", "Thriller", "War", "Western")
COUNTRIES = ("Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua & Deps", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Rep", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Congo {Democratic Rep}", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland {Republic}", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea North", "Korea South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", " {Burma}", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russian Federation", "Rwanda", "St Kitts & Nevis", "St Lucia", "Saint Vincent & the Grenadines", "Samoa", "San Marino", "Sao Tome & Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad & Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe")


def input_text(text, min_len, max_len):
    inp = input(text)
    while len(inp) > max_len or len(inp) < min_len:
        if len(inp) > max_len:
            print("     Text is too long!")
        else:
            print("     Text is too short!")
        inp = input(text)

    return inp


def input_num(prompt, min_num, max_num):
    inp = input(prompt)
    while True:
        try:
            inp = int(inp)
            if inp in range(min_num, max_num +1):
                return inp
            else:
                print(f"Must be a number between {min_num} and {max_num}.")
        except: 
            print("Must be an integer. ")

        inp = input(prompt)

    return inp


def input_selection(prompt, countries):
    inp = input(prompt)
    
    while inp not in countries:
        print("Not a valid choice.")
        xx = inp[0:min(2, len(inp))]
        print(f"Options that start with {xx}")
        for c in countries:
            if xx == c[:len(xx)]:
                print(c)

        inp = input(prompt)

    return inp


def enter_title():
    title = input_text("Title: ", 1, 100)
    year = input_num("Year: ", 1900, 2019)
    genre = input_selection("Genre: ", GENRES)
    agerating = input_num("Age rating (0-18): ", 0, 18)
    country = input_selection("Country: ", COUNTRIES)
    score = input_num("Score (0-100): ", 0, 100)
    comment = input_text("Comment: ", 10, 100)

    return (title, year, genre, agerating, country, score, comment)



def add_movies(db):
    inp = input("Do you want to enter a movie? (y/n) ")

    while inp != "n":
        data = enter_title()
        db[data[0]] = data[1:]
        inp = input("Do you want to add another movie? (y/n) ")

    return db


def save_movies(db):
    fname = input_text("Save database to filename (without filetype): ", 5, 20) + ".json"

    # try:
    #     with open(fname) as f:
    #         f.write(db)
    #         f.close()
    #     print(f"Database was saved to {fname}")
    # except error as e: 
    #     print(f"Database could not be saved to {fname}")

    with open(fname, "w") as f:
        json.dump(db, f)
        print(f"Database was saved to {fname}")

    

def load_movies(FILES):
    fname = input_selection("Load database from filename: ", FILES)

    try: 
        with open(fname, "r") as f:
            db = json.load(f)

        print(f"A database has been loaded from {fname}")
        return db
    except: 
        print(f"Could not load database from {fname}")
        

def show_movies(db):
    for title, data in db.items():
        title = title[:min(20, len(title))-1]
        year = data[0]
        genre = data[1][:min(10, len(data[1])-1)]
        country = data[3][:min(15, len(data[3])-1)]
        age = "Age: " + str(data[2])
        score = "Score: " + str(data[4]) + "%"
        print(year, title.ljust(20), genre.ljust(10), country.ljust(15), age.rjust(4), score.rjust(4))



db = {"Movie1": (2009, "Sci-Fi", 15, "Norway", 99, "Very good movie.")}
# db = add_movies(db)
# print(db)

# save_movies(db)
# db = load_movies(os.listdir())
# print(db)

show_movies(db)






