from . import dbconnection as db
from .abstractmodel import AbstractModel


class UserType(AbstractModel):
    def __init__(self, usertypeid):
        self.id = usertypeid
        self.build()

    class AccessibleModule():
        def __init__(self, mdata):
            self.id, self.packageid, self.classname, self.displayname, self.description, self.parentid, self.creationdate, self.updatedate, self.isdeleted = mdata

        def packagename(self):
            return db.submit_query('SELECT name FROM packages WHERE id = %s', (self.packageid,))[0][0]

    def build(self):
        self.name = db.submit_query('SELECT name FROM usertypes WHERE id = %s', (self.id, ))[0][0]
        self.options = db.submit_query('''
                                        SELECT name, type
                                        FROM usertypeoptions
                                        WHERE id IN (
                                            SELECT optionid
                                            FROM usertypeoptionmappings
                                            WHERE usertypeid = %s
                                        )
                                        ''', (self.id, ))

        # (module)id, importname, displayname, description, parentID
        accessiblemodulesdata = db.submit_query('''
                                                SELECT *
                                                FROM modules
                                                WHERE id IN (
                                                    SELECT module_id
                                                    FROM modulemappings
                                                    WHERE usertype_id = %s
                                                )
                                                ''', (self.id, ))

        self.accessiblemodules = []
        for mdata in accessiblemodulesdata: self.accessiblemodules.append(self.AccessibleModule(mdata))
