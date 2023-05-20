/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let isThrottled=false;
    let nextArgs=undefined;
    return function(...args) {
        if(isThrottled){
            nextArgs=args;
        }else{
            fn(...args);
            isThrottled=true;
            setTimeout(helper,t);
        }

        function helper(){
            if(nextArgs){
                fn(...nextArgs);
                isThrottled = true;
                nextArgs=undefined;
                setTimeout(helper,t);
            }
            else{
                isThrottled=false;
            }
        }
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */