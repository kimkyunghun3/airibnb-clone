from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "country", "address", "price")},
         ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        ("More about the space", {
            "classes": ("collapse",),
         "fields": ("amenities", "facilities", "house_rules"),
         },
         ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities"

    )

    ordering = ("name", "price", "bedrooms")

    list_filter = ("instant_book", "host__superhost", "room_type",
                   "amenities", "facilities", "house_rules", "city", "country")

    search_fields = ("^city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj):  # class 안의 함수에서 self은 class을 의미하고 obj은 admin에서 row을 의미
        print(obj.amenities.all())
        return "potato"
    count_amenities.short_description = "hello sexy!"  # functionailty다. 장고에서 함수로 받아들인다


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ """

    pass
