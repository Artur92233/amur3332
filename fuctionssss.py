WORD = "hand"


def return_strings_with_hands(lists):
    for list in lists:
        if WORD in list:
            print(
                f"{list}"
            )


list = [
    ["arm" "shoulder", "finger"],
    ["arm", "hand", "shoulder", "finger"],
    ["arm", "shoulder", "finger"],
    ["arm", "hand", "shoulder"],
    ["hand", "shoulder", "finger"]
]

return_strings_with_hands(list)
