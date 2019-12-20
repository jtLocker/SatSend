from django.shortcuts import render
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
from django.http import HttpResponse

# def make_friend(request):
#     other_user = User.objects.get(pk=1)
#     Friend.objects.add_friend(
#         request.user,                               # The sender
#         other_user,                                 # The recipient
#         message='Hi! I would like to add you')      # This message is optional

def friend_req(request):
    all_users = User.objects.all().values_list('username', flat=True) 
    context = {}
    context['all_users'] = all_users
    return render(request, 'addFriend.html', context)
    # if request.method == "POST":
    #     return(request, 'addFriend.html')
    # else:
    #     return(request, 'addFriend.html')
    #     other_user = User.objects.get()
    #     if request.POST['password'] == request.POST['confirm_password']:
    #         try:
    #             user = User.objects.get(username = request.POST["username"])
    #             return render(request, 'signup.html', {"error" : "this username is taken"})
    #         except User.DoesNotExist:
    #             user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
    #             auth.login(request, user)
    #             return redirect('home')
    #     else:
    #         return render(request, 'signup.html', {"error" : "passwords do not match"})
    # else:
    #     return render(request, 'signup.html', )
