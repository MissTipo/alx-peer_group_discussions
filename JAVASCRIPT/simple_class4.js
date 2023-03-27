/* eslint-disable no-useless-constructor */
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a noise.`);
  }
}

class Dog extends Animal {
  constructor(name) {
    super(name);
  }

  speak() {
    console.log(`${this.name} barks.`);
  }
}

class Cat extends Animal {
  constructor(name) {
    super(name);
  }

  speak() {
    console.log(`${this.name} meows.`);
  }
}

class Goat extends Animal {
  constructor(name) {
    super(name);
  }

  speak() {
    console.log(`${this.name} bleats.`);
  }
}

const dog = new Dog('Rex');
const cat = new Cat('Fluffy');
const goat = new Goat('Billy');

dog.speak(); // "Rex barks."
cat.speak(); // "Fluffy meows."
goat.speak(); // "Billy bleats."
