from django.shortcuts import render, HttpResponse

topics = [
    {"id": 1, "title": "routing", "body": "routing is.."},
    {"id": 2, "title": "view", "body": "view is.."},
    {"id": 3, "title": "model", "body": "model is.."},
]


def index(request):
    global topics
    ol_content = "".join(
        [
            f"<li><a href='/read/{topic['id']}'>{topic['title']}</a></li>"
            for topic in topics
        ]
    )

    return HttpResponse(
        f"""
    <html>
        <body>
            <h1>Django</h1>
            <ol>
            {ol_content}
            </ol>
            <h2>Welcome</h2>
            <p>hello, django</p>
        </body>
    </html>
    """
    )


def create(request):
    return HttpResponse("create page")


def read(request):
    return HttpResponse("read page")
