/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var commonFactors = function(a, b) {
    function tets(n) {
    res =[];
    for (let i=1;i<=n;i++) {
        if (n%i == 0){
            res.push(i)
        }
    }
    return res;
}
less12 = tets(a);
less6 = tets(b);


let ccm = [];
for(let w of less12) {
    if(less6.includes(w))
    ccm.push(w)
}

return ccm.length;

};