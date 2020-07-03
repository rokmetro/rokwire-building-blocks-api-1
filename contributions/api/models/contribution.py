import utils.datasetutils as datasetutils

class Contribution():
    def __init__(self, injson):
        self.name = None
        self.shortDescription = None
        self.longDescription = None
        self.capabilities = None
        self.talents = None
        self.dateCreated = None
        self.dateModified = None

        self, restjson = datasetutils.update_contribution_dataset_from_json(self, injson)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_short_description(self, shortDescription):
        self.shortDescription = shortDescription

    def get_short_description(self):
        return self.shortDescription

    def set_long_description(self, longDescription):
        self.longDescription = longDescription

    def get_long_description(self):
        return self.longDescription

    def set_capabilities(self, capabilities):
        self.capabilities = capabilities

    def get_capabilities(self):
        return self.capabilities

    def set_talents(self, talents):
        self.talents = talents

    def get_talents(self):
        return self.talents

    def set_contacts(self, contacts):
        self.contacts = contacts

    def get_contacts(self):
        return self.contacts

    def set_date_created(self, dateCreated):
        self.dateCreated = dateCreated

    def get_date_created(self):
        return self.dateCreated

    def set_date_modified(self, dateModified):
        self.dateModified = dateModified

    def get_date_modified(self):
        return self.dateModified