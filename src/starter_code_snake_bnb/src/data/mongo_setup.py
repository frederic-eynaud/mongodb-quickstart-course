import mongoengine

alias_core = 'core'
db = 'snakebnb'

def grobal_init():
    mongoengine.register_connection(alias=alias_core, name=db)
 