export default class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHello() {
    console.log(
      `Hello, my name is ${this.name} and I am ${this.age} years old`,
    );
  }
}

/* const person1 = new Person('John', 30);
const person2 = new Person('Jane', 25);

person1.sayHello();
person2.sayHello(); */

// export default Person;
