from fastapi import APIRouter, Depends, HTTPException
from schemas import schemas
from sqlalchemy.orm import Session
from config import propertyCrud, userCrud
from routes import access

propertyHandler = APIRouter()

@propertyHandler.post('/createProperty/')
def create_property(propertySchema: schemas.PropertySchema, db: Session = Depends(access.get_db)):
   db_user = userCrud.get_user(db, propertySchema.email_user)
    
   if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")

   return propertyCrud.create_property(db, propertySchema, db_user.id)

@propertyHandler.post('/deleteProperty/')
def delete_property(property_id: int, email_user: str, db: Session = Depends(access.get_db)):
   db_user = userCrud.get_user(db, email_user)

   if db_user is None:
      raise HTTPException(status_code=400, detail="Permission denied.")

   db_property = propertyCrud.get_property(db, property_id)

   if (db_property is None) or (db_property.user_id != db_user.id): 
      raise HTTPException(status_code=400, detail="Permission denied.")
   
   return propertyCrud.delete_property(db, db_property)

@propertyHandler.post('/updateProperty/')
def update_property(property_id: int, propertySchema: schemas.PropertySchema, db: Session = Depends(access.get_db)):
   db_user = userCrud.get_user(db, propertySchema.email_user)

   if db_user is None:
      raise HTTPException(status_code=400, detail="Permission denied.")

   db_property = propertyCrud.get_property(db, property_id)

   if (db_property is None) or (db_property.user_id != db_user.id):
      raise HTTPException(status_code=400, detail="Permission denied.")
   
   return propertyCrud.update_property(db, db_property, propertySchema)

@propertyHandler.post('/fetchAllUserProperties/')
def fetch_all_user_properties(email_user: str, db: Session = Depends(access.get_db)):
   db_user = userCrud.get_user(db, email_user)

   if db_user is None:
      raise HTTPException(status_code=400, detail="User not exist.")

   return propertyCrud.get_properties_by_user_id(db, db_user.id)