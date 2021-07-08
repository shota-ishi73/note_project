from django.shortcuts import render,redirect, get_object_or_404
from .forms import NoteCreateForm
from .models import Note


def index(request):
  context={
    'note_list':Note.objects.all(),
  }
  return render(request,'note_app/note_list.html',context)

def add(request):
  # 送信内容を基にフォームを作成し、POST出なければ空のフォーム
  form = NoteCreateForm(request.POST or None)

  # method = POST、送信ボタン押下時、入力内容に問題なければ
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('note_app:index')

  # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示 
  context = {
    'form':form
  }
  return render(request,'note_app/note_form.html',context)

def update(request,pk):
  note = get_object_or_404(Note,pk=pk)

  form = NoteCreateForm(request.POST or None,instance=note)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('note_app:index')

  context={
    'form':form
  }
  return render(request,'note_app/note_form.html',context)

def delete(request,pk):
  note = get_object_or_404(Note,pk=pk)

  if request.method == 'POST':
    note.delete()
    return redirect('note_app:index')

  context={
    'note':note
  }
  return render(request,'note_app/note_confirm_delete.html',context)

def detail(request,pk):
  note = get_object_or_404(Note,pk=pk)

  context={
    'note':note
  }
  return render(request,'note_app/note_detail.html',context)