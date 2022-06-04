from django.http import HttpResponse


def home_view(request):
    html = """<html>
        <body>  
                <h1>Welcome...</h1>
                <h2> In settings.py edit WP_URL to your website url to fetch blogs. </h1>
                <a href = "blog">blogs
        </body>
    </html>"""
    return HttpResponse(html)