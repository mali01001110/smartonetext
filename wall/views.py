from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Message


def index(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        message_text = request.POST.get("message", "").strip()

        if username and message_text:
            Message.objects.create(username=username, message=message_text)
            return redirect("feed")

    return render(request, "index.html", {"site_name": "SmartOneText"})


def feed(request):
    messages = Message.objects.order_by("-created_at")
    return render(
        request,
        "feed.html",
        {"site_name": "SmartOneText", "messages": messages},
    )


@require_POST
@login_required(login_url="/admin/login/")
@user_passes_test(lambda u: u.is_staff, login_url="/admin/login/")
def delete_message(request, message_id):
    msg = get_object_or_404(Message, id=message_id)
    msg.delete()
    return redirect("feed")