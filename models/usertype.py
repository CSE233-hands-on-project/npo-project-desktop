from . import dbconnection as db
from .abstractmodel import AbstractModel


class UserType(AbstractModel):
    def __init__(self, usertypeid):
        self.id = usertypeid
        self.build()

    class AccessibleModule():
        def __init__(self, mdata):
            self.id, self.packageid, self.classname, self.displayname, self.description, self.parentid = mdata

        def packagename(self):
            return db.submit_query(f'SELECT name FROM packages WHERE id = {self.packageid}')[0][0]

    def build(self):
        self.name = db.submit_query(f'SELECT name FROM usertypes WHERE id = {self.id}')[0][0]
        self.options = db.submit_query(f'''
                                        SELECT name, type
                                        FROM usertypeoptions
                                        WHERE id IN (
                                            SELECT optionid
                                            FROM usertypeoptionmappings
                                            WHERE usertypeid = {self.id}
                                        )
                                        ''')

        # (module)id, importname, displayname, description, parentID
        accessiblemodulesdata = db.submit_query(f'''
                                                SELECT *
                                                FROM modules
                                                WHERE id IN (
                                                    SELECT module_id
                                                    FROM modulemappings
                                                    WHERE usertype_id = {self.id}
                                                )
                                                ''')

        self.accessiblemodules = []
        for mdata in accessiblemodulesdata: self.accessiblemodules.append(self.AccessibleModule(mdata))
