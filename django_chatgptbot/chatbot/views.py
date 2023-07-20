import os
import openai
import json
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # print(response)
    answer = response.choices[0].message.content.strip()
    # print(answer)
    return answer


def ask_dalle(prompt):
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    image_url = response["data"][0]["url"]
    return image_url


def index(request):
    return redirect("chatbot")


def image(request):
    if request.method == "POST":
        body = json.loads(request.body)
        image_url = ask_dalle(body["prompt"])
        return JsonResponse({"image_url": image_url, "prompt": body["prompt"]})

    return render(request, "image.html")


def chatbot(request):
    chats = Chat.objects.filter(user=request.user).order_by("created_at")

    if request.method == "POST":
        body = json.loads(request.body)
        response = ask_openai(body["message"])
        chat = Chat(
            user=request.user,
            message=body["message"],
            response=response,
            created_at=timezone.now(),
        )
        chat.save()
        return JsonResponse({"response": response, "message": body["message"]})

    return render(request, "chatbot.html", {"chats": chats})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("chatbot")
            else:
                return render(
                    request,
                    "login.html",
                    {"error_message": "Invalid username or password"},
                )
        except:
            return render(
                request,
                "login.html",
                {"error_message": "Invalid username or password"},
            )

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(
                request, "register.html", {"error_message": "Passwords do not match"}
            )
        else:
            try:
                user = User.objects.create_user(
                    username=username, email=email, password=password1
                )
                user.save()
                auth.login(request, user)
                return redirect("chatbot")
            except:
                return render(
                    request,
                    "register.html",
                    {"error_message": "Error creating account"},
                )

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect("login")
