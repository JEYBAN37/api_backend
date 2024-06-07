from rest_framework import serializers
from aps_api.managers.familyContext import FamilyContext
from aps_api.properties.coverters import yn_mapping

class FamilyContextSerializers(serializers.ModelSerializer):
    class Meta:
        model = FamilyContext
        fields = '__all__'


class CustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = FamilyContext
        fields = ['id', 'family', 'vulneravility', 'risk_psychosocial', 'disable', 'victim',
                  'patient','infected_person', 'event_noted','younger','pregnant','senior', 'healthy_habits', 'socioemotional',
                  'environment_care','healthy_relationships', 'health_support', 'senior_protection', 'family_welfare', 'scl_conservation']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        if 'victim' in data:
            data['victim'] = yn_mapping.get(data['victim'], data['victim'])
        
        if 'vulneravility' in data:
            data['vulneravility'] = yn_mapping.get(data['vulneravility'], data['vulneravility'])
            
        if 'risk_psychosocial' in data:
            data['risk_psychosocial'] = yn_mapping.get(data['risk_psychosocial'], data['risk_psychosocial'])
        
        if 'disable' in data:
            data['disable'] = yn_mapping.get(data['disable'], data['disable'])
        
        if 'patient' in data:
            data['patient'] = yn_mapping.get(data['patient'], data['patient'])
        
        if 'younger' in data:
            data['younger'] = yn_mapping.get(data['younger'], data['younger'])
        
        if 'pregnant' in data:
            data['pregnant'] = yn_mapping.get(data['pregnant'], data['pregnant'])
        
        if 'senior' in data:
            data['senior'] = yn_mapping.get(data['senior'], data['senior'])
        
        if 'event_noted' in data:
            data['event_noted'] = yn_mapping.get(data['event_noted'], data['event_noted'])
        
        if 'healthy_habits' in data:
            data['healthy_habits'] = yn_mapping.get(data['healthy_habits'], data['healthy_habits'])
        
        if 'socioemotional' in data:
            data['socioemotional'] = yn_mapping.get(data['socioemotional'], data['socioemotional'])
        
        if 'environment_care' in data:
            data['environment_care'] = yn_mapping.get(data['environment_care'], data['environment_care'])
        
        if 'healthy_relationships' in data:
            data['healthy_relationships'] = yn_mapping.get(data['healthy_relationships'], data['healthy_relationships'])
        
        if 'health_support' in data:
            data['health_support'] = yn_mapping.get(data['health_support'], data['health_support'])
        
        if 'scl_conservation' in data:
            data['scl_conservation'] = yn_mapping.get(data['scl_conservation'], data['scl_conservation'])
        
        if 'family_welfare' in data:
            data['family_welfare'] = yn_mapping.get(data['family_welfare'], data['family_welfare'])
        
        if 'senior_protection' in data:
            data['senior_protection'] = yn_mapping.get(data['senior_protection'], data['senior_protection'])            
        return data


class CustomUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = FamilyContext
        read_only_fields = ['id', 'family']



class FamilyContextAnaliticSerializers(serializers.ModelSerializer):
    class Meta:
        model = FamilyContext
        fields = ['id', 'victim','vulneravility','healthy_habits','antecedent_salud','family_welfare']
