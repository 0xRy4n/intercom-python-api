from intercom_python_api.paths.articles_id.get import ApiForget
from intercom_python_api.paths.articles_id.put import ApiForput
from intercom_python_api.paths.articles_id.delete import ApiFordelete


class ArticlesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
