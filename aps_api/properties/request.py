keys_welfare = {
    'id': 'id',
    'family': 'family'    
}

keys_pipeline = {
    'id': 'id',
    'entity': 'entity',
    'person': 'person'    
}

keys_channel_entity = {
    'id': 'id',
    'contact': 'contact',
    'pollster': 'pollster'
}

keys_info_general = {
    'id': 'id',
    'pollster': 'pollster',
    'id_familia': 'id_familia',
}

keys_family = {
    'id': 'id',
    'info_general': 'info_general',

}

keys_field = {
    'id': 'id',
    'pollster': 'pollster'
}


keys_family_context = {
    'id': 'id',
    'family': 'family',
}

keys_sanation = {
    'id': 'id',
    'living_place_id': 'living_place_id',
}

keys_member = {
    'id': 'id',
    'family': 'family',
    'sex': 'sex',
    'last_update': 'last_update',
    'eps': 'eps'
}


keys_pollster = {
    'id': 'id',
}

keys_member_atributes = {
    'id': 'id',
    'member': 'member',
}

mss = (
    'No records found',
    'Error',
    'This item already exists',
    'The object with this id does not exist',
    'Item deleted successfully.',
    'Login successful',
    'Credentials Invalid',
    'logut successful ',
    'Ya existe esta cedula '
)

url = (
    'info_general/add/',
    'info_general/',
    'info_general/update/<int:pk>/',
    'info_general/<int:pk>/delete/',
    'family/add/',
    'family/',
    'family/update/<int:pk>/',
    'family/<int:pk>/delete/',
    'member/add/',
    'member/',
    'member/update/<int:pk>/',
    'member/<int:pk>/delete/',
    'family_context/add/',
    'family_context/',
    'family_context/update/<int:pk>/',
    'family_context/<int:pk>/delete/',
    'living_place/add/',
    'living_place/',
    'living_place/update/<int:pk>/',
    'living_place/<int:pk>/delete/',
    'sanation/add/',
    'sanation/',
    'sanation/update/<int:pk>/',
    'sanation/<int:pk>/delete/',
    'atributes_member/add/',
    'atributes_member/',
    'atributes_member/update/<int:pk>/',
    'atributes_member/<int:pk>/delete/',
    'pollster/add/',
    'pollster/',
    'pollster/update/<int:pk>/',
    'pollster/<int:pk>/delete/',
    'login/',
    'register/',
    'logout/',
    'channel_entity/add/',
    'channel_entity/',
    'channel_entity/update/<int:pk>/',
    'channel_entity/<int:pk>/delete/',
    'pipeline/add/',
    'pipeline/',
    'pipeline/update/<int:pk>/',
    'pipeline/<int:pk>/delete/',
    'welfare/add/',
    'welfare/',
    'welfare/update/<int:pk>/',
    'welfare/<int:pk>/delete/',
    'family/<int:pk>/pollster/',
    'info_general/<int:pk>/donut/',
    'family/<int:pk>/filter/',
    'family_context/barchart/',
    'family_context/barchart/antecedent/',
    'family_context/donut/victim/',
    'family/all_info/',
    'family/donut/total_family/',
    'member/bar_list/sex/',
    'infoGeneral/barchart/estratum/',
    'member/donut/affiliation_regime/',
    'member/barChart/etnia/',
    'atributesMember/donut/sport/',
    'family_context/donut/disability/',
    'family_context/donut/disease_prevention/',
    'family_context/barChart/healthy_habits/',
    'new_fields/add/',
    'new_fields/',
    'new_fields/update/<int:pk>/',
    'new_fields/<int:pk>/delete/',
    'family_detail/<int:pk>/',
    'familyContext_detail/<int:pk>/',
    'familyMember/<int:pk>/',#path nuevo
    'user/update/<int:pk>/',
    'user/',
    'user/recovery/',
    'reset/password/<int:pk>/'
)

name = (
    'add-items',
    'view_items',
    'update-items',
    'delete-items',
    'login',
    'register',
    'logout',
)
