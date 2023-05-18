var TimeLimitedCache = function() {
    this.cache=new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const currentTime = Date.now();
    const expirationTime = currentTime+ duration;
    if(this.cache.has(key)){
        const [cachedValue,cachedExpiration] = this.cache.get(key);
        if (cachedExpiration > currentTime) {
            this.cache.set(key, [value, expirationTime]);
            return true; // Key already existed and is unexpired
        }
    }
    this.cache.set(key, [value, expirationTime]);
    return false

};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const currentTime = Date.now();
    if (!this.cache.has(key)) {
        return -1; // Key does not exist
    }
    const [value, expiration] = this.cache.get(key);
    if (expiration > currentTime) {
        return value; // Key exists and is unexpired
    }else{
        this.cache.delete(key);
        return -1;
    }
    
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let count = 0;
    const currentTime = Date.now();
    for (const [key,[_, expiration]] of this.cache) {
        if (expiration > currentTime) {
            count++;
        }
    }

    return count;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */