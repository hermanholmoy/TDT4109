def do_user_like(l):
    res = []
    print("On a scale from 1-10, how much do you like: ")
    for item in l:
        like = int(input(f"{item}? "))

        while like not in range(1, 11):
            print("Please enter a valid number. ")
            like = int(input(f"{item}? "))
        res.append((item, like))

    return res


def get_prioritized_list(l):
    s = sorted(l, key=lambda t: (-t[1], t[0]))
    return s



def what_user_likes_best(items, num):

    if int(num) not in range(1, len(items)):
        print("Not a valid number.")
        return 
    else:
        likes = do_user_like(items)
        sorted_likes = get_prioritized_list(likes)
        print(f"Your top {num}: ")
        for i, item in enumerate(sorted_likes[:int(num)]):
            print(f"{i+1}. {item[0]}")


tl = ["Dogs", "Cats", "Chocolate", "Pancakes", "Ice Cream"]
what_user_likes_best(tl, 3)




tl = [("Dogs", 10), ("Cats", 10), ("Chocolate", 10), ("Pancakes", 7), ("Ice Cream", 4)]

