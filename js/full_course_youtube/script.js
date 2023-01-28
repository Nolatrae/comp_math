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

 const zalary = {
  city: 'zalary'
 }
console.log(zalary)
zalary.country = 'Russia'
console.log(zalary)
zalary.age = 123
console.log(zalary)
delete zalary.country
console.log(zalary)
zalary.user = {
  name:'egor',
  fam: 'Ezhov'
}
delete zalary.city
console.log(zalary)
console.log('свойство -', zalary.user.fam)

//////////////////////////////////////////////

