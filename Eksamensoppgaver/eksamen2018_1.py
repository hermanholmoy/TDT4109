#https://learn-eu-central-1-prod-fleet01-xythos.s3.eu-central-1.amazonaws.com/5def77a38a2f7/2957158?response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27TDT4110%25202018%2520sett%25202%25281%2529.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20201004T090000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5M5HI5WH%2F20201004%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=86be9387d185252223203211a2b12b6ccc91cd66200565d82815548ff9e2ea15

def menu():
    print(
        """
        Select task: 
        'i' to show the	highest	bid of an item,
        's' to save all winning bids to file,
        'q' to exit
    """
    )

    allowed_choices = ["i", "s", "q"]
    choice = input("Choice: ")

    if choice in allowed_choices:
        return choice
    else:
        return None


def item_offers(item, data):
    index = data[0].index(item)
    offers = [data[i][index] for i in range(1, len(data))]
    bidders = [data[i][0] for i in range(1, len(data))]

    res = []

    for i in range(len(offers)):
        res.append([bidders[i], offers[i]])

    return res


def item_winner(item, data):
    offers = item_offers(item, data)
    offers.sort(key=lambda x: x[1], reverse=True)
    winner = offers[0]
    return winner


def all_winners_dict(data):
    res = {}
    for item in data[0][1:]:
        winner = item_winner(item, data)
        res[item] = winner

    return res


sample_data = [
    ["Customer", "vase", "maleri", "tv"],
    ["Per", 100, 0, 1500],
    ["Ida", 110, 50, 1500],
    ["Ottar", 200, 600, 1700],
    ["Dag", 200, 600, 1700],
]


print(all_winners_dict(sample_data))