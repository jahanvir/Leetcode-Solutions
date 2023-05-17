/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function(functions, n) {

    let i=0;
    async function callback(){
        
        if(i===functions.length){
            return ;
        }
        await functions[i++]();
        await callback();
    }

    const nPromises = Array(n).fill().map(callback);
    await Promise.all(nPromises);
    

};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */