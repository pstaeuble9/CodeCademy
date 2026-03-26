#include <iostream>
#include <vector>
#include <string>

class Profile{
    private:
    std::string name, city, country, pronouns;
    int age;
    std::vector <std::string> hobbies;

    public:
    Profile(std::string new_name, std::string new_city, std::string new_country, int new_age, std::string new_pronouns = "they/them");
    std::string view_profile();
    void add_hobbies(std::string new_hobbies);

};
