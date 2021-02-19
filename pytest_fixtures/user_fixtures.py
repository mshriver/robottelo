import logging

import pytest
from fauxfactory import gen_string
from nailgun import entities


LOGGER = logging.getLogger('robottelo')


@pytest.fixture(scope='module')
def default_viewer_role(module_org, default_location):
    """Custom user with viewer role for tests validating visibility of entities or fields created
    by some other user. Created only when accessed, unlike `module_user`.
    """
    viewer_role = entities.Role().search(query={'search': 'name="Viewer"'})[0]
    custom_password = gen_string('alphanumeric')
    custom_user = entities.User(
        admin=False,
        default_organization=module_org,
        location=[default_location],
        organization=[module_org],
        role=[viewer_role],
        password=custom_password,
    ).create()
    custom_user.password = custom_password
    return custom_user


@pytest.fixture(scope='module')
def module_user(request, module_org, module_loc):
    """Creates admin user with default org set to module org and shares that
    user for all tests in the same test module. User's login contains test
    module name as a prefix.

    :rtype: :class:`nailgun.entities.User`
    """
    # take only "module" from "tests.ui.test_module"
    test_module_name = request.module.__name__.split('.')[-1].split('_', 1)[-1]
    login = f'{test_module_name}_{gen_string("alphanumeric")}'
    password = gen_string('alphanumeric')
    LOGGER.debug('Creating session user %r', login)
    user = entities.User(
        admin=True,
        default_organization=module_org,
        default_location=module_loc,
        description=f'created by nailgun for module "{test_module_name}"',
        login=login,
        password=password,
    ).create()
    user.password = password
    yield user
    try:
        LOGGER.debug('Deleting session user %r', user.login)
        user.delete(synchronous=False)
    except Exception:
        LOGGER.exception('Unable to delete module scoped user')
