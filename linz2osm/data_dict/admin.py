from django.contrib import admin

from linz2osm.data_dict.models import Layer, Tag

class TagInline(admin.StackedInline):
    model = Tag
    extra = 3
    verbose_name = 'Tag'
    verbose_name_plural = 'Tags'

class LayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'entity', 'get_geometry_type_display', 'stats_link', 'tag_count', 'dataset_descriptions', 'notes',)
    list_filter = ('entity',)
    inlines = [
        TagInline,
    ]
    ordering = ('name',)
    readonly_fields = ('name', 'entity',)
    search_fields = ('name', 'notes',)

    class Media:
        css = {
            'all': ('code_exec.css',),
        }
        js = ("jquery.cookie.js", "code_exec.js",)
            
    def tag_count(self, obj):
        return obj.tags.count()
    tag_count.short_description = 'Defined Tags'
    
    def dataset_descriptions(self, obj):
        return ", ".join([d.description for d in obj.datasets.all()])
    dataset_descriptions.short_description = 'Available in' 

    def stats_link(self, obj):
        return "<a href='%s/stats/'>Layer Stats</a>" % obj.name
    stats_link.short_description = 'Statistics'
    stats_link.allow_tags = True

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    ordering = ('tag',)
    exclude = ('layer',)
    
    class Media:
        css = {
            'all': ('code_exec.css',),
        }
        js = ("jquery.cookie.js", "code_exec.js",)
            
    def queryset(self, request):
        # only tags without layers (default tags)
        return self.model.objects.default()

admin.site.register(Layer, LayerAdmin)
admin.site.register(Tag, TagAdmin)

