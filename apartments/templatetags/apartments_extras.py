from django import template

register = template.Library()


@register.simple_tag
def paginate_url(page_num, page_field_name, urlencode=None):
    url = f"?{page_field_name}={page_num}"

    if urlencode:
        query_string = urlencode.split('&')
        filtered_query_string = filter(lambda item: item.split('=')[0]!=page_field_name, query_string)
        encoded_query_string = '&'.join(filtered_query_string)

        url = f"{url}&{encoded_query_string}"

    return url