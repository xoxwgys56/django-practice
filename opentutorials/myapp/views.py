from __future__ import annotations
from typing import TYPE_CHECKING
from django.shortcuts import redirect, render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

if TYPE_CHECKING:
    from django.http.request import HttpRequest

topics = [
    {"id": 1, "title": "routing", "body": "routing is.."},
    {"id": 2, "title": "view", "body": "view is.."},
    {"id": 3, "title": "model", "body": "model is.."},
]

next_id = len(topics) + 1


def get_html_template(article_tag: str, topic_id: str = None):
    global topics
    ol_content = "".join(
        [
            f"<li><a href='/read/{topic['id']}'>{topic['title']}</a></li>"
            for topic in topics
        ]
    )

    return f"""
    <html>
        <body>
            <h1>Django</h1>
            <ol>
            {ol_content}
            </ol>
            <p>{article_tag}</p>
            <ul>
                <li>
                    <form action='/delete/' method='post' >
                        <input type='hidden' name='id' value='{topic_id}' />
                        <input type='submit' value='delete' />
                    </form>
                </li>
            </ul>
        </body>
    </html>
    """


def index(request):
    article = f"""
        <h2>Welcome</h2>
        <p>hello, django</p>
    """
    return HttpResponse(get_html_template(article))


@csrf_exempt
def create(request: HttpRequest):
    global next_id

    if request.method == "GET":
        article = f"""
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title" /></p>
            <p><textarea name="body" placeholder="body" ></textarea></p>
            <p><input type="submit" /></p>
        </form>
        """
        return HttpResponse(get_html_template(article))
    elif request.method == "POST":
        topics.append(
            {
                "id": next_id,
                "title": request.POST["title"],
                "body": request.POST["body"],
            }
        )
        my_id = next_id
        next_id = next_id + 1

        return redirect(f"/read/{my_id}")


def read(request: HttpRequest, id: str):
    global topics
    article = f"""
        <h2>Not Found</h2>
        <p>sorry can not found item id {id}</p>
    """
    for topic in topics:
        if topic["id"] == int(id):
            article = f"""
                <h2>{topic['title']}</h2>
                <p>{topic['body']}</p>
            """

    return HttpResponse(get_html_template(article, id))


@csrf_exempt
def delete(request: HttpRequest):
    global topics

    if request.method == "POST":
        id = int(request.POST["id"])
        if not (id in [topic["id"] for topic in topics]):
            return HttpResponse(f"can not found item include id {id}")
        else:
            topics = [topic for topic in topics if topic["id"] != id]
            return redirect("/")
