from django.db import models
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=False)
    password = models.CharField(max_length=100,null=False)
    role = models.CharField(max_length=100,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'

    def str(self):
        return self.name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'category'

    def str(self):
        return self.name


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=False)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'post'

    def str(self):
        return self.title
    
    
    
    
    
    

    
