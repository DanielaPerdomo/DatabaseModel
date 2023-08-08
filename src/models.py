import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(25), nullable=False)
    favorites = relationship( "Favorites", back_populates="user")

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(50))
    birth_year = Column(Int(50))
    species = Column(String(50))
    height = Column(Int(50))
    mass = Column(Int(50))
    gender = Column(String(50))
    age = Column(Int(50))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    homeworld = Column(String(50))
    #Relacion con la tabla de Favoritos
    favorites = relationship("Favorites", back_populates="character")

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(50))
    population_number = Column(String(50))
    rotation_period = Column(String(50))
    orbital_period = Column(String(50)) 
    diameter = Column(String(50))
    gravity = Column(String(50))
    terrain = Column(String(50))
    surface = Column(String(50))
    climate = Column(String(50))
    #Relacion con la tabla de Favoritos
    favorites = relationship("Favorites" , back_populates="planets")

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    # Relacion con la tabla de Usuario
    id_user = Column(ForeignKey("user.id"))
    user = relationship( "User", back_populates = "favorites")
    #Relacion con la tabla de Planetas
    id_planets = Column(ForeignKey("planets.id"))
    planets = relationship(back_populates = "favorites")
    #Relacion con la tabla de Personajes
    id_characters = Column(ForeignKey("characters.id"))
    characters = relationship("characters", back_populates = "favorites")
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
