/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null || object === undefined){
        return String(object);
    }
    if (Array.isArray(object)){
        const values = object.map((obj) => jsonStringify(obj));
        return `[${values.join(",")}]`;
    }

    if (typeof object === 'object'){
        const keys=Object.keys(object);
        const keyValPairs = keys.map((key)=>`"${key}":${jsonStringify(object[key])}`);
        return `{${keyValPairs.join(",")}}`;
    }

    if (typeof object === 'string'){
        return `"${String(object)}"`;
    }

    return String(object);
};