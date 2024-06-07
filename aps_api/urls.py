from django.urls import path
from aps_api.views.loginView import LoginView
from .views import (infoGeneralView, familyView, memberView, familyContextView, livingPlceView, sanitationView,
                    atributesMemberView, pollsterView, userView, channelEntityView, pipelineView, welfareView,
                    NewFieldsView)
from .properties.request import url, name
from .views.familyView import FamilyListView

urlpatterns = [
    path(url[32], LoginView.as_view(), name=name[4]),
    path(url[33], userView.register, name=name[5]),
    path(url[34], userView.out, name=name[6]),
    path(url[70], userView.update_items, name=name[6]),
    path(url[71], userView.view_items, name=name[6]),
    path(url[72],userView.recovery_item, name=name[6]),
    path(url[73],userView.reset_password, name=name[6]),

    path('get-csrf-token/', userView.token_generate, name='token'),

    path(url[0], infoGeneralView.add_item, name=name[0]),
    path(url[1], infoGeneralView.view_items, name=name[1]),
    path(url[2], infoGeneralView.update_items, name=name[2]),
    path(url[3], infoGeneralView.delete_item, name=name[3]),
    path(url[48], infoGeneralView.counter_families, name=name[3]),
    path(url[56], infoGeneralView.count_stratum, name=name[3]),
    path(url[74], infoGeneralView.view_items_analitic, name=name[3]),

    path(url[4], familyView.add_item, name=name[0]),
    path(url[5], familyView.view_items, name=name[1]),
    path(url[6], familyView.update_items, name=name[2]),
    path(url[7], familyView.delete_item, name=name[3]),
    path(url[47], familyView.view_items_pollster, name=name[3]),
    path(url[49], FamilyListView.as_view(), name=name[3]),
    path(url[53], familyView.view_items_all, name=name[3]),
    path(url[54], familyView.count_family, name=name[3]),
    path(url[67], familyView.get_family_by_id, name=name[3]),

    path(url[8], memberView.add_item, name=name[0]),
    path(url[9], memberView.view_items, name=name[1]),
    path(url[10], memberView.update_items, name=name[2]),
    path(url[11], memberView.delete_item, name=name[3]),
    path(url[55], memberView.count_sex, name=name[3]),
    path(url[57], memberView.count_affiliation_regime, name=name[3]),
    path(url[58], memberView.count_etnia, name=name[3]),
    path(url[69], memberView.get_member_family_by_id, name=name[3]),#path nuevo

    path(url[12], familyContextView.add_item, name=name[0]),
    path(url[13], familyContextView.view_items, name=name[1]),
    path(url[14], familyContextView.update_items, name=name[2]),
    path(url[15], familyContextView.delete_item, name=name[3]),
    path(url[50], familyContextView.count_vulnerability, name=name[3]),
    path(url[51], familyContextView.count_antecedent_salud, name=name[3]),
    path(url[52], familyContextView.count_victim, name=name[3]),
    path(url[60], familyContextView.count_disability, name=name[3]),
    path(url[61], familyContextView.count_disease_prevention, name=name[3]),
    path(url[62], familyContextView.count_healthy_habits, name=name[3]),
    path(url[68], familyContextView.get_familyContext_by_id, name=name[3]),

    path(url[16], livingPlceView.add_item, name=name[0]),
    path(url[17], livingPlceView.view_items, name=name[1]),
    path(url[18], livingPlceView.update_items, name=name[2]),
    path(url[19], livingPlceView.delete_item, name=name[3]),

    path(url[20], sanitationView.add_item, name=name[0]),
    path(url[21], sanitationView.view_items, name=name[1]),
    path(url[22], sanitationView.update_items, name=name[2]),
    path(url[23], sanitationView.delete_item, name=name[3]),


    path(url[24], atributesMemberView.add_item, name=name[0]),
    path(url[25], atributesMemberView.view_items, name=name[1]),
    path(url[26], atributesMemberView.update_items, name=name[2]),
    path(url[27], atributesMemberView.delete_item, name=name[3]),
    path(url[59], atributesMemberView.count_sport, name=name[3]),

    path(url[28], pollsterView.add_item, name=name[0]),
    path(url[29], pollsterView.view_items, name=name[1]),
    path(url[30], pollsterView.update_items, name=name[2]),
    path(url[31], pollsterView.delete_item, name=name[3]),
    
    path(url[35], channelEntityView.add_item, name=name[0]),
    path(url[36], channelEntityView.view_items, name=name[1]),
    path(url[37], channelEntityView.update_items, name=name[2]),
    path(url[38], channelEntityView.delete_item, name=name[3]),
    
    path(url[39], pipelineView.add_item, name=name[0]),
    path(url[40], pipelineView.view_items, name=name[1]),
    path(url[41], pipelineView.update_items, name=name[2]),
    path(url[42], pipelineView.delete_item, name=name[3]),
    
    path(url[43], welfareView.add_item, name=name[0]),
    path(url[44], welfareView.view_items, name=name[1]),
    path(url[45], welfareView.update_items, name=name[2]),
    path(url[46], welfareView.delete_item, name=name[3]),

    path(url[63], NewFieldsView.add_item, name=name[0]),
    path(url[64], NewFieldsView.view_items, name=name[1]),
    path(url[65], NewFieldsView.update_items, name=name[2]),
    path(url[66], NewFieldsView.delete_item, name=name[3]),
]
