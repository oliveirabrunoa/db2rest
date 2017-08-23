class {{ class_name }}(Base):
    __tablename__ = "{{ table_name }}"
    __table_args__ = ({'autoload':True})

    id = Column(Integer, primary_key=True)
    description = Column(String(50))

    def __init__(self, id, description, *args):
        self.id = id
        self.description = description
