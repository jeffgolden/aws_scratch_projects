# Reference:
# https://jeffgolden.me/posts/default-document-for-cloudfront-folders-with-s3-origin/index.html
# for more details
def lambda_handler(event, context):
    
    request = event['Records'][0]['cf']['request']
    old_uri = request['uri']
    new_uri = old_uri
    is_file = len(old_uri.split('.'))>1
    if not is_file:
        new_uri = f"{old_uri}{'' if old_uri[-1] == '/' else '/'}index.html"
    
    request['uri']=new_uri
    return request

