from django.contrib import admin
from .models import Book,Borrower,Reviewer
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['book_id','book_title','number_of_copies','borrowed_on']
    list_filter=('book_title','number_of_copies')
    search_fields=('book_title',)
class BorrowerAdmin(admin.ModelAdmin):
    list_display=['borrower_id','borrower_name','book','borrower_emailid']
    #raw_id_fields=('book',)

class ReviewerAdmin(admin.ModelAdmin):
    list_display=['reviewer_id','reviewer_name','reviewer_emailid','reviewer_comments']

admin.site.register(Book, BookAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Reviewer, ReviewerAdmin)
