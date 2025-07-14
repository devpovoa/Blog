from django.contrib import admin
from django.utils.html import format_html
from blog.models import Post, Comment, Category, About


@admin.action(description="Ativar comentários selecionados")
def ativar(modeladmin, request, queryset):
    queryset.update(active_at=True)


@admin.action(description="Desativar comentários selecionados")
def desativar(modeladmin, request, queryset):
    queryset.update(active_at=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    list_filter = ('author', 'published_at', 'category')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email', 'post', 'active_at', 'created_at')
    list_editable = ('active_at',)
    list_filter = ('active_at', 'created_at')
    search_fields = ('user__username', 'user__email', 'content')
    actions = [ativar, desativar]

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'Usuário'

    def get_email(self, obj):
        return obj.user.email

    get_email.short_description = 'Email'


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'exibir_foto')

    fieldsets = (
        (None, {
            'fields': ('nome', 'cargo', 'email', 'foto')
        }),
        ('Biografia', {
            'fields': ('biografia',),
        }),
        ('Redes sociais', {
            'fields': ('linkedin', 'github', 'portfolio'),
        }),
    )

    def exibir_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="height: 50px; border-radius: 50%;" />', obj.foto.url)
        return "-"

    exibir_foto.short_description = "Foto"

    def has_add_permission(self, request):
        return not About.objects.exists()
