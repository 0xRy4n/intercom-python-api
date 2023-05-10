from intercom_python_api.paths.contacts_id.get import ApiForget
from intercom_python_api.paths.contacts_id.put import ApiForput
from intercom_python_api.paths.contacts_id.delete import ApiFordelete


class ContactsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
