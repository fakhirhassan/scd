from django import forms
from .models import Team

class TeamRegistrationForm(forms.ModelForm):
    class Meta:
        model = Team
        
        fields = [
            'team_name',
            'player_1_id', 'player_1_name',
            'player_2_id', 'player_2_name',
            'player_3_id', 'player_3_name',
            'player_4_id', 'player_4_name',
            'substitute_id', 'substitute_name'
        ]
        widgets = {
            'team_name': forms.TextInput(attrs={'placeholder': 'Enter Team Name'}),
            'player_1_id': forms.TextInput(attrs={'placeholder': 'Enter Player 1 ID'}),
            'player_1_name': forms.TextInput(attrs={'placeholder': 'Enter Player 1 Name'}),
            'player_2_id': forms.TextInput(attrs={'placeholder': 'Enter Player 2 ID'}),
            'player_2_name': forms.TextInput(attrs={'placeholder': 'Enter Player 2 Name'}),
            'player_3_id': forms.TextInput(attrs={'placeholder': 'Enter Player 3 ID'}),
            'player_3_name': forms.TextInput(attrs={'placeholder': 'Enter Player 3 Name'}),
            'player_4_id': forms.TextInput(attrs={'placeholder': 'Enter Player 4 ID'}),
            'player_4_name': forms.TextInput(attrs={'placeholder': 'Enter Player 4 Name'}),
            'substitute_id': forms.TextInput(attrs={'placeholder': 'Enter Substitute Player ID'}),
            'substitute_name': forms.TextInput(attrs={'placeholder': 'Enter Substitute Player Name'}),
        }
