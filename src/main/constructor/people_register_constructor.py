from src.views.people_register_view import PeopleRegisterView


def people_register_constructor():
    people_register_view = PeopleRegisterView()

    new_person_informations = people_register_view.register_person_view()