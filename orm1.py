import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "page_demo.settings")
    os.environ["DJANGO_SETTINGS_MODULE"] = "page_demo.settings"

    import django
    django.setup()

    from app01 import models
    # 批量创建
    # 有100个书籍对象
    # objs = [models.Book(title="书本{}".format(i)) for i in range(1000)]
    #
    # # 在数据库中批量创建, 10次一提交
    # models.Book.objects.bulk_create(objs, 100)

    models.Book.objects.all().delete()