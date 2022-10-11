from django.core import validators
from django.core.validators import (MinValueValidator, MaxValueValidator,
                                    RegexValidator)
from django.db import models
from users.models import User

# ORANGE = "#E26C2D"
# GREEN = "#49B64E"
# PURPLE = "#8775D2"

# CHOICES = ((ORANGE, "оранжевый"), (GREEN, "зелёный"), (PURPLE, "фиолетовый"))


# class Tag(models.Model):
#     """Модель тега"""
#     name = models.CharField("Тэг", max_length=200, unique=True, blank=False)
#     color = models.CharField(
#         "Цвет тэга", max_length=7, choices=CHOICES, unique=True, blank=False
#     )
#     slug = models.SlugField(
#         "Slug тэга", max_length=200, unique=True, blank=False
#     )

#     class Meta:
#         verbose_name = "Тэг"
#         verbose_name_plural = "Тэги"

#     def __str__(self):
#         return self.name

class Tag(models.Model):
    """Модель тега"""
    name = models.CharField(
                            'Название Тега',
                            unique=True,
                            max_length=50,
                            blank=False)
    color = models.CharField(
        'Цветовой HEX-код',
        unique=True,
        max_length=7,
        validators=[
            RegexValidator(
                regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
                message='Введенное значение не относится к формату HEX!'
            )
        ]
    )
    slug = models.SlugField(
                            'Уникальный слаг',
                            unique=True,
                            max_length=50)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель ингридиента"""
    name = models.CharField('Название', max_length=200, blank=False)
    measurement_unit = models.CharField(
        'Единица измерения', max_length=200, blank=False
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}, {self.measurement_unit}"


class Recipe(models.Model):
    """Модель рецепта"""
    name = models.CharField('Название рецепта', max_length=200, blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Автор',
    )
    text = models.TextField('Описание приготовления', blank=False, null=True)
    image = models.ImageField(
        'Изображение готового блюда', upload_to='recipes/', blank=False
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientInRecipe',
        related_name='recipes',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag, related_name='recipe', verbose_name='Теги'
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления в минутах',
        blank=False,
        validators=(
            MinValueValidator(1, message='Минимальное значение 1 мин.!'),
            MaxValueValidator(600, message='Максимальное значение 10000 мин.!')
        ),
    )
    pub_date = models.DateTimeField(
        'Дата публикации рецепта', auto_now_add=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class AmountIngredient(models.Model):
    """Модель количества ингридиентов в отдельных рецептах"""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient',
        verbose_name='Ингредиент',
    )
    amount = models.PositiveSmallIntegerField(
        'Количество',
        blank=False,
        validators=[
            MinValueValidator(1, message='Минимальное количество 1!'),
            MaxValueValidator(10000, message='Максимальное значение 10000!')
        ]
    )

    class Meta:
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_ingredient',
            )
        ]


class FavoriteRecipe(models.Model):
    """Модель избранного"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_user',
        verbose_name='Пользователь',
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite_recipe',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_favorite_recipe',
            )
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Избранное'


class ShoppingCart(models.Model):
    """Модель списка покупок"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart_user',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart_recipe',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_recipe_in_shopping_cart',
            )
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Корзину покупок'
