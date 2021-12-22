from rest_framework.pagination import PageNumberPagination


class GlobalPageNumberPagination(PageNumberPagination):
    """
    自定义分页
    """
    def __init__(self):
        super(GlobalPageNumberPagination, self).__init__()
        self.page_size_query_param = 'page_size'
        self.max_page_size = 20
