import os
from typing import Dict


class PeopleRegisterView:
    def register_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Cadastrar nova Pessoa \n\n')
        name = input('Determine o nome da pessoa: ')
        age = input('Determine a idade da pessoa: ')
        height = input('Determine a altura da pessoa: ')
        
        new_person_informations = {
            "name": name,
            "age": age,
            "height": height
        }

        return new_person_informations