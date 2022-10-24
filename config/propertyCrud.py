from sqlalchemy.orm import Session
from schemas.propertySchema import PropertySchema
from models.propertie import Property

def get_property(db: Session, property_id: int):
    return db.query(Property).filter(Property.id == property_id).first()

def get_properties_by_user_id(db: Session, user_id: int):
    return db.query(Property).filter(Property.user_id == user_id).all()

def create_property(db: Session, propertySchema: PropertySchema, user_id: int):
    db_property = Property(
                            direction=propertySchema.direction, 
                            province=propertySchema.province, 
                            location=propertySchema.location, 
                            country=propertySchema.country, 
                            toilets=propertySchema.toilets, 
                            rooms=propertySchema.rooms,
                            people=propertySchema.people, 
                            description=propertySchema.description, 
                            link=propertySchema.link,
                            user_id=user_id
                        )
    db.add(db_property)
    db.commit() 
    db.refresh(db_property)
    return db_property

def delete_property(db: Session, db_property):
    db.delete(db_property)
    db.commit()
    return db_property

def update_property(db: Session, db_property, propertySchema: PropertySchema):
    db_property.direction = propertySchema.direction
    db_property.province = propertySchema.province 
    db_property.location = propertySchema.location 
    db_property.country = propertySchema.country 
    db_property.toilets = propertySchema.toilets 
    db_property.rooms = propertySchema.rooms
    db_property.people = propertySchema.people 
    db_property.description = propertySchema.description
    db_property.link = propertySchema.link                              
    db.add(db_property)
    db.commit()
    return db_property