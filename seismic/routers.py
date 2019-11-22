class CassandraRouter(object):
    def db_for_read(self, model, **hints):
        if model.__class__.__name__ in ['SeismicEvent', 'Weather']:
            return 'cassandra'
        else:
            return 'default'

    def db_for_write(self, model, **hints):
        if model.__class__.__name__ in ['SeismicEvent', 'Weather']:
            return 'cassandra'
        else:
            return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model=None, **hints):
        if model.__class__.__name__ in ['SeismicEvent', 'Weather']:
            return 'cassandra'
        else:
            return 'default'
