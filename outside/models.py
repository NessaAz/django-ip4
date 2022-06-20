from email.mime import image
from django.db import models
from django.contrib.auth.models import User


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    occupants = models.IntegerField(default=1, blank=True, null=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    @classmethod
    def get_neighborhood(cls, id):
        neighborhood = cls.objects.get(id=id)
        return neighborhood

    def create_neighborhood(self):
        self.save()
        return self

    @classmethod
    def delete_neighborhood(cls, id):
        neighborhood = cls.objects.get(id=id).delete()
        return neighborhood

    @classmethod
    def update_neighborhood(cls, obj):
        neighborhood = cls.get_neighborhood(obj.id)
        neighborhood.name = obj.name
        neighborhood.location = obj.location
        neighborhood.save()
        return neighborhood

    def update_occupants(self, occupants):
        self.occupants += occupants
        self.save()
        return self

    def __str__(self):
        return self.location        
    
class Business(models.Model):
    name = models.CharField(max_length=55, unique=True)
    user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, related_name='hood', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    established = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    @classmethod
    def get_business(cls, id):
        business = cls.objects.get(id=id)
        return business

    def create_business(self):
        self.save()
        return self

    @classmethod
    def delete_business(cls, id):
        business = cls.objects.get(id=id).delete()
        return business

    @classmethod
    def update_business(cls, obj):
        business = cls.get_business(obj.id)
        business.name = obj.name
        business.neighborhood = obj.neighborhood
        business.email = obj.email
        business.save()
        return business


def __str__(self):
    return self.name
        
        
class Post(models.Model):
    user = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    post = models.TextField()
    comments = models.ManyToManyField('Comment', related_name='comments', blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.post        
    
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment    
    
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
    
class Profile( models.Model ):
    objects=None
    profilePic=models.ImageField( upload_to='profile/' , null=True , blank=True )
    #contact=HTMLField( max_length=60 , null=True )
    bio=models.CharField( max_length=200 , blank=True )
    user=models.ForeignKey( User , on_delete=models.CASCADE , related_name='profile' , null=True )
    email=models.TextField( max_length=200 , null=True , blank=True , default=0 )

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save( )

    def delete_profile(self):
        self.delete( )

    @classmethod
    def get_profile(cls):
        profile=Profile.objects.all( )
        return profile

    @classmethod
    def find_profile(cls , search_term):
        profile=cls.objects.filter( user__username__icontains=search_term )
        return profile        