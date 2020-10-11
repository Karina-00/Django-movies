from django.contrib import admin
from .models import Film, AdditionalInfo, Review, Actor

# admin.site.register(Film)
# lub


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["title"]  # what to show to admin
    # exclude = ["poster"]  # all beyond
    list_display = ["title", "year", "imdb_rating"]  # enables sorting
    list_filter = ["year", "imdb_rating"]
    search_fields = ["title", "description"]


admin.site.register(AdditionalInfo)
admin.site.register(Review)
admin.site.register(Actor)
