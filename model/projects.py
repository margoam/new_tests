from sys import maxsize


class Project:

    def __init__(self, name=None, status=None, global_categories=None, view_status=None,
                 description=None, id=None):
        self.name = name
        self.status = status
        self.global_categories = global_categories
        self.view_status =view_status
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s %s %s %s %s" % (self.name, self.status, self.global_categories, self.view_status,
                                   self.description)

    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name) and \
               (self.status is None or other.status is None or self.status == other.status) and \
               (self.global_categories is None or other.global_categories is None or
                self.global_categories == other.global_categories) and\
               (self.view_status is None or other.view_status is None or
                self.view_status == other.view_status) and \
               (self.description is None or other.description is None or
                self.description == other.description) and (self.id is None or other.id or self.id == other.id)

    def compare_name(self):
        return self.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
