from models.categories import Category


def get_category_by_id(id: int) -> Category:
    obj = Category.query.get_or_404(id)

    return obj
