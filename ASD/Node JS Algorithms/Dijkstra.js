// Dijkstra algorithm on list adjacency

// PriorityQueue from: https://www.npmjs.com/package/priorityqueuejs
const PriorityQueue = require('priorityqueuejs')


// complexity:
// -time O(ElogV)
// -space O(V)

function getPath(parent,actual){
    let path = [actual]
    if (parent[actual] !== null){
        path = path.concat(getPath(parent,parent[actual]))
    } 
    return path
}


function relax(distance,parent,w,u,v) {
    if (distance[v] > distance[u] + w){
        parent[v] = u
        distance[v] = distance[u] + w
        return true
    }
    else {
        return false
    }
}


function Dijkstra(graph,b,e) {
    const n = graph.length
    // array of distances
    const distance = []
    for(i=0;i<n;i++){
        distance.push(Infinity)
    }
    distance[b] = 0
    // array to recreate a path
    const parent = []
    for(i=0;i<n;i++){
        parent.push(null)
    }

    const pQueue = new PriorityQueue(function(a,b) {return b-a})
    // adding all edges from beginig vertex
    graph[b].forEach(element => {
        let v = element[0] 
        let w = element[1] 
        // weight of edge, vertices
        pQueue.enq([w, b, v])
    })

    while (!pQueue.isEmpty()) {
        let element = pQueue.deq()
        let w = element[0]
        let u = element[1]
        let v = element[2]
        if (relax(distance, parent, w, u, v)){
            graph[v].forEach(element =>{
                let weight = element[1]
                let k = element[0]
                if(k != u){
                    pQueue.enq([weight,v,k])
                }
            })
        }
    }
    path = getPath(parent,e).reverse()
    // returning array total lowest distance, and path to get into
    return [distance[e], path]
}


graph = [
    [[1,1],[4,2],[5,3],[6,7]],
    [[0,1],[2,7],[4,3]],
    [[1,7],[3,6],[5,12]],
    [[2,6],[4,2]],
    [[0,2],[1,3],[3,2],[6,4]],
    [[0,3],[2,12]],
    [[0,7],[4,4]],
]

console.log(Dijkstra(graph,0,3))