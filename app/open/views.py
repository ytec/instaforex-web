from .models import OpenAccountReal, OpenAccountDemo, OpenAccountAnonymous


def openAccountReal(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            pass

def openAccountDemo():
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Open = form.save(commit=False)
    pass

def openAccountAnonymous():
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Open = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
