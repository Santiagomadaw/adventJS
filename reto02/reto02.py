def manufacture(gifts, materials):
    is_avaiable = True
    avaiables = []
    for gift in gifts:
        for char in gift:
            if char in materials:
                is_avaiable = True
            else:
                is_avaiable = False
                break
        if is_avaiable:
            avaiables.append(gift)
    return avaiables