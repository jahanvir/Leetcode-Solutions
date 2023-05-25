/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
   const ans=[];
   if (!Array.isArray(arr) || size <= 0) {
    return ans;
    }
   for(let x=0;x<arr.length;x+=size){
       var temp=[]
       for(let y=x;y<x+size && y < arr.length;y++){
           temp.push(arr[y]);
       }
       ans.push(temp);
   } 
   return ans;
};