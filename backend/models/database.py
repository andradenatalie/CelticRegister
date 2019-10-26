from backend.data.alchemy import alchemy


class Celtic(alchemy.Model):
    __tablename__ = "celtic"
    _id = alchemy.Column(alchemy.Integer, primary_key=True, autoincrement=True)
    name = alchemy.Column(alchemy.String)
    location = alchemy.Column(alchemy.String)
    wars = alchemy.Column(alchemy.String)
    properties = alchemy.Column(alchemy.String)
    times = alchemy.Column(alchemy.String)
