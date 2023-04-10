def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    categories_list = []
    for categoryId in mapping['categoryIdsSorted']:
        category = []
        for roleId in mapping['categories'][categoryId]['roleIds']:
            category += [{'id': roleId, 'text': mapping['roles'][roleId]['name']}]
        categories_list += [{'id': 'category-' + categoryId, 'text': mapping['categories'][categoryId]['name'], 'items': category}]
    return {"categories": categories_list}