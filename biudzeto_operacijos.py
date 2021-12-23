from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import duomenu_baze


engine = create_engine('sqlite:///biudzetas.db')
Session = sessionmaker(bind=engine)

ispejimas = "neteisingas duomenų formatas, reikia įvesti skaičių"



def prideti_pajamu_irasa(suma, siuntejas, papildoma_informacija):
    session = Session()
    irasas = duomenu_baze.Pajamos(suma, siuntejas, papildoma_informacija)
    session.add(irasas)
    session.commit()


def prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga):
    session = Session()
    irasas = duomenu_baze.Islaidos(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
    session.add(irasas)
    session.commit()

def suskaiciuoti_pajamas():
    session = Session()
    pajamu_irasai = session.query(duomenu_baze.Pajamos.suma)
    session.commit()
    pajamos = sum([irasas[0] for irasas in pajamu_irasai])
    return pajamos


def suskaiciuoti_islaidas():
    session = Session()
    islaidu_irasai = session.query(duomenu_baze.Islaidos.suma)
    session.commit()
    islaidos = sum([irasas[0] for irasas in islaidu_irasai])
    return islaidos

def skaiciuoti_biudzeto_balansa():
    pajamos = suskaiciuoti_pajamas()
    islaidos = suskaiciuoti_islaidas()
    balansas = pajamos - islaidos
    return pajamos, islaidos, balansas

def parodyti_biudzeto_ataskaita():
    session = Session()
    pajamu_irasai = session.query(duomenu_baze.Pajamos)
    islaidu_irasai = session.query(duomenu_baze.Islaidos)
    session.commit()
    return list(pajamu_irasai), list(islaidu_irasai)

