using System;

namespace gameProject
{   // Create a base Human class with five attributes: name, strength, intelligence, dexterity, and health.
    public class human
    {
        public string charName;
        public int health;
        public int dexterity;
        public int strength;

        public int intelligence;

        // Give a default value of 3 for strength, intelligence, and dexterity. Health should have a default of 100.
        //  When an object is constructed from this class it should have the ability to pass a name

        public human(string name) {
            this.health = 100;
            this.dexterity = 3;
            this.strength = 3;
            this.intelligence = 3;
            this.charName = name;

        }
        //  Let's create an additional constructor that accepts 5 parameters, so we can set custom values for every field.
        public human(string name, int health, int dexterity, int strength, int intelligence) {
            this.charName = name;
            this.health = health;
            this.dexterity = dexterity;
            this.strength = strength;
            this.intelligence = intelligence;
        }
        //  Now add a new method called attack, which when invoked, should attack another Human object that is passed as a parameter. The damage done should be 5 * strength (5 points of damage to the attacked, for each 1 point of strength of the attacker).
        public void Attack(human opponent) {
            opponent.health -= (this.strength * 5);
        }

        public void opponent(object opponent) {
            if (opponent is human) {
                this.Attack(opponent as human);
            }
        }
    }
}
