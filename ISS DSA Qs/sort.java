import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Person {
    private String name;
    private int age;
    Person(String name, int age){
        this.name = name;
        this.age = age;
    }
    public String getName(){
        return this.name;
    }
    public int getAge(){
        return this.age;
    }
}
class sorting implements Comparator<Person>{
    public int compare(Person p1, Person p2) {
        int nameComparison = p1.getName().compareTo(p2.getName());
        if (nameComparison != 0) {
            return nameComparison;
        }
        return Integer.compare(p1.getAge(), p2.getAge());
    }
}
public class sort{
    public static void main(String[] args) {
        ArrayList <Person> persons = new ArrayList<>();
        persons.add(new Person("Alice", 25));
        persons.add(new Person("Bob", 30));
        persons.add(new Person("Alice", 20));
        persons.add(new Person("Bob", 35));

        Collections.sort(persons, new sorting());

        for (Person person : persons) {
            System.out.println(person.getName() + ", " + person.getAge());
        }
    }
}


// I was then asked how to sort elements in an array/ArrayList using a second parameter in case 
// of a tie in the first parameter. For eg, sorting the names from A-Z and in case of a tie, 
// sorting them on the basis of age.