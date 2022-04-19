console.log(1)
//https://ischurov.github.io/pythonvjs/show/lists-arrays/en/

const o1 = {}
console.log(o1)



const array1 = [[1, 2], [3, 4]]
const flatArray1 = array1.flat()
console.log(flatArray1)




const array2 = [1, 2, 3]

map1 = array2.map(i => i * 2)
console.log(map1)

filter1 = array2.filter(i => i > 1)
console.log(filter1)










array2.forEach(i => {
    console.log(i)
})





const obj2 = {
    a: 1,
    b: 2,
    c: 3
}
Object.keys(obj2).forEach(o => {
    console.log(o)
})
Object.entries(obj2).forEach(([k, v]) => {
    console.log(k, v)
})
Object.values(obj2).forEach(v => {
    console.log(v)
})
const obj3 = Object.assign({}, {d: 4}, obj2)
console.log(obj3)
