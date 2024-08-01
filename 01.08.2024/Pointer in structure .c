#include <stdio.h>
#include <string.h>

struct Person {
    char name[50];
    int age;
};

void printPerson(struct Person *p) {
    printf("Name: %s\n", p->name);
    printf("Age: %d\n", p->age);
}

int main() {
    struct Person person1;

    printf("Enter name: ");
    fgets(person1.name, sizeof(person1.name), stdin);
    person1.name[strcspn(person1.name, "\n")] = 0;
    printf("Enter age: ");
    scanf("%d", &person1.age);

    struct Person *pPerson = &person1;

    printPerson(pPerson);

    return 0;
}
