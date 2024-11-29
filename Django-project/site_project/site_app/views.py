from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from site_app.forms import CategoryForm, ContactForm
from site_app.models import Product, Category, Contact


class IndexView(TemplateView):
    template_name = "site_app/index.html"


class CategoryView(ListView):
    # model = Category
    template_name = "site_app/categories.html"
    context_object_name = "categories"
    queryset = (
        Category.objects
        .prefetch_related('products')
        .all()
    )


class CategoryDetailView(DetailView):
    model = Category
    template_name = "site_app/categories_detail.html"
    context_object_name = 'category_detail'


class CategoryAddView(CreateView):
    model = Category
    template_name = "site_app/categories_add.html"
    form_class = CategoryForm


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "site_app/categories_confirm_delete.html"
    success_url = reverse_lazy("site_app:ListCategory")
    context_object_name = "category_delete"


class CategoryEditView(UpdateView):
    model = Category
    template_name = "site_app/categories_edit.html"
    form_class = CategoryForm
    context_object_name = "category_edit"


class ArticleList(ListView):
    # model = Product
    template_name = "site_app/article.html"
    context_object_name = "articles"
    queryset = (
        Product.objects
        .select_related('author')
        .prefetch_related('category')
        .all
    )


class ArticleDetailView(DetailView):
    model = Product
    template_name = "site_app/article_detail.html"
    context_object_name = "article_detail"


class ContactFormAdd(CreateView):
    model = Contact
    template_name = "site_app/contact_form.html"
    form_class = ContactForm

