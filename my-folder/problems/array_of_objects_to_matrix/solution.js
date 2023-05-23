/**
 * @param {Array} arr
 * @return {Matrix}
 */
var jsonToMatrix = function(arr) {
    const keySet = new Set();

    for(const obj of arr){
      getKeys(obj,"");
    }

    const keys= Array.from(keySet).sort();
    const res=[keys];

    for(const obj of arr){
      const keyToVal = {};
      getValues(obj,"",keyToVal);
      let row = [];
      for (const key of keys){
        if (key in keyToVal){
          row.push(keyToVal[key]);
        }
        else{
          row.push("");
        }
      }
      res.push(row);
    }
    return res;

    function getKeys(obj,path){
      for(const key in obj){
        const newPath =  path ?  `${path}.${key}`:key;
        if(isObject(obj[key])){
          getKeys(obj[key],newPath)
        }
        else{
          keySet.add(newPath);
        }
      }
    }

    function getValues(obj,path,keyToVal){
      for(const key in obj){
        const newPath = path ?  `${path}.${key}`:key;
        if(isObject(obj[key])){
          getValues(obj[key],newPath,keyToVal)
        }
        else{
          keyToVal[newPath] = obj[key];
        }
      }
    }

    function isObject(obj){
      return obj !== null && typeof obj === 'object';
    }

};