#include <iostream>
#include <vector>
#include <string>
#include "profile.hpp"

Profile::Profile(std::string new_name, std::string new_city, std::string new_country, int new_age,std::string new_pronouns){
    name = new_name;
    city = new_city;
    country = new_country;
    pronouns = new_pronouns;
    age = new_age;
}
std::string Profile::view_profile(){
    std::string bio = "Name: " + name;
    bio += "\nAge: " +  std::to_string(age);
    bio += "\nCountry: " + country;
    bio += "\nCity: " + city;
    for (int i = 0; i < hobbies.size(); i++){
        bio += "\nHobbies: " + hobbies[i] + "\n";
    }
    
    return bio;

}
void Profile::add_hobbies(std::string new_hobby){
    hobbies.push_back(new_hobby);

}
