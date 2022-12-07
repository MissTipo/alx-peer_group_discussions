#!/usr/bin/node
class Person {
	constructor(name) {
		this.name = name;
	}
	introduceSelf() {
		console.log(`hello Iam ${this.name}`);
	}
}

const Erick = new Person('erick');
Erick.introduceSelf();
