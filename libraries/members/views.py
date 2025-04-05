from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Member, Loan, Book, BookCopy, LibraryBranch
from .forms import MemberLoginForm
from django.db.models import Count

def members(request):
    libraryMembers = Member.objects.all()
    template = loader.get_template('my_members.html')
    context = {
        'librarymembers': libraryMembers,
    }
    return HttpResponse(template.render(context,request))

def member_entry(request):
    form = MemberLoginForm(request.POST)
    member = None
    loans = None
    if request.method == "POST":
        if form.is_valid():
            member_id = form.cleaned_data["mid"]
            member = Member.objects.get(mid = member_id)
            if member:
                loans = Loan.objects.filter(mid = member_id).select_related('copyid','copyid__bid','copyid__lid')
            else:
                member = get_object_or_404(Member, mid = member_id)

    return render(request, "my_members.html", {"form": form, "member":member, "loans":loans})

def book_availability(request,book_id):
    book = Book.objects.get(pk = book_id)
    copies = BookCopy.objects.filter(bid = book_id).select_related('lid')
    available = BookCopy.objects.filter(bid = book_id).select_related('lid').values('lid','lid__lname').annotate(copy_count = Count('copyid'))
    return render(request, 'book_availability.html',{'book':book, 'copies' : copies,'available':available})