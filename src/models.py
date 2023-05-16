import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    people = relationship("Films")
    vehicles = relationship ("Vehicles")

  
   


class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    director = Column(String(250))
    episode_id = Column(String(250), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'))
    elenco = relationship ("Elenco")
    vehicles = relationship ("Vehicles")
    


class Elenco (Base):
    __tablename__ = 'Elenco'
    id = Column(Integer, primary_key=True)

    films_id = Column(Integer, ForeignKey('films.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))

    # film = relationship("Films", backref="elenco")
    # planets = relationship("Planets", backref ="elenco")
    # vehicles = relationship("Vehicles", backref ="elenco")

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model= Column(String(250), nullable=False)
    vehicle_class= Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    films_id = Column(Integer, ForeignKey('films.id')) 
    pilots_id = Column(Integer, ForeignKey('people.id'))
    elenco = relationship ("Elenco")

class Planets(Base):
    __tablename__= "planets"
    id = Column(Integer, primary_key=True)
    climate= Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    people = relationship ("People")
    elenco = relationship ("Elenco")


def to_dict(self):
    return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
