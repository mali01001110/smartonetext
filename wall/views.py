from django.shortcuts import render, redirect
from .models import Message


def index(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        message = request.POST.get("message", "").strip()

        if username and message:
            Message.objects.create(username=username, message=message)
            return redirect("feed")

    return render(request, "index.html", {"site_name": "SmartOneText"})


def feed(request):
    messages = Message.objects.order_by("-created_at")
    return render(
        request,
        "feed.html",
        {"site_name": "SmartOneText", "messages": messages},
    )