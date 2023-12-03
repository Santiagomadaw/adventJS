function manufacture(gifts, materials) {
    let isAvailable = true;
    let availables = [];

    for (let i = 0; i < gifts.length; i++) {
        for (let j = 0; j < gifts[i].length; j++) {
            if (materials.includes(gifts[i][j])) {
                isAvailable = true;
            } else {
                isAvailable = false;
                break;
            }
        }

        if (isAvailable) {
            availables.push(gifts[i]);
        }
    }

    return availables;
}