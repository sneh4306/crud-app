from sqlalchemy.ext.automap import automap_base
from config.database import Base, engine

# Option 1: If you want to automatically reflect the existing database
Base = automap_base()
Base.prepare(autoload_with=engine)
Books = Base.classes.books