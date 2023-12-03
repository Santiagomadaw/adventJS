function findFirstRepeated(gifts) {
    
    let firstIndex = gifts.length;

    for (let index = 0; index < gifts.length; index++) {
        for (let index2 = index + 1; index2 < gifts.length; index2++) {
            if (gifts[index] == gifts[index2] && index2 < firstIndex) {
                firstIndex = index2;
            }
        }
    }

    return firstIndex !== gifts.length ? gifts[firstIndex] : -1;
}

