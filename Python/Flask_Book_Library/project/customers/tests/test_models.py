import pytest
from project.customers.models import Customer


def test_validate_customer_name():
    with pytest.raises(ValueError):
        Customer.validate_name(Customer, "name", "Invalid Name!")

    with pytest.raises(ValueError):
        Customer.validate_name(Customer, "name", "a" * 65)

    assert Customer.validate_name(Customer, "name", "ValidName") == "ValidName"


def test_validate_customer_city():
    with pytest.raises(ValueError):
        Customer.validate_city(Customer, "city", "Invalid City!")

    assert Customer.validate_city(Customer, "city", "ValidCity") == "ValidCity"
