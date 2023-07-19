from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from users.exceptions import AlreadyExistsError, AlreadyFriendsError

class User(AbstractUser):
    book_author_staff = models.BooleanField(default=False)
    profile_picture = models.ImageField(default='def_pic.jpeg')
    country = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=200,default='')


class FriendsRequest(models.Model):
    
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="requester",)
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="receiver",)

    message = models.TextField(_("Message"), blank=True)

    created = models.DateTimeField(default=timezone.now)
    rejected = models.DateTimeField(blank=True, null=True)
    viewed = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _("Friend Request")
        verbose_name_plural = _("Friend Requests")
        unique_together = ("from_user", "to_user")

    def __str__(self):
        return f"User #{self.from_user} friend requested #{self.to_user}"
    
    def accept(self):
        Friends.objects.create(from_user=self.from_user, to_user=self.to_user)
        Friends.objects.create(from_user=self.to_user, to_user=self.from_user)
        
        
        self.delete()
        FriendsRequest.objects.filter(from_user=self.from_user, to_user=self.to_user).delete()
        return True
    
    def rejected(self):
        self.rejected = timezone.now()
        self.save()
        return True
    
    def cancel(self):
        self.delete()
        return True
    
    def mark_viewed(self):
        self.viewed = timezone.now()
        self.save()
        return True


class FriendsManager(models.Manager):
    
    def friends(self, user):
        qs = Friends.objects.filter(from_user=user)
        
        friends = [u.to_user for u in qs]
        
        return friends
    
    def add_friend(self, from_user, to_user, message=None):
        
        if from_user==to_user:
            raise ValidationError("Foydalanuvchi o'zi bilan o'zi do'st bo'la olmaydi!")
        
        if self.are_friends(from_user,to_user):
            raise AlreadyFriendsError("Foydalanuvchilar allaqachon do'stlar.")
        
        if FriendsRequest.objects.filter(from_user=from_user,to_user=to_user).exists():
            raise AlreadyExistsError("Friend already requested")
        
        if FriendsRequest.objects.filter(from_user=to_user,to_user=from_user).exists():
            raise AlreadyExistsError("Friend already requested")
        
        if message is None:
            message = ""
        
        request, created = FriendsRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
        
        if created is False:
            raise AlreadyExistsError("Friend already requested")
        
        if message:
            request.message = message
            request.save()
        
        return request
    
    def remove_friend(self, from_user, to_user):
        try:
            qs = Friends.objects.filter(to_user__in=[to_user, from_user], from_user__in=[from_user,to_user])
            if qs:
                qs.delete()
                return True
            else:
                return False
        except Friends.DoesNotExist:
            return False
    
    
    def are_friends(self, user1, user2):
        friends1 = self.friends(user1)
        friends2 = self.friends(user2)
        
        if friends1 and user2 in friends1:
            return True
        elif friends2 and user1 in friends2:
            return True
        else:
            try:
                Friends.objects.get(to_user=user1, from_user=user2)
                return True
            except Friends.DoesNotExist:
                return False
     

class Friends(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="_unused_friend_relation")
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="friends")
    created = models.DateTimeField(default=timezone.now)
    
    objects = FriendsManager()
    
    class Meta:
        verbose_name = _("Friend")
        verbose_name_plural = _("Friends")
        unique_together = ("from_user", "to_user")
        
    
    def __str__(self):
        return f"{self.from_user_id} friends to {self.to_user_id}"
    
    
    def save(self, *args, **kwargs):
        if self.from_user==self.to_user:
            raise ValidationError("Foydalanuvchilar o'zlariga do'stlik so'rovi yuborolmaydilar!")
        super().save(*args, **kwargs)
