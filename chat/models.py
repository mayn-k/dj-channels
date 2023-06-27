from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Room represents a chat room. It contains an online field for tracking when users connect and disconnect from the chat room.
class Room(models.Model):
    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=User, blank=True)

    def get_online_count(self):
        return self.online.count()
    

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()


    def __str__(self):
        return "{} ({})".format(self.name, self.get_online_count())
    


# Message represents a message sent to the chat room. We'll use this model to store all the messages sent in the chat.
class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{}: {} [{}]".format(self.user.username, self.content, self.timestamp)