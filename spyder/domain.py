from urllib.parse import urlparse

"""
     Cralwer Helper Functions
     - Based on the universial web crawler by Bucky Roberts <https://thenewboston.com/>
 """

# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
