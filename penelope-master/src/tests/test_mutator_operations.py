import sys
import datetime

import pytest

from ..person import Person
from ..mutator import Mutator

@pytest.yield_fixture()
def resource():
    """ A trivial person object to act upon in testing """
    print("setup")
    person = Person(
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12),
        "No. 12 Short Street, Greenville",
        "555 456 0987",
        "jane.doe@example.com",
    )
    yield person
    print("teardown")


class TestMutatorOperations:
    """ Check the longer Mutator """
    # it should be able to instantiate Mutator and a target class
    def test_mutator_can_instantiate(self, resource):
        mutator = Mutator(resource)
        assert type(mutator) is Mutator
        assert callable(getattr(mutator, "get_prop"))

    # it should have a class that it can instantiate
    def test_target_exists_to_operate_on(self, resource):
        assert resource is not None
        assert isinstance(resource, Person)
        assert resource.name is "Jane"

    # it should be able to set an arbitrary non-clashing property
    def test_mutator_can_create_prop(self, resource):
        simple_dummy_string = "dummy string"
        mutator = Mutator(resource)
        result = mutator.set_prop("best_new_prop", simple_dummy_string)
        assert result is simple_dummy_string

    # it should be able to set then get a custom property
    def test_mutator_can_get_prop(self, resource):
        random_chars = "random chars for testing"
        mutator = Mutator(resource)
        mutator.set_prop("mutant", random_chars)
        assert mutator.get_prop("mutant") == random_chars

    # it should be able to override an existing property
    def test_it_can_override_existing_prop(self, resource):
        random_chars = "Roy Ronalds"
        mutator = Mutator(resource)
        mutator.set_prop("name", random_chars)
        assert mutator.get_prop("name") == random_chars

    # it should error when trying to override an existing property of an incompatible type
    @pytest.mark.xfail
    def test_it_should_error_on_incompatible_types(self, resource):
        with pytest.raises(Exception):
            mutator = Mutator(resource)
            mutator.set_prop("name", 5)

    # When the list operation is called, it should print out starting and set properties
    def test_partial_list_outputs(self, resource):
        mutator = Mutator(resource)
        assert mutator.render() is not None
        assert type(mutator.render()) is str
        assert mutator.render() is not ""
        assert "name" in mutator.render()
        assert "Jane" in mutator.render()

    def test_more_full_list_output_of_mutator(self, resource):
        mutator = Mutator(resource)
        more_matches = ["birthdate", "telephone", "email"]
        assert mutator.render() is not ""
        assert "birthdate" in str(mutator)
        assert all([x in str(mutator) for x in more_matches])

    def test_extract_the_object_can_run_methods(self, resource):
        mutator = Mutator(resource)
        final = mutator.write()
        assert final.age() == 26

    @pytest.mark.xfail
    def test_mutator_cannot_override_existing_methods(self, resource):
        with pytest.raises(Exception):
            mutator = Mutator(resource)
            mutator.set_prop("age", 999)

    def test_string_commands_set(self, resource):
        resource.name = "JamesZ"
        mutator = Mutator(resource)
        mutator.command("SET name=William")
        mutator.command("SET new_prop=Zigzag")
        mutator.command("SET AAAAA=Zigzag")
        assert mutator.command("GET name") == "William"
        final = mutator.write()
        assert final.name == "William"
        assert final.new_prop == "Zigzag"
        assert final.AAAAA == "Zigzag"
        assert 'new_prop' in final._members()
        assert 'AAAAA' in final._members()
        assert final.age() == 26

    def test_list_command(self, resource):
        mutator = Mutator(resource)
        more_matches = ["birthdate", "telephone", "email"]
        result = mutator.command("GET *")
        assert result is not ""
        assert "birthdate" in result
        assert all([x in result for x in more_matches])

    # When I reach this point, refactor

