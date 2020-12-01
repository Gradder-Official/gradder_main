from bson import ObjectId
from flask.json import JSONEncoder


class JSONImproved(JSONEncoder):
    def default(self, obj):
        """Replaces the default :func:`~JSONEncoder.default` function

        Parameters
        ----------
        obj : any
            The object to convert

        Returns
        -------
        any
            The JSON valid object
        """
        if isinstance(obj, ObjectId):
            return str(obj)
        elif hasattr(obj, "to_dict"):
            return obj.to_dict()
        else:
            return obj
