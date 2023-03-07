from rest_framework import pagination


class DefaultPagination(pagination.LimitOffsetPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5
