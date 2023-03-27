class Person {
  #firstName;
  #lastName;
  #age;
  static #count = 0;

  constructor(firstName, lastName, age) {
    this.#firstName = firstName;
    this.#lastName = lastName;
    this.#age = age;
    Person.#count++;
  }

  get firstName() {
    return this.#firstName;
  }

  get lastName() {
    return this.#lastName;
  }

  get age() {
    return this.#age;
  }

  set firstName(firstName) {
    this.#firstName = firstName;
  }

  set lastName(lastName) {
    this.#lastName = lastName;
  }

  set age(age) {
    this.#age = age;
  }

  get fullName() {
    return `${this.#firstName} ${this.#lastName}`;
  }

  static get count() {
    return Person.#count;
  }

  mySelf() {
    console.log(`My name is ${this.fullName}., I am ${this.#age} years old.`);
  }
}

const person1 = new Person("John", "Doe", 30);
const person2 = new Person("Jane", "Doe", 25);

person1.mySelf();
person2.mySelf();

console.log(Person.count);

person1.firstName = "Johnathan";
person1.lastName = "Doe";
person1.age = 31;

person1.mySelf();

console.log(Person.count);
