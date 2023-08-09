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
    password = Column(String(20), nullable=False)
    #Relacion con la Tabla Favorites
    id_favorites = Column(ForeignKey("favorites.id"))
    favorites = relationship( "Favorites", back_populates = "user")
    #Relacion con la Tabla character
    id_character = Column(ForeignKey("characters.id"))
    character = relationship("Characters", back_populates = "user")
    #Relacion con la Tabla Planets
    id_planets = Column(ForeignKey("planets.id"))
    planets = relationship( "Planets", back_populates = "user")

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    homeworld = Column(String(10), nullable=False)
    #Relacion con la Tabla Favorites
    favorites = relationship("Favorites", back_populates="characters")

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    #Relacion con la Tabla Favorites
    favorites = relationship("Favorites", back_populates="planets")
    
class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    #Relacion con la Tabla User
    id_user = Column(ForeignKey("users.id")) 
    users = relationship( "Users", back_populates = "favorites")
    #Relacion con la Tabla Character
    id_character = Column(ForeignKey("characters.id"))
    character = relationship("Characters", back_populates = "favorites")
    #Relacion con la Tabla Planets
    id_planets = Column(ForeignKey("planets.id"))
    planets = relationship( "Planets", back_populates = "favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')