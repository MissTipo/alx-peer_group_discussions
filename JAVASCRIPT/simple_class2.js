import Person from './simple_class';

class Employee extends Person {
  constructor(name, age, job) {
    super(name, age);
    this.job = job;
  }

  introduce() {
    console.log(
      `Hi, my name is ${this.name} and I am ${this.age} years old. I am a ${this.job}`,
    );
  }
}

const employee1 = new Employee('John', 30, 'Manager');
const employee2 = new Employee('Jane', 25, 'Developer');

employee1.introduce();
employee2.introduce();
