#include <iostream>
#include <vector>
#include <string>
#include "profile.hpp"

int main(){
    Profile sam("Sam Darkkila", "New York", "USA", 30, "he/him");
    sam.add_hobbies("listening to audio books");
    sam.add_hobbies("playing rec sports like bowling and kickball");
    sam.add_hobbies("writing a speculative fiction novel");
    sam.add_hobbies("rading advice columnns");
    std::cout << sam.view_profile();

    return 0;
}
