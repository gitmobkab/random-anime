import pytest
from random_anime import data_unwrapper

dict_1 = {
    "user": {
        "name": "Alice",
        "location": "Wonderland"
    }
}

dict_2 = {
    "company": {
        "department": {
            "team": {
                "lead": "Mob",
                "members": 5
            }
        }
    }
}

dict_3 = {
    "root": {
        "branch_a": {
            "leaf": {
                "color": "green"
            }
        },
        "branch_b": {
            "leaf": {
                "color": "yellow"
            }
        }
    }
}


@pytest.mark.parametrize("input_dict, attributes, expected_output",[
    (dict_1,["user","location"],"Wonderland"),
    (dict_2,["company","department","team","members"],5),
    (dict_3,["root","branch_b","leaf","color"],"yellow")
])
def test_data_unwrapper(input_dict, attributes, expected_output):
    assert data_unwrapper(input_dict, attributes) == expected_output