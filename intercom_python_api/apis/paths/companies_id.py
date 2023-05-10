from intercom_python_api.paths.companies_id.get import ApiForget
from intercom_python_api.paths.companies_id.put import ApiForput
from intercom_python_api.paths.companies_id.delete import ApiFordelete


class CompaniesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
