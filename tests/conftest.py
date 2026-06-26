import copy

import pytest

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activities():
    original_state = copy.deepcopy(app_module.INITIAL_ACTIVITIES)
    app_module.activities.clear()
    app_module.activities.update(original_state)
    yield
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(app_module.INITIAL_ACTIVITIES))
