import logging

import nailgun.entities
import pytest

from robottelo.constants import DEFAULT_LOC
from robottelo.constants import DEFAULT_ORG


LOGGER = logging.getLogger('robottelo')


@pytest.fixture(scope='module')
def module_org():
    """Shares the same organization for all tests in specific test module.
    Returns 'Default Organization' by default, override this fixture on

    :rtype: :class:`nailgun.entities.Organization`
    """
    default_org_id = (
        nailgun.entities.Organization().search(query={'search': f'name="{DEFAULT_ORG}"'})[0].id
    )
    return nailgun.entities.Organization(id=default_org_id).read()


@pytest.fixture(scope='module')
def module_loc():
    """Shares the same location for all tests in specific test module.
    Returns 'Default Location' by default, override this fixture on

    :rtype: :class:`nailgun.entities.Organization`
    """
    default_loc_id = (
        nailgun.entities.Location().search(query={'search': f'name="{DEFAULT_LOC}"'})[0].id
    )
    return nailgun.entities.Location(id=default_loc_id).read()
