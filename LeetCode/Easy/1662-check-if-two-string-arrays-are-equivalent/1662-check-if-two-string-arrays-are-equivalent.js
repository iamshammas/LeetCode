/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
var arrayStringsAreEqual = function(word1, word2) {
    let jW1 =word1.join('');
    let jW2 = word2.join('');
    let res = jW1==jW2 ? true : false;
    return res;
};