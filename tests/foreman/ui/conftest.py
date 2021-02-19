import logging

import pytest
from airgun.session import Session


LOGGER = logging.getLogger('robottelo')


@pytest.fixture()
def autosession(module_user, request):
    """Session fixture which automatically initializes and starts airgun UI
    session and correctly passes current test name to it. Use it when you want
    to have a session started before test steps and closed after all of them,
    i.e. when you don't need manual control over when the session is started or
    closed.

    Usage::

        def test_foo(autosession):
            # your ui test steps here
            autosession.architecture.create({'name': 'bar'})

    """
    login = module_user.login
    password = module_user.password
    with Session(request.node.nodeid, login, password) as started_session:
        yield started_session
