from base import engine
from tables import Base
from tables import PprRawAll

if __name__ == "__main__":
    Base.metadata.create_all(engine)