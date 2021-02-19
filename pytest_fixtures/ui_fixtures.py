import pytest
from airgun.session import Session


@pytest.fixture()
def session(request, module_user):
    """Session fixture which automatically initializes (but does not start!)
    airgun UI session and correctly passes current test name to it. Uses shared
    module user credentials to log in.


    Usage::

        def test_foo(session):
            with session:
                # your ui test steps here
                session.architecture.create({'name': 'bar'})

    """
    return Session(request.node.nodeid, module_user.login, module_user.password)
