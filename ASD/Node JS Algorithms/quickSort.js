// quick sort algorithm

// complexity:
// -time O(NlogN)
// -space -> recurstion stack size


// swap of elements
function swap(array,a,b){
    let tmp = array[a]
    array[a] = array[b]
    array[b] = tmp
}


function partition(array,l,r){
    let pivot = array[r]
    let limit = l-1
    for(i=l;i<r;i++){
        if (array[i] < pivot){
            limit ++
            swap(array, limit, i)
        }
    }
    swap(array, limit+1, r)
    return limit + 1
}


function quickSort(array,l=0,r=null){
    if (r === null) r = array.length-1
    if (l < r){
        let p = partition(array,l,r)
        quickSort(array,l,p-1)
        quickSort(array,p+1,r)
    }
}


const array = [3,2,1,5,4,0,9,10,6]
quickSort(array,0,array.length-1)
console.log(array)
