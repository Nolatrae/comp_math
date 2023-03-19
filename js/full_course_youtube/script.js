/* const objectA = {
    a: 10,
    b:true
}
console.log(objectA)
//ссылки разные, которые хранят 1 объект
const copyOfA = objectA
copyOfA.a = 20 // меняем значение ссылочного типа(objectA)
copyOfA.c = 'abc' // добавили новое свойство к объекту
console.log(copyOfA)
console.log(objectA)  */

/////////////////////////////////////////////

//  const zalary = {
//   city: 'zalary'
//  }
// console.log(zalary)
// zalary.country = 'Russia'
// console.log(zalary)
// zalary.age = 123
// console.log(zalary)
// delete zalary.country
// console.log(zalary)
// zalary.user = {
//   name:'egor',
//   fam: 'Ezhov'
// }
// delete zalary.city
// console.log(zalary)
// console.log('свойство -', zalary.user.fam)

//////////////////////////////////////////////

// JSONzalary = JSON.stringify(zalary)
// console.log(JSONzalary)
// console.log(JSON.parse(JSONzalary))

//////////////////////////////////////////////

// const border = {
//   width: 1,
//   color: "black"
// }
// console.log(border)

// const info = {
//   info: "bla-bla-bla",
//   number: 123
// }

// const solidBorder = {
//   ...border,
//   ...info,
//   solid: "solid"
// }
// console.log(solidBorder)

////////////////////////////////

// const name = "egor"
// const city = "Irk"

// const sentence = `меня зовут ${name} и я живу в городе ${city}`

// console.log(sentence)

////////////////////////////////

const newPost = (post, addDate = Date()) => {
  let PostPam = JSON.parse(JSON.stringify(post))
  PostPam.date = addDate
  return PostPam
}

const firstPost = {
  id: 1,
  author : 'egor'
}

let fn = newPost(firstPost)
console.log(fn)

