from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    player_1_id = models.CharField(max_length=100)
    player_1_name = models.CharField(max_length=100)
    player_2_id = models.CharField(max_length=100)
    player_2_name = models.CharField(max_length=100)
    player_3_id = models.CharField(max_length=100)
    player_3_name = models.CharField(max_length=100)
    player_4_id = models.CharField(max_length=100)
    player_4_name = models.CharField(max_length=100)
    substitute_id = models.CharField(max_length=100)
    substitute_name = models.CharField(max_length=100)
    tournament = models.CharField(max_length=100)


    def __str__(self):
        return self.team_name
    
class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    developer = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='game_covers/')  

    def __str__(self):
        return self.title
