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