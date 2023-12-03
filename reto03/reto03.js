function findNaughtyStep(original, modified) {
    function difference(str1, str2) {
        if (str2 === '') {
            return str1[0];
        }
        for (let i = 0; i < str2.length; i++) {
            if (str1[i] !== str2[i]) {
                return str1[i];
            }
        }
        return str1[str1.length - 1];
    }

    if (original.length > modified.length) {
        return difference(original, modified);
    } else if (modified.length > original.length) {
        return difference(modified, original);
    } else {
        return '';
    }
}