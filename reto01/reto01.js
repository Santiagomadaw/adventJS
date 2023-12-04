function findFirstRepeated(gifts) {
    for (let index = 1; index < gifts.length; index++) {
        if (gifts.slice(0, index).includes(gifts[index])) {
            return gifts[index];
        }
    }
    return -1;
}
