from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///biudzetas.db')
Base = declarative_base()



class Pajamos(Base):
    __tablename__ = 'pajamos'
    id = Column(Integer, primary_key=True)
    suma = Column("suma", Float)
    siuntejas = Column("siuntejas", String)
    papildoma_informacija = Column("papildoma_informacija", String)


    def __init__(self, suma, siuntejas, papildoma_informacija):
        self.suma = suma
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

    def __repr__(self):
        return f"""
            suma: {self.suma},
            siuntėjas: {self.siuntejas},
            papildoma informacija: {self.papildoma_informacija}     
        """


class Islaidos(Base):
    __tablename__ = 'islaidos'
    id = Column(Integer, primary_key=True)
    suma = Column("suma", Float)
    atsiskaitymo_budas = Column("atsiskaitymo_budas", String)
    isigyta_preke_paslauga = Column("isigyta_preke_paslauga", String)


    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        self.suma = suma
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def __repr__(self):
        return f"""
            suma: {self.suma},
            atsiskaitymo būdas: {self.atsiskaitymo_budas},
            įsigyta prekė / paslauga: {self.isigyta_preke_paslauga}     
        """

Base.metadata.create_all(engine)