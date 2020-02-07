
def re_arrange(str1, distance):
    d = {}
    for character in str1:
        if character not in d:
            d.update({character: 1})
        else:
            count = d.get(character)
            d.update({character: count + 1})

    input_ = []
    for key, value in d.items():
        input_.append(
            (key, value)
        )
    input_ = sorted(input_, key=lambda elmnt: elmnt[1], reverse=True)
    output = ["" for i in range(0, len(str1))]

    outer_idx = 0
    for elmnt in input_:
        count = elmnt[1]
        sub_idx = outer_idx
        cc = 0
        # char count
        while cc < count and sub_idx < len(output):
            if output[sub_idx] == "":
                output[sub_idx] = elmnt[0]
                sub_idx += 3
                cc += 1
            else:
                sub_idx += 1
        outer_idx += 1
    return "".join(output)
    

if __name__ == "__main__":
    str1 = "abcdadaeda"
    distance = 2
    print(re_arrange(str1, distance))