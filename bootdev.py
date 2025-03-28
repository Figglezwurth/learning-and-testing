can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    can_create_guild & user_permissions
    return get_create_bits


def get_review_bits(user_permissions):
    can_review_guild & user_permissions
    return get_review_bits

def get_delete_bits(user_permissions):
    can_delete_guild & user_permissions
    return get_delete_bits


def get_edit_bits(user_permissions):
    can_edit_guild & user_permissions
    return get_edit_bits
