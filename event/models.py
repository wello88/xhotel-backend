
# from django.db import models

# class Event(models.Model):
#     event_type = models.CharField(max_length=100)
#     event_id = models.TextField(unique=True)
#     check_in = models.DateTimeField(null=False, help_text="YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]")

#     def __str__(self):
#         return f"{self.event_type} - {self.event_id}"


from django.db import models

class Event(models.Model):
    event_type = models.CharField(max_length=100)
    event_id = models.TextField(default='some_default_value')  # Set your desired default value here
    check_in = models.DateTimeField(unique=True,null=False, help_text="YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]")

    def _str_(self):
        return f"{self.event_type} - {self.event_id}"