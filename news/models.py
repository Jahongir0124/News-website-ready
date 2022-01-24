from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=400,null=True)


    def __str__(self):
        return self.category_name
class Info(models.Model):
    cat_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    info_name=models.CharField(max_length=200,null=False)
    info=models.TextField()
    image=models.ImageField(upload_to='images/')
    tag=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.info
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
             url= "Rasm yoq"
        return url



