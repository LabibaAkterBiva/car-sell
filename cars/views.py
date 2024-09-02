from django.shortcuts import render,redirect
from .import forms,models
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView,DetailView
from django.utils.decorators import method_decorator
from .models import Car
from orders.models import Order

class DetailsCar(DetailView):
    model=models.Car
    template_name='car_detail.html'
    pk_url_kwarg='id'
    
    def post(self,request,*args,**kwargs):
        comment_form=forms.CommentForm(self.request.POST)
        car=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.car=car
            new_comment.save()

        return  self.get(request,*args,**kwargs)  
                # comment_form.instance.author=self.request.user
                # comment_form.instance.post=post
                
        
        
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        car=self.object #post model er object akhana store hoilo
        comments=car.comments.all()         #redirect korte chai comment_form er form ta validate kore comment save hobe na
        comment_form=forms.CommentForm()         
        context['comments']=comments
        context['comment_form']=comment_form
        return context
                
@login_required
def buy_car(request,id):
    car=models.Car.objects.get(pk=id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        Order.objects.create(user=request.user, car=car)
        return redirect('profile')
    else:
        return render(request,'car_detail.html', {'id': id})
    
    
