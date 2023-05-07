/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let count_val=init;
    function increment(){
        count_val++;
        return count_val;
    }
    function decrement(){
        count_val--;
        return count_val;
    }
    function reset(){
        count_val=init;
        return count_val;
    }

    return{
        increment,
    decrement,
    reset
    };

};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */